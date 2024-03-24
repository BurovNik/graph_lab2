import random
from draw_graph import draw_graph
from dijkstra_algorithm import dijkstra_algorithm
import time
import matplotlib.pyplot as plt


print("Hello World")

size = 10
arr = []
for i in range(size):
    arr.append(random.randint(0, 10))
print(arr)


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

        start_node = 0
        end_node = 11
        start_time = time.time()
        length, path = dijkstra_algorithm(Matrix, start_node, end_node)
        end_time = time.time()
        times.append(end_time - start_time)
        print(f'Длина пути от {start_node} до {end_node} равна {length}\n путь выглядит так: {path}')
    avg_time.append(sum(times)/len(times))

plt.plot(size_arr, avg_time)
plt.show()