# Fed-Batch Bioreactor Modeling Using Monod Kinetics

This project implements a mechanistic computational model of fed-batch bioreactor systems using Monod kinetics.

The model is based on mass balances for biomass (X), substrate (S), product (P), and reactor volume (V), and is solved using SciPy's ODE solver.

## Objectives
- Model fed-batch bioreactor dynamics
- Investigate the effect of feed rate on biomass, substrate, and product concentrations

## Methods
- Monod growth kinetics
- Ordinary differential equations derived from mass balances
- Solved in python using `scipy.integrate.odeint`

## Results
Simulations show that increasing feed rate leads to higher biomass, substrate, and product accumulation, with diminishing marginal gains at higher feed rates.

## Tools Used
- Python
- NumPy
- SciPy
- Matplotlib

## Future Work
- Implement exponential feeding strategies
- Fit model parameters to experimental data

