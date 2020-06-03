from graph import Graph

graph_1 = Graph()

graph_1.insert_vertex('A')
graph_1.insert_vertex('B')
c = graph_1.insert_vertex('C')
d = graph_1.insert_vertex('D')

graph_1.vertex_count()

graph_1.insert_edge(graph_1.insert_vertex('A'), graph_1.insert_vertex('B'))
graph_1.insert_edge(a, c)
graph_1.insert_edge(a, d)
graph_1.insert_edge(d, b)
graph_1.insert_edge(d, c)

for i in graph_1.vertices():
    print(i)

for i in graph_1.edges():
    print(i)