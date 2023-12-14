import heapq
def read_file(file_name):
    map_graph = {}
    heuristic_values = {}

    with open(file_name, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        location = parts[0]
        heuristic = int(parts[1])
        adjacent = [(parts[i], int(parts[i+1]))
        for i in range(2, len(parts), 2)]

        map_graph[location] = adjacent
        heuristic_values[location] = heuristic

    return map_graph, heuristic_values

def astar_algorithm(map_graph, heuristic_values, start_point, end_point):
    open_nodes = [(0, start_point)]
    path_map = {}
    g_score_map = {location: float('inf') for location in map_graph}
    g_score_map[start_point] = 0
    while open_nodes:
        _, current_node = heapq.heappop(open_nodes)
        if current_node == end_point:
            final_path = reconstruct_path(path_map, current_node)
            return final_path
        for adjacent_node, cost in map_graph[current_node]:
            tentative_g_score = g_score_map[current_node] + cost
            if tentative_g_score < g_score_map[adjacent_node]:
                path_map[adjacent_node] = current_node
                g_score_map[adjacent_node] = tentative_g_score
                f_score_value = tentative_g_score + heuristic_values[adjacent_node]
                heapq.heappush(open_nodes, (f_score_value, adjacent_node))
    return None

def reconstruct_path(path_map, current_node):
    path_sequence = [current_node]
    while current_node in path_map:
        current_node = path_map[current_node]
        path_sequence.insert(0, current_node)
    return path_sequence

file_name = "input.txt"
map_graph, heuristic_values = read_file(file_name)
start_location = input("Enter the starting city: ")
end_location = input("Enter the destination city: ")
path_sequence = astar_algorithm(map_graph, heuristic_values, start_location, end_location)

output_file_name = "output.txt"
with open(output_file_name, 'w') as output_file:
    if path_sequence:
        total_distance_travelled = 0
        for i in range(len(path_sequence) - 1):
            current_location = path_sequence[i]
            next_location = path_sequence[i + 1]
            for adjacent_location, cost in map_graph[current_location]:
                if adjacent_location == next_location:
                    total_distance_travelled += cost
                    break
        output_file.write(f"Total distance: {total_distance_travelled} km\n")
        output_file.write("Path: " + " -> ".join(path_sequence))
    else:
        output_file.write("No path found from {} to {}".format(start_location,
end_location))
print("Output written to", output_file_name)
