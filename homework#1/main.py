#Amarilda Celhaka
#Hoemework #1
#Breadth-First-Search Algorithm

from collections import deque

graph = {'A': {'Z':75, 'S':140, 'T':118},
         'Z': {'O':71},
         'S': {'O':151,'F':99, 'R':80},
         'T': {'L':111},
         'O': {'S':151},
         'F': {'B':211},
         'R': {'P':97,'C':146},
         'L': {'M':70},
         'P': {'B':101},
         'C': {'P':138,'C':138},
         'M': {'D':75},
         'D': {'C':120}
         }



def breadth_first_search(graph):

    #node with inital state (inital-state = Arad)
    inital_state = 'A' 

    #setting goal state to B
    goal = 'B'
   
    #if initial state is equal to goal, than you reached the goal
    if inital_state == goal:
      return goal

    #defining frontier as a queue with node as the only element
    frontier = deque()
    frontier.append(inital_state)

    #defining explored as an empty set
    explored = []


   
   #enter a while loop that is always true, exit when frontier is empty or goal reached
    while True:

      #check if the frontier is empty, if yes return failure, otherwise expand the paths of the frontier
      if frontier:

        #poping the first element in the frontier
        main_path = frontier.popleft()

        #appending every explored node to the explored set
        explored.append(main_path)
       
        #main_path[-1] extraxts always the last element of the main_path
        node = main_path[-1]
    
        childs = graph[node]
        
        #traversing each leaf of the node in frontier
        for child in childs:
          #creating a path list for each traversed path
          paths = list(main_path)
          paths.append(child)
          frontier.append(paths)
          
          if child not in explored and child not in frontier:
           
            if child == goal:
              return paths
            
            frontier.append(child)

      #if frontier is empty      
      else: 
        return "Failed: Frontier is empty!"

       
print("Path from Arad to Bucharest:")
#calling the function to display the optimal path
print(breadth_first_search(graph))
    
 
