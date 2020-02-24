#messing around with dictionaries as a way to implement graphs

graph1 = {
    'A': {'B', 'C'},
    'B': {'A', 'C', 'D', 'E'},
    'C': {'A', 'B', 'D', 'E'},
    'D': {'B', 'C', 'E', 'F'},
    'E': {'B', 'C', 'D', 'F'},
    'F': {'D', 'E'}
} 
print(graph1)
print('-----------------------------------------------')
'''
for element in graph1:
    print(element)
print('-----------------------------------------------')

for index in range (0,len(graph1)):
    print(graph1[0] + '\n\t' + graph1.items())

list1 = ['A', 'B', 'C']
sublistA = ['B', 'C']
sublistB = ['B', 'C']
sublistC = ['A']

list2 = [['B', 'C'], ['B', 'C'], ['A']]
'''
'''
for key in graph1:
    print(key)
    print(graph1[key])
'''
def print_edges(node, graph):
    for edge in graph[node]:
        print(edge)

print_edges('D',graph1)