from Graph import Graph as Graph
from ASearch import ASearch as ASearch

graph = Graph()

a_search = ASearch(graph.bucharest)
a_search.search(graph.arad)
