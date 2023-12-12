# Romania Route Solver with A* Search 🚀

This implementation solves the Arad to Bucharest route problem using the A* Search algorithm. The goal is to find the most efficient path considering both the road distance and the straight-line distance to Bucharest.

## A* Search Algorithm

The A* Search algorithm is an informed search algorithm that uses heuristics to guide the search. In this case, the algorithm combines the road distance with the straight-line distance to Bucharest as the heuristic. The road distance is the actual distance traveled, and the straight-line distance is a heuristic estimation to prioritize nodes.

![Arad to Bucharest map](https://github.com/filipelimavaz/a--search-algorithm/blob/main/map.png)

## Classes

### 1. `ASearch`

The `ASearch` class represents the A* Search algorithm.

- **Attributes:**
  - `target`: The destination node (Bucharest).
  - `find`: Flag indicating whether the destination has been found.

- **Methods:**
  - `search(self, current_city)`: Executes the A* Search from a given city.

### 2. `OrderedVector`

The `OrderedVector` class implements an ordered vector used in the A* Search.

- **Attributes:**
  - `capacity`: Maximum capacity of the vector.
  - `last_position`: Index of the last element in the vector.
  - `valor_list`: List storing the elements.

- **Methods:**
  - `__init__(self, capacity)`: Initializes the ordered vector.
  - `print(self)`: Prints the elements in the vector.
  - `add(self, adjacent)`: Adds an adjacent node to the vector while maintaining order.

### 3. `Node`

The `Node` class represents a node in the graph, which is a city in Romania.

- **Attributes:**
  - `city_name`: The name of the city.
  - `visited`: Flag indicating whether the node has been visited during the search.
  - `target_distance`: Distance to the destination (Bucharest).
  - `adjacent_cities`: List of adjacent cities.

- **Methods:**
  - `add_adjacent_city(self, adjacent)`: Adds an adjacent city to the list.
  - `print_adjacent_cities(self)`: Prints the adjacent cities.

### 4. `Graph`

The `Graph` class defines the graph with nodes/cities and their connections.

### 5. `Adjacent`

The `Adjacent` class represents an edge between two nodes, indicating the cost of traversal.

- **Attributes:**
  - `node`: The adjacent node.
  - `cost`: The cost of traversing to the adjacent node.
  - `road_distance`: The total distance (road distance + heuristic) to the adjacent node.
