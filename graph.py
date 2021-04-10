from vertex import Vertex

class Graph:
    def __init__(self, directed=False):
        self.directed = directed 
        self.graph_dict = {}
    
    def add_vertex(self, vertex):
        print("Adding {}".format(vertex.value))
        self.graph_dict[vertex.value] = vertex 
    
    def add_edge(self, from_vertex, to_vertex, weight=0):
        self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)

        if not self.directed:
            self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}
        while len(start) > 0:
            current_vertex = start.pop()
            seen[current_vertex] = True 
            print(current_vertex)

            if current_vertex == end_vertex:
                return True 
            else:
                vertex = self.graph_dict[current_vertex]
                next_vertices = vertex.get_edges()
                next_vertices = [i for i in next_vertices if not i in seen]
                start.extend(next_vertices)

        return False

    
    def traverse(self, start_vertex, end_vertex):
        counts = []
        lst = []
        for i, j in self.graph_dict.items():
            
            
            count = 0 
            
            temp = [start_vertex.value]

            if len(counts) > 0:
                i = lst.pop()
            
            if len(counts) == 0:
                if i == start_vertex.value:    
                    for j in start_vertex.edges.keys():
                        lst.append(j)                     #First element, to make sure we start off at the right index 
                    for j in start_vertex.edges.keys():
                        temp.append(j)
                        if j == end_vertex.value:
                            count += start_vertex.edges[j]
                            break
                            
                        else:
                            count += start_vertex.edges[j]
                            continue 
                    counts.append({count:temp})
                        
            else:
                try:
                    temp.append(i)
                    for j in self.graph_dict[i].edges.keys():
                        lst.append(j)
                        temp.append(j)
                        if  j == end_vertex.value:
                            count += self.graph_dict[i].edges[j]
                            break
                            
                        else:
                            count += start_vertex.edges[j]
                            continue 
                    counts.append({count:temp})
                except KeyError:
                    break
                #i = lst.pop()
        sorted_nums = []
        for i in counts:
            for j in i.keys():
                sorted_nums.append(j)
        
        for i in counts:
            for j in i.keys():
                if j == sorted_nums[0]:
                    return i[j]
                else:
                    continue 
    
        
        
                    




railway = Graph()

one = Vertex('1')
two = Vertex('2')
three = Vertex('3')

railway.add_vertex(one)
railway.add_vertex(two)
railway.add_vertex(three)
railway.add_vertex(Vertex('4'))

railway.add_edge(one, two, 2)
railway.add_edge(two, three, 4)
railway.add_edge(three, one, 1)
railway.add_edge(three, two, 5)
railway.add_edge(one, three, 6)

test1 = railway.find_path('1', '2')
test2 = railway.find_path('2', '3')
test3 = railway.find_path('3', '1')
test4 = railway.find_path('4', '2')

print("An edge from 1 to 2 ")
print(test1)
print("An edge from 2 to 3")
print(test2)
print("An edge form 3 to 1")
print(test3)
print(test4)
print(railway.traverse(one, two))