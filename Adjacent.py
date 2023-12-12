class Adjacent:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost
        self.road_distance = node.target_distance + self.cost