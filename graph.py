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
            self.array[destination].insert_at_tail(source)

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
a.add_edge(0, 1)
a.add_edge(0, 2)
a.add_edge(0, 3)
#
a.add_edge(3, 5)
a.add_edge(5, 4)
# a.add_edge(1,4)
a.add_edge(2,4)
# a.add_edge(4,1)
a.print_graph()


# print(a.array[0].get_head().data)


def bfs(graph, source):
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
    return result


vis = set()
r = []


def helper(graph, source):
    r.append(source)
    if source not in vis:
        vis.add(source)
        temp = graph.array[source].head
        while temp:
            dfs_traversal(graph, temp.data)
            temp = temp.next_element


def dfs_traversal(graph, source):
    helper(graph, source)
    result = ''
    for item in r:
        result += str(item)
    return result


def detect_cycle(graph):
    visit = []
    for i in range(graph.vertices):
        temp = graph.array[i].get_head()
        while temp is not None:
            if len(visit) > 0 and temp.data < visit[-1]:
                return True
            if temp.data not in visit:
                visit.append(temp.data)
            temp = temp.next_element
    return False


def find_mother_vertex(g):
    res = []
    for i in range(g.vertices):
        result = bfs(g, i)
        res.append(result)
    return (max(res, key=len)[0])


def num_edges(g):
    # Complexity : O(V + E)
    a = 0
    for i in range(g.vertices):
        temp = g.array[i].get_head()
        while temp is not None:
            a += 1
            temp = temp.next_element
    return a


def check_path(g, source, destination):
    # Complexity O(V + E)
    res = bfs(g, source)
    if str(destination) in res:
        return True
    return False


def is_tree(g):
    for i in range(g.vertices):
        temp = g.array[i].get_head()
        if temp.next_element is None:
            return False
    if detect_cycle(g):
        return False
    return True

def remove_edge(graph,source, dest):
    temp = graph.array[source]
    temp.delete_value(dest)
    graph.print_graph()
    return graph

remove_edge(a,3,5)