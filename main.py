import random
from draw_graph import draw_graph
from dijkstra_algorithm import dijkstra_algorithm
import time
import matplotlib.pyplot as plt


# size = 10
# my_matrix = [0] * size
# for i in range(size):
#     my_matrix[i] = [0] * size
#
# my_edges = []
# my_weights = []
# for i in range(size):
#     for j in range(i, size):
#         my_matrix[i][j] = my_matrix[j][i] = random.randint(0, 3)
#         if my_matrix[i][j] != 0:
#             my_edges.append((i, j))
#             my_weights.append(my_matrix[i][j])

my_edges = []
my_weights = []
my_graph = [[0, 3, 6, 1, 0, 0],
            [3, 0, 0, 0, 8, 5],
            [6, 0, 0, 4, 4, 0],
            [1, 0, 4, 0, 12, 0],
            [0, 8, 4, 12, 0, 3],
            [0, 5, 0, 0, 3, 0]]
for i in range(len(my_graph)):
    for j in range(0, i):
        if my_graph[i][j] != 0:
            my_edges.append((i, j))
            my_weights.append(my_graph[i][j])
start_node = 0
end_node = 4
length, path = dijkstra_algorithm(my_graph, start_node, end_node)

print(f'Длина пути от {start_node} до {end_node} равна {length}\n путь выглядит так: {path}')
draw_graph(len(my_graph), my_edges, my_weights, "kk")


size_arr = []
avg_time = []
for M in range(5, 25, 2):
    size_arr.append(M)
    times = []
    for i in range(100):

        Matrix = [0] * (M**2)
        edges = []
        weights = []
        for i in range(M**2):
            Matrix[i] = [0] * (M**2)

        # for i in range(M**2):
            # print(Matrix[i])
        for V in range(M**2):
            R = V // M
            C = V % M
            if C < M - 1:
                Matrix[V][V + 1] = Matrix[V + 1][V] = 1
                edges.append((V, V + 1))
                weights.append(1)
                # edges.append((V + 1, V))
                # weights.append(1)
            if R < M - 1:
                Matrix[V][V+M] = Matrix[V+M][V] = 1
                edges.append((V, V + M))
                weights.append(1)
                # edges.append((V + M, V))
                # weights.append(1)

        # if (M == 5):
        #     print("------------------------")
        #     for i in range(M**2):
        #         print(Matrix[i])
        #     draw_graph(M**2, edges, weights, layout="grid")

        start_node = random.randint(0, M)
        end_node = random.randint(0, M)
        start_time = time.time()
        length, path = dijkstra_algorithm(Matrix, start_node, end_node)
        end_time = time.time()
        times.append(end_time - start_time)
        print(f'Длина пути от {start_node} до {end_node} равна {length}\n путь выглядит так: {path}')
    avg_time.append(sum(times)/len(times))

plt.plot(size_arr, avg_time)
plt.show()