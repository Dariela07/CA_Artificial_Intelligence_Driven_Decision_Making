from mip import Model, xsum, maximize, INTEGER, MAXIMIZE
import numpy as np

# Create an empty optimization model for solving Mixed-Integer Linear Programming problem
m = Model("ProductManufacture", sense=MAXIMIZE)
L = [2, 3, 1, 4, 5]  # Required labour units for the five products
M = [3, 2, 4, 1, 3]  # Required units of machine time for the five products
R = [4, 1, 3, 2, 2]  # The required raw material units for the five products
Pr = [5, 4, 6, 7, 8]  # Generated profits in dollars($) for the five products
I = range(len(Pr))  # The number of different products

# Define decision variables Xi. Production units must be integer, and cannot be negative (lower bound is 0).
X = [m.add_var(var_type=INTEGER, lb=0) for i in I]
# Define the objective function
m.objective = maximize(xsum(Pr[i] * X[i] for i in I))
# Add Constraints
# Resource constraints (a. Total available labour: 100 units; b. Total available machine time: 80 units;
# c. Total available raw materials: 70 units):
m += xsum(L[i] * X[i] for i in I) <= 100
m += xsum(M[i] * X[i] for i in I) <= 80
m += xsum(R[i] * X[i] for i in I) <= 70
# Additional Constraints: a. Production of P1 cannot exceed 20 units. b. Production of P2 and P3 combined
# must be at least 10 units. c. At least 5 units of P4 must be produced.
m += X[0] <= 20
m += X[1] + X[2] >= 10
m += X[3] >= 5

# MIP solvers execute a Branch-&-Cut (BC) algorithm that in finite time will provide the optimal solution.
m.optimize()

# The optimized value of a decision variable X[i] is accessed using X[i].x.
optimal_productions = [X[i].x for i in I]
print(f"Status: {m.status}")
for i in I:
    print(f'Optimal Production for P{i+1}: {optimal_productions[i]}')
print(f'Total Labor: {sum(np.array(L)*np.array(optimal_productions))}')
print(f'Total Machine Time: {sum(np.array(M)*np.array(optimal_productions))}')
print(f'Total Raw Material: {sum(np.array(R)*np.array(optimal_productions))}')
print(f'Total profit:${m.objective_value}')