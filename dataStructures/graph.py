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



graph = DirectedGraph("0")
graph.addNode("1")
graph.addNode("2")
graph.addNode("3")

graph.addEdge("0", "2")
graph.addEdge("2", "0")
graph.addEdge("0", "1")
graph.addEdge("2", "3")
graph.addEdge("3", "3")
graph.addEdge("1", "2")


graph.printNodes()

graph.breadthFirst("2")
graph.depthFirst("2")
