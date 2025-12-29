import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt



# PARAMETERS

mu_max = 0.4      # maximum specific growth rate, 1/hr
Ks = 0.5          # g/L
Yxs = 0.5         # gX / gS
alpha = 0.1       # gP / gX



# FEED RATE PARAMETERS

F_values = [0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]         # feed rate, L/h
# independent variable in our experiment
                                    
Sf = 100.0                                                # substrate in feed, g/L



# INITIAL CONDITIONS

X0 = 0.1                        # cell concentration, g/L
S0 = 20.0                       # substrate concentration, g/L
P0 = 0.0                        # product concentration, g/L
V0 = 100.0                      # volume of reactor (L)

y0_feed = [X0, S0, P0, V0]      #vector for all state variables



# TIME GRID

t = np.linspace(0, 30, 300)     # hours



# MASS BALANCE AND MONOD KINEMATICS CALCULATIONS

def bioreactor_feed(y, t, mu_max, Ks, Yxs, alpha, F, Sf):
    X, S, P, V = y
    mu = mu_max * S / (Ks + S)
    dVdt = F
    dXdt = mu * X - (F/V) * X
    dSdt = (F/V) * (Sf - S) - (1 / Yxs) * mu * X
    dPdt = alpha * mu * X - (F/V) * P
    
    return [dXdt, dSdt, dPdt, dVdt]



# RESULT CALCULATIONS

results = []        # this will hold our dependent variables for our experiment

for F in F_values:
    solution_feed = odeint(bioreactor_feed, y0_feed, t, args=(mu_max, Ks, Yxs, alpha, F, Sf))

    #odient solves systems in this format: dy/dt = f(y,t)   ...
    #...where y is vector of state variables and f is function returning their derivatives
    #args are constants used inside bioreactor function that don't fit in odeint() format

    Xf, S_f, Pf, Vf = solution_feed.T    #array unpacking

    results.append({"F": F, "X_final": Xf[-1], "S_final": S_f[-1], "P_final": Pf[-1], "V_final": Vf[-1]})



# DATA PLOTTING

Fs = [r["F"] for r in results]
Xfinal = [r["X_final"] for r in results]
Sfinal = [r["S_final"] for r in results]
Pfinal = [r["P_final"] for r in results]
Vfinal = [r["V_final"] for r in results]

plt.figure()
plt.plot(Fs, Xfinal, marker='o')
plt.xlabel("Feed Rate F (L/hr)")
plt.ylabel("Final Biomass X (g/L)")
plt.title("Effect of Feed Rate on Final Biomass")
plt.show()

plt.figure()
plt.plot(Fs, Sfinal, marker='o')
plt.xlabel("Feed Rate F (L/hr)")
plt.ylabel("Final Sustrate S (g/L)")
plt.title("Effect of Feed Rate on Final Substrate")
plt.show()

plt.figure()
plt.plot(Fs, Pfinal, marker='o')
plt.xlabel("Feed Rate F (L/hr)")
plt.ylabel("Final Product P (g/L)")
plt.title("Effect of Feed Rate on Final Product")
plt.show()

plt.figure()
plt.plot(Fs, Vfinal, marker='o')
plt.xlabel("Feed Rate F (L/hr)")
plt.ylabel("Final Volume V (L)")
plt.title("Effect of Feed Rate on Final Volume")
plt.show()
