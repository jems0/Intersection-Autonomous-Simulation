import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time

# Define the initial position and speed of the car
x_position = 0.0   # meters
y_position = 50.0   # meters
speed = 3.0       # meters per second

# Define initial position for car 2
x_position2 = 50.0
y_position2 = 0.0
speed2 = 5.0

# Define the time increment for each simulation step
delta_t = 0.1      # seconds

# Define the duration of the simulation
duration = 10.0    # seconds

# Create a new tkinter window
root = tk.Tk()
root.title("Car Simulation")

# Create a new matplotlib figure for the XY plane
fig = Figure(figsize=(5, 5), dpi=100)
axes = fig.add_subplot(111)
axes.set_xlim(0, 100)
axes.set_ylim(0, 100)
axes.set_xlabel('X Position (m)')
axes.set_ylabel('Y Position (m)')

# Create a new line object to represent the car's motion
line, = axes.plot([x_position], [50], '-o')

# Create a canvas to display the matplotlib figure in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a label to display the current position of the car
position_label = tk.Label(root, text="Position: ({:.1f}, {:.1f})".format(x_position, y_position))
position_label.pack()

last_update_time = time.time()

# Define a function to update the position of the car and the label
def update_position():
    global x_position, y_position, last_update_time
    current_time = time.time()
    elapsed_time = current_time - last_update_time
    last_update_time = current_time
    distance = speed * elapsed_time
    x_position += distance
    y_position += distance
    position_label.config(text="Position: ({:.1f}, {:.1f})".format(x_position, y_position))
    line.set_xdata([line.get_xdata()[-1], x_position])
    line.set_ydata([line.get_ydata()[-1], 50])
    # = [] create array to store data points

    axes.relim()
    axes.autoscale_view(True,True,True)
    canvas.draw()
    if x_position <= axes.get_xlim()[1]:
        root.after(100, update_position)
    else:
        x_position = 0.0
        y_position = 0.0
        line.set_xdata([x_position])
        line.set_ydata([y_position])
        axes.relim()
        axes.autoscale_view(True,True,True)
        canvas.draw()

# Define a function to start the simulation
def start_simulation():
    global x_position, y_position, line
    x_position = 0.0
    y_position = 0.0
    line.set_xdata([x_position])
    line.set_ydata([y_position])
    axes.relim()
    axes.autoscale_view(True,True,True)
    canvas.draw()
    update_position()

# Add a button to start the simulation
start_button = tk.Button(root, text="Start", command=start_simulation)
start_button.pack()

# Start the tkinter main loop
root.mainloop()