import igraph as ig
import matplotlib.pyplot as plt


def draw_graph(size: int, edges: list, weights: list):
    My_G = ig.Graph()
    My_G.add_vertices(size)
    My_G.add_edges(edges)
    My_G.es["weight"] = weights
    My_G.vs["label"] = range(size)

    #Построение графа
    fig, ax = plt.subplots(figsize=(11, 11))  # создание окна для рисования
    ig.plot(My_G,  # отрисовка графа
                target=ax,
                layout="grid",  # print nodes in a kawada kiwai layout
                vertex_size=50,  # размер вершины
                vertex_color="purple",  # цвет вершин
                vertex_frame_width=4.0,  #
                vertex_frame_color="white",  # цвет фона
                vertex_label=My_G.vs["label"],  # добавление подписей
                vertex_label_size=12.0,  # размер подписей вершин
                edge_label=My_G.es["weight"]  # добавление ребер
                )
    plt.show()
