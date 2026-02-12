
import math
import numpy as np


filenames = "F10.txt"

flight_range = [4600]

filename = filenames[i]
n_drones = 2 #instance file
speed_ratio = 1.5 # instance file
flight_range = flight_ranges[i]
drone_capacity = 1 # instance file
depot_index=0 # instance file

example_solution_str = ("0,0,|,-1,|,-1,|,-1")
 
# Problem instance data  
# ---------------------------------------------------------------------------
def parse_solution(values: str):
    """
    values: string like "1,2,3,|,10,20,|,5,6,|,100,200"
            or "1,2,3|10,20|5,6|100,200"
    returns: {"part1": [...], "part2": [...], "part3": [...], "part4": [...]}
    """

    if not isinstance(values, str):
        raise TypeError(f"Expected string from Go, got {type(values)}")

    s = values.strip()

    # normalize around pipes: ",|," or ",|" or "|," -> "|"
    s = s.replace(",|,", "|").replace(",|", "|").replace("|,", "|")

    parts = s.split("|")
    if len(parts) != 4:
        raise ValueError(f"Expected 4 parts separated by '|', got {len(parts)} parts: {parts}")

    def parse_int_list(part: str):
        # split by comma, ignore empty chunks (can happen after normalization)
        chunks = [c.strip() for c in part.split(",") if c.strip() != ""]
        return [int(c) for c in chunks]

    return {
        "part1": parse_int_list(parts[0]),
        "part2": parse_int_list(parts[1]),
        "part3": parse_int_list(parts[2]),
        "part4": parse_int_list(parts[3]),
    }
    
    
    
    def read_coordinates(filename: str):
        """
        Read coordinates from a file formatted like TRP-S50-R1.txt,
        where each line contains two integers:  X<TAB>Y
    
        Returns:
            List[Tuple[int, int]]
        """
        coords = []
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # skip empty lines
                
                parts = line.split()
                if len(parts) != 2:
                    raise ValueError(f"Invalid line (expected 2 numbers): {line}")
    
                x, y = map(int, parts)
                coords.append((x, y))
        print(coords)
        return coords
    
    
    def create_target_solution_instance():
        """Create problem instance that naturally leads to the target solution"""
        coords = read_coordinates(filename)
        n_nodes = len(coords) -1 # first and last node is the depot
        n_customers = n_nodes -1
        distance_matrix = np.zeros((n_nodes, n_nodes))
    
        for i in range(n_nodes):
            for j in range(n_nodes):
                dx = coords[i][0] - coords[j][0]
                dy = coords[i][1] - coords[j][1]
                distance_matrix[i][j] = math.sqrt(dx**2 + dy**2)
    
        # print("Euclidean Distance Matrix (11 nodes):")
        # print(np.array2string(distance_matrix, formatter={'float_kind': lambda x: "%.2f" % x}))
    
        T = np.floor(distance_matrix)  #truck_times
        drone_times=np.floor(T / speed_ratio) *100
        truck_times=T*100
    
        return n_nodes, n_customers, n_drones, truck_times, drone_times, flight_range,  drone_capacity
    
    
    n_nodes, n_customers, n_drones, truck_times, drone_times, flight_range, drone_capacity = create_target_solution_instance()    
    
    #"""
    with open(filename[:-4]+"_.txt", "w") as f:
        f.write("# Number of customers\n")
        f.write(str(n_nodes-1)+"\n")
        f.write("# Drone flight limit\n")
        f.write(str(flight_range)+"\n")    
        f.write("# Travel time matrix for the truck\n")
        for row in truck_times:
            f.write("\t".join(map(str, row)) + "\n")
        f.write("# Travel time matrix for the drones\n")
        for row in drone_times:
            f.write("\t".join(map(str, row)) + "\n")
        f.write("#\n")
    #"""
    
