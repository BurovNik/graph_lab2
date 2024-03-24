import sys

def dijkstra_algorithm(graph: list, start_node: int, end_node: int):
    unvisited_node = [node for node in range(len(graph))]
    shortest_path = {node : sys.maxsize for node in range(len(graph))}
    # заполнить значения для всех вершин бесконечностью, кроме первой
    previous_nodes = {node : [] for node in range(len(graph))}
    shortest_path[start_node] = 0
    previous_nodes[start_node] = [start_node]

    # начать перебор пока есть не посещенные вершины
    while unvisited_node:
        # выбрать наименьшую не посещенную вершину
        current_min_node = None
        for node in unvisited_node:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
        # если минимальная вершина - та, к которой нужно прийти - заканчиваем перебор
        if current_min_node == end_node:
            break
        # проверить всех ее соседей
        for i in range(len(graph)):
            if graph[current_min_node][i] != 0:
                # обновить веса и пути, если это нужно
                if shortest_path[i] >  shortest_path[current_min_node] + graph[current_min_node][i]:
                    shortest_path[i] = shortest_path[current_min_node] + graph[current_min_node][i]
                    previous_nodes[i] = previous_nodes[current_min_node] + [i]

        # удаляем вершину из списка не посещенных
        unvisited_node.remove(current_min_node)
    return shortest_path[end_node], previous_nodes[end_node]




