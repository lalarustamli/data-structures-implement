from linklist import LinkedList


class Graph:
    def __init__(self, vertices):
        # Total n of vertices:
        self.vertices = vertices
        # A list will contain linked lists for adjacency matrix
        self.array = []
        # Create a linked list for each vertex
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        # Complexity: O (1)
        # Add edge for directed graph
        if source < self.vertices and destination < self.vertices:
            self.array[source].insert_at_tail(destination)
            # for undirected graph:
            #self.array[destination].insert_at_head(source)

    def print_graph(self):
        print(" Adjacency list of directed graph\n")
        print(" VERTICES : ", self.vertices)
        for i in range(self.vertices):
            print(" | ", i, end=" | => ")
            temp = self.array[i].get_head()
            while temp is not None:
                print("[", temp.data, end=" ] -> ")
                temp = temp.next_element
            print(" None ")


a = Graph(6)
a.add_edge(0,1)
a.add_edge(1,2)
a.add_edge(2,0)
#
a.add_edge(3,0)
a.add_edge(3,1)
# a.add_edge(1,4)
# a.add_edge(2,5)
# a.add_edge(4,1)
a.print_graph()
# print(a.array[0].get_head().data)


def bfs(graph,source):
    visited = []
    que = []
    visited.append(source)
    que.append(source)
    result = ""
    while que:
        elem = que.pop(0)
        temp = graph.array[elem].head
        result += str(elem)
        while temp:
            if temp.data not in visited:
                visited.append(temp.data)
                que.append(temp.data)
            temp = temp.next_element
    # if len(result) == graph.vertices:
    #     print("MOTHER!")
    # print(result)
    return result


vis = set()
r = []
def dfs(graph,source):
    r.append(source)
    if source not in vis:
        vis.add(source)
        temp = graph.array[source].head
        while temp:
            dfs(graph,temp.data)
            temp=temp.next_element
        return
    result = ''
    for item in r:
        result += str(item)
    print(result)



# dfs(a,0)

# bfs(a,1)

def detect_cycle(graph):
    visit = []
    for i in range(graph.vertices):
        temp = graph.array[i].get_head()
        while temp is not None:
            if temp.data not in visit:
                visit.append(temp.data)
            if temp.data<visit[-1]:
                print("LOOP")
            temp = temp.next_element
# detect_cycle(a)

def find_mother_vertex(g):
    res = []
    for i in range(g.vertices):
        result = bfs(g,i)
        res.append(result)
    return(max(res, key=len)[0])
print(find_mother_vertex(a))
# bfs(a,2)