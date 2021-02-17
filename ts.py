visited_vertex = [False,False,False,False,False,False,False]
graph_matrix = [[ 0,12,	10,	-1,	-1,	-1,	12],
[12,	0,	8,	12,	-1,	-1,	-1],
[10,	8,	0,	11,	3,	-1,	9],
[-1,	12,	11,	0,	11,	10,	-1],
[-1,	-1,	3,	11,	0,	6,	7],
[-1,	-1,	-1,	10,	6,	0,	9],
[12,	-1,	9,	-1,	7,	9,	0 ]]

graph_matrix = [[ 0,12,	10,	-1,	-1,	-1,	12],
[12,	0,	8,	12,	-1,	-1,	-1],
[10,	8,	0,	11,	3,	-1,	9],
[-1,	12,	11,	0,	11,	10,	-1],
[-1,	-1,	3,	11,	0,	6,	7],
[-1,	-1,	-1,	10,	6,	0,	9],
[12,	-1,	9,	-1,	7,	9,	0 ]]

path = []
shortest_path = None  #{path: [],total_dist: int }
count = 0

def adjacent_list(vertex: int):
    adj_list = []
    for i in range(0,graph_matrix.__len__()):
        if graph_matrix[vertex][i] != 0 and graph_matrix[vertex][i] != -1:
            adj_list.append(i)
    return adj_list

def check_if_all_visited():
    ans = True
    for bool in visited_vertex:
        ans = ans and bool
    return ans

def find_shortest_path(input_graph_matrix):
    global graph_matrix
    graph_matrix = input_graph_matrix

    

def cal_path(sv,cv,total_dist):
  global path
  global shortest_path
  global graph_matrix
  global visited_vertex
  global count

  count = count + 1 
  print((sv,cv,total_dist))
#   print(visited_vertex)

  if check_if_all_visited() == True:
        # print(visited_vertex) 
        # visited_vertex = [True,False,False,False,False,False,False]  
        if graph_matrix[sv][cv] < 0:
                return
        else: 
            # path.append(sv)	
            	
            if shortest_path == None:
                shortest_path = {'path': path.copy(), 'total_dist': total_dist + graph_matrix[cv][sv] }
                print(path)
                print(shortest_path)
            elif shortest_path['total_dist'] < total_dist + graph_matrix[cv][sv]:
                return
            elif shortest_path['total_dist'] > total_dist + graph_matrix[cv][sv]: 
                shortest_path = {'path': path.copy(), 'total_dist': total_dist + graph_matrix[cv][sv] }
            
            print(path)
            print(shortest_path)

            # total_dist = total_dist - graph_matrix[cv][sv]    
            # path = []
            return shortest_path['path']

#   if graph_matrix[sv][cv] < 0 or graph_matrix[sv][cv] > total_dist:
#       graph_matrix[sv][cv] = total_dist
		
#   if graph_matrix[sv][cv] < total_dist:
#       return   	  

  for v in adjacent_list(cv):										  
    if visited_vertex[v] == True:
        continue 					
    path.append(v)
    visited_vertex[v] = True
    cal_path(sv,v,total_dist + graph_matrix[cv][v])
    visited_vertex[v] = False
    # total_dist = total_dist - graph_matrix[cv][sv]
    # path.remove(v)
    if path.__len__() != 0:
        path.pop()
					
   					
visited_vertex[0] = True
# print(graph_matrix)					
cal_path(0,0,0)
# print(graph_matrix)
print(shortest_path)
# print(path)
print("count = %d" % (count))
