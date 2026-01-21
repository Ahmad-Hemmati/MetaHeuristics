# UiB INF273-Meta-Heuristics Truck-and-drone utils
This Repo is dedicated to the function utils needed for the project of the course.

# Requirements
- numpy, typing, collections

## Description of important classes and functions
1) Function **read_data**: Takes the string adress of input data file and gets the data about number of customers, drone flight limit, and travel time matrices for the truck and the drones. The depot is fixed as the node 0, and the number of drones as 2.

2) Function **parse_solution**: Converts the solution in string format to four parts: the truck route, the customers served by the drone in the order of the truck route (with -1 denoting new drone usage), the launch indices of the drones starting from 1 (with -1 denoting new drone usage) in increasing order, the landing (reconvene) indices of the drones starting from 1 (with -1 denoting new drone usage) in increasing order

3) class **SolutionRunner**: Encodes the parsed solution and input data to be used for the following sub-calsses below:

4) Class **SolutionRunner.feasibility**: Used for checking the feasibility of the parsed solution based on calling 4 member functions: is_truck_route_feasible (checks whether the truck route has valid entries only), is_complete_solution (checking whether the truck and the available drones together serve all customers exactly once), are_parts_consistent (checks whether the length of the parts 2, 3, and 4 and the drone separators match) and the lauches and landing indices are consistent, are_all_drone_trips_feasible (checks whether the for each drone, the flights are feasible with respect to flight limit and launch->land->launch->land...)

5) Class **SolutionRunner.calculate_total_waiting_time**: Used for calculating the total objective, which is equal to the sum of arrival times at the customers by either the truck, or a drone, divided by a 100. This arrival time is based on the departure time of the trucks and the drones, which might involve either the truck waiting for some drones or some drones waiting for the truck. This calculation is performed within the function, and a detailed log is also provided.
