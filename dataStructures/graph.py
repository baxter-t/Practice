'''
    
'''

class Graph(object):

    def __init__(self, first):
        self.nodes = {first: []}

    def addNode(self, new):
        if self.nodes.get(new) != None:
            print("Node Already Exists")
        else:
            self.nodes[new] = []

    def addEdge(self, start, end):
        
        if self.nodes.get(start) == None or self.nodes.get(end) == None:
            print("Node not present. First call .addNode")
            return

        else :
            if end not in self.nodes[start]:
                self.nodes[start].append(end)

            if start not in self.nodes[end]:
                self.nodes[end].append(start)

    def printNodes(self):

        print(self.nodes)

    def breadthFirst(self, start):

        toVisit = []
        visited = []

        toVisit.append(start)

        while len(toVisit) > 0:
            current = toVisit.pop(0)
            visited.append(current)
            
            # For each of the outward edges check it hasnt been visitored then add
            for x in self.nodes[current]:
                if x not in visited and x not in toVisit:
                    toVisit.append(x)

            # Visit current
            print(current)

    def depthFirst(self, start):

        toVisit = []
        visited = []

        toVisit.append(start)

        while len(toVisit) > 0:
            current = toVisit.pop(0)
            visited.append(current)

            print(current)

            for x in self.nodes[current]:
                if x not in visited and x not in toVisit:
                    toVisit = [x] + toVisit

class DirectedGraph(Graph):

    def addEdge(self, start, end, mutual=False):
        
        if self.nodes.get(start) == None or self.nodes.get(end) == None:
            print("Node does not exist.")
            return

        if end not in self.nodes[start]:
            self.nodes[start].append(end)

        if mutual:
            if start not in self.nodes[end]:
                self.nodes[end].append(start)

class WeightedGraph(Graph):

    def addEdge(self, start, end, weight):

        if self.nodes.get(start) ==  None or self.nodes.get(end) ==  None:
            print("Node does not exist.")
            return
        
        if (end, weight) not in self.nodes[start]:
            self.nodes[start].append((end, weight))

        if (start, weight) not in self.nodes[end]:
            self.nodes[end].append((start, weight))

    def dijkstras(self, start):
        
        toVisit = []
        visited = []

        lengths = {}

        for x in list(self.nodes.keys()):
            lengths[x] = 10**10

        lengths[start] = 0
        
        toVisit.append((start, 0))

        while len(toVisit) > 0:

            # Sort to go to the closest node
            toVisit.sort(key = lambda x: x[1])

            # Get closest
            current = toVisit.pop(0)
            visited.append(current[0])

            toVisit = []

            for outwardEdge in self.nodes[current[0]]:
                if outwardEdge[1] + lengths[current[0]] < lengths[outwardEdge[0]]:
                    lengths[outwardEdge[0]] = outwardEdge[1] + lengths[current[0]]

                if outwardEdge[0] not in visited:
                    toVisit.append(outwardEdge)
        return lengths 

graph = WeightedGraph("1")
graph.addNode("2")
graph.addNode("3")
graph.addNode("4")
graph.addNode("5")
graph.addNode("6")

graph.addEdge("1", "2", 7)
graph.addEdge("1", "3", 9)
graph.addEdge("1", "6", 14)
graph.addEdge("2", "3", 10)
graph.addEdge("3", "4", 11)
graph.addEdge("3", "6", 2)
graph.addEdge("6", "5", 9)
graph.addEdge("5", "4", 6)

#graph.printNodes()

print(graph.dijkstras("1"))
