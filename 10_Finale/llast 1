import random
import operator
import tkinter
import matplotlib.pyplot
import matplotlib.animation 
import matplotlib
import agentframework
import csv
import requests
import bs4
matplotlib.use('TkAgg')


#Webscrapping part 12

r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
print(td_ys)
print(td_xs)



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
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i, agents, environment, rows, cols, y, x))
#print agents    
for i in range(num_of_agents): 
    print(agents[i])   
    
    
    
#for i i range (num_of_agents)
#   agents.append(agentframework.Agent(i, agents,environment))
    random.shuffle(agents)

fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()

root = tkinter.Tk() 
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 


#ax.set_autoscale_on(False)

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(i, agents, environment, rows, cols, y, x))

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

#New function def run
#Create a canvas  


    
#animation = matplotlib.animation.FuncAnimation(fig, update, interval=1, repeat=False, frames=10)
#animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)



matplotlib.pyplot.show()

#print agents 
for i in range(num_of_agents): 
    print(agents[i])
    print("Final agents")
    
#This line sets the GUI 
tkinter.mainloop()

