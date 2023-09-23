def is_hamiltonian(graph):
    num_vertices = len(graph)
    path = []

    def hamiltonian_path(vertex):
        path.append(vertex)

        if len(path) == num_vertices:
            if graph[path[-1]][path[0]] == 1:
                return 2
            else:
                path.pop()
                return 1

        for v in range(num_vertices):
            if is_valid(v):
                result = hamiltonian_path(v)
                if result == 1 or result == 2:
                    return result

        path.pop()

        return 0

    def is_valid(vertex):
        if vertex in path:
            return False
        if len(path) > 0 and graph[path[-1]][vertex] == 0:
            return False
        return True

    for initial_vertex in range(num_vertices):
        result = hamiltonian_path(initial_vertex)
        if result == 1:
            print("The graph contains a Hamiltonian path but not a circuit.")
            return True
        elif result == 2:
            print("The graph contains a Hamiltonian circuit.")
            return True

    print("The graph does not contain a Hamiltonian path or circuit.")
    return False

print("Enter the adjacency matrix of the graph: ")
print("Enter each row of the matrix (spaces between them ), use 0s and 1s.")

graph = []
while True:
    row = input("Enter the next row or type 'done' to finish : ")
    if row.lower() == 'done':
        break
    graph.append(list(map(int, row.split())))

is_hamiltonian(graph)
