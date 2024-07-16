# Overview # 
This project solves a production optimization problem using Mixed-Integer Programming (MIP) with the mip library in Python. The objective is to maximize profit for a factory producing five products (P1, P2, P3, P4, and P5) while adhering to resource and production constraints. 

# Problem Statement
The factory produces five products: P1, P2, P3, P4, and P5. Each product requires specific amounts of labor, machine time, and raw materials, and generates a certain profit. The goal is to determine the optimal production quantities for each product to maximize total profit, given the constraints on resource availability and production capacities.

Product Details
- P1: Requires 2 units of labor, 3 units of machine time, 4 units of raw materials, and generates $5 profit.
- P2: Requires 3 units of labor, 2 units of machine time, 1 unit of raw materials, and generates $4 profit.
- P3: Requires 1 unit of labor, 4 units of machine time, 3 units of raw materials, and generates $6 profit.
- P4: Requires 4 units of labor, 1 unit of machine time, 2 units of raw materials, and generates $7 profit.
- P5: Requires 5 units of labor, 3 units of machine time, 2 units of raw materials, and generates $8 profit.

Resource Constraints
- Total available labor: 100 units
- Total available machine time: 80 units
- Total available raw materials: 70 units

Additional Constraints
- Production of P1 cannot exceed 20 units.
- Production of P2 and P3 combined must be at least 10 units.
- At least 5 units of P4 must be produced.

# Results
The code is well documented in a python file and the optimal solution was found using CBC MILP Solver. The results are presented as follows:
- “Status: OptimizationStatus.OPTIMAL
- Optimal Production for P1: 0.0
- Optimal Production for P2: 0.0
- Optimal Production for P3: 10.0
- Optimal Production for P4: 10.0
- Optimal Production for P5: 10.0
- Total Labor: 100.0
- Total Machine Time: 80.0
- Total Raw Material: 70.0
- Total profit: $210.0”







