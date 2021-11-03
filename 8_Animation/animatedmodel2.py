import random
import operator
import matplotlib.pyplot
import matplotlib.animation 
import matplotlib
import agentframework
import csv

# Install environment as a list of list
environment = []
with open('in.txt', newline='') as f:
     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
     for row in reader:
        rowlist = []
        for value in row:
            #print(value) 
            rowlist.append(value)
        environment.append(rowlist) 

# To check if it works, print enviroment 
print(environment) 

rows = len(environment)
cols = len(environment[0])
print("rows", rows)
print("cols", cols)

# To check if each of the rows have the same number columns
for rows in range(rows):
    if (len(environment[rows]) != cols):
        print("unhappy")
    # else :
    #     print("unhappy")
        
# #visualisation
# matplotlib.pyplot.imshow(environment)
# matplotlib.pyplot.show()


def distance_between(agents_row_a, agents_row_b):
     return (((agents_row_a.x - agents_row_b.x)**2) + 
     ((agents_row_a.y - agents_row_b.y)**2))**0.5

num_of_agents = 10
num_of_iterations = 10
agents = []
neighbourhood = 20

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, agents,environment))
    random.shuffle(agents)

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, agents, environment))

carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
   
#Plotting the plots behind the enviroment (visual)
    matplotlib.pyplot.imshow(environment)         
    matplotlib.pyplot.xlim(0, cols )
    matplotlib.pyplot.ylim(0, rows)
    
    print("Iteration", frame_number)
    random.shuffle(agents)
    for i in range(num_of_agents):
         #print(agents[i])
         # print(i, "before move", agents[i].x, agents[i].y)
         agents[i].move()
         # print(i, "after move", agents[i].x, agents [i].y)
         # print("store before eat", agents[i].store)
         agents[i].eat()
         # print("store after eat", agents[i].store)
         agents[i].share_with_neighbours(neighbourhood) 
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #print(agents[i][0],agents[i][1])
		
      
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)



matplotlib.pyplot.show()

#print agents 
for i in range(num_of_agents): 
    print(agents[i])
    print("Final agents")
    












