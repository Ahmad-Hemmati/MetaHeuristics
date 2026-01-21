![Truck-and-drone routing](https://github.com/Ahmad-Hemmati/MetaHeuristics/blob/main/Truck-and-drones%20challenge/toy_example_solution.jpg)


# UiB INF273-Meta-Heuristics Truck-and-Drone utils
This Repo is dedicated to the function utils needed for the project of the course.

# Requirements
- numpy, typing, collections

## Description of important classes and functions
1) Function **read_data**: Takes the string adress of input data file and gets the data about number of customers, drone flight limit, and travel time matrices for the truck and the drones. The depot is fixed as the node 0, and the number of drones as 2.

2) Function **parse_solution**: Converts the solution in string format to four parts: the truck route, the customers served by the drone in the order of the truck route (with -1 denoting new drone usage), the launch indices of the drones starting from 1 (with -1 denoting new drone usage) in increasing order, the landing (reconvene) indices of the drones starting from 1 (with -1 denoting new drone usage) in increasing order

3) class **SolutionRunner**: Encodes the parsed solution and input data to be used for the following sub-calsses below:

4) Class **SolutionRunner.feasibility**: Used for checking the feasibility of the parsed solution based on calling 4 member functions: is_truck_route_feasible (checks whether the truck route has valid entries only), is_complete_solution (checking whether the truck and the available drones together serve all customers exactly once), are_parts_consistent (checks whether the length of the parts 2, 3, and 4 and the drone separators match) and the lauches and landing indices are consistent, are_all_drone_trips_feasible (checks whether the for each drone, the flights are feasible with respect to flight limit and launch->land->launch->land...)

5) Class **SolutionRunner.calculate_total_waiting_time**: Used for calculating the total objective, which is equal to the sum of arrival times at the customers by either the truck, or a drone, divided by a 100. This arrival time is based on the departure time of the trucks and the drones, which might involve either the truck waiting for some drones or some drones waiting for the truck. This calculation is performed within the function, and a detailed log is also provided.


A toy example instance with the example feasible solution illustrated above is used in main.py now. Several other instances are also provided with which you will be working on in the course. The format of the solution that is used in this case, and will be expected for the solutions that you submit for evaluation is explained below:

**Required solution format for submission**

The solution must be submitted as a comma-separated sequence of numbers, using values from -1 to the number of customers.
The full sequence is divided into four parts, separated by the character "|" .
--------------------------------------------------
Part 1: Truck route
A subset of numbers from 0 to the number of customers.
Represents the order in which customers are visited by the truck.
The route must start and end at the depot (0).
--------------------------------------------------
Part 2: Drone deliveries
Contains the customers not served by the truck.
Customers are listed in the order they are served by each drone, following the truck route.
Each drone’s sequence is separated by -1.
This part contains one "-1".
--------------------------------------------------
Part 3: Drone launch sites
Specifies where each drone is launched.
Uses truck route indices, counted from 1, in increasing order.
Each index refers to a position in the truck route from Part 1.
The launch sequence for each drone is separated by -1.
This part contains one "-1".
--------------------------------------------------
Part 4: Drone landing sites
Similar to Part 3, but specifies where each drone lands.
Uses truck route indices, counted from 1, in increasing order.
Each drone’s landing sequence is separated by -1.
This part contains one "-1".
