# Overview # 
This project solves a production optimization problem using Mixed-Integer Programming (MIP) with the mip library in Python. The objective is to maximize profit for a factory producing five products (P1, P2, P3, P4, and P5) while adhering to resource and production constraints.

# Problem Statement #
You are managing the production schedule for a factory that manufactures five different
products (P1, P2, P3, P4, and P5). Each product requires different amounts of three
resources: labor, machine time, and raw materials. The goal is to maximize the total
profit while considering the constraints related to resource availability and production
capacities. The details are as follows:
i. Products:
a. P1: Requires 2 units of labor, 3 units of machine time, 4 units of raw
materials, and generates $5 profit.
b. P2: Requires 3 units of labor, 2 units of machine time, 1 unit of raw
materials, and generates $4 profit.
c. P3: Requires 1 unit of labor, 4 units of machine time, 3 units of raw
materials, and generates $6 profit.
d. P4: Requires 4 units of labor, 1 unit of machine time, 2 units of raw
materials, and generates $7 profit.
e. P5: Requires 5 units of labor, 3 units of machine time, 2 units of raw
materials, and generates $8 profit.
ii. Resource Constraints:
a. Total available labor: 100 units
b. Total available machine time: 80 units
c. Total available raw materials: 70 units
iii. Additional Constraints:
a. Production of P1 cannot exceed 20 units.
b. Production of P2 and P3 combined must be at least 10 units.
c. At least 5 units of P4 must be produced.

∑_(i∈I)▒〖Pr⁡i*Xi〗![image](https://github.com/user-attachments/assets/88165f7e-f166-4a69-b58b-b9dd065b628f)




