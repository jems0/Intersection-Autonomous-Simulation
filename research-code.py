import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import time

# Define the initial position and speed of the cars
car1_x_position1 = 0.0   # meters
car1_y_position1 = 50.0   # meters
car1_speed = 3.0       # meters per second

car2_x_position2 = 0.0   # meters
car2_y_position2 = 30.0   # meters
car2_speed = 2.0       # meters per second

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

# Create a label to display the current position of the first car
position_label1 = tk.Label(root, text="Car 1 Position: ({:.1f}, {:.1f})".format(car1_x_position1, car1_y_position1))
position_label1.pack()

# Create a label to display the current position of the second car
position_label2 = tk.Label(root, text="Car 2 Position: ({:.1f}, {:.1f})".format(car2_x_position2, car2_y_position2))
position_label2.pack()

# Create a new line object to represent the first car's motion
car1_line, = axes.plot([car1_x_position1], [car1_y_position1], '-o', label='Car 1')

# Create a new line object to represent the second car's motion
car2_line, = axes.plot([car2_x_position2], [car2_y_position2], '-o', label='Car 2')

axes.legend()

# Create a canvas to display the matplotlib figure in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a label to display the current position of the cars
position_label = tk.Label(root, text="Car 1 Position: ({:.1f}, {:.1f})\nCar 2 Position: ({:.1f}, {:.1f})".format(car1_x_position1, car1_y_position1, car2_x_position2, car2_y_position2))
position_label.pack()

last_update_time = time.time()

# Define a function to update the position of the cars and the labels
def update_position():
    global car1_x_position1, car1_y_position1, car2_x_position2, car2_y_position2, last_update_time

    # Update the position of the first car
    current_time = time.time()
    elapsed_time = current_time - last_update_time
    last_update_time = current_time
    distance = car1_speed * elapsed_time
    car1_x_position1 += 0
    car1_y_position1 += -5
    position_label1.config(text="Car 1 Position: ({:.1f}, {:.1f})".format(car1_x_position1, car1_y_position1))
    car1_line.set_xdata([car1_x_position1])
    car1_line.set_ydata([car1_y_position1])

    # Update the position of the second car
    car2_x_position2 += car2_speed * elapsed_time
    car2_y_position2 += car2_speed * elapsed_time
    position_label2.config(text="Car 2 Position: ({:.1f}, {:.1f})".format(car2_x_position2, car2_y_position2))
    car2_line.set_xdata([car2_x_position2])
    car2_line.set_ydata([car2_y_position2])

    # Redraw the canvas
    axes.relim()
    axes.autoscale_view(True,True,True)
    canvas.draw()

    # Check if the first car has reached the end of the road
    if car1_x_position1 <= axes.get_xlim()[1]:
        root.after(100, update_position)

    # If the first car has reached the end of the road, reset its position
    else:
        car1_x_position1 = 0.0
        car1_y_position1 = 50.0
        car1_line.set_xdata([car1_x_position1])
        car1_line.set_ydata([car1_y_position1])
        position_label1.config(text="Car 1 Position: ({:.1f}, {:.1f})".format(car1_x_position1, car1_y_position1))
        axes.relim()
        axes.autoscale_view(True,True,True)
        canvas.draw()

    # Check if the second car has reached the end of the road
if car2_x_position2 <= axes.get_xlim()[1]:
    root.after(100, update_position)

# If the second car has reached the end of the road, reset its position
elif car1_x_position1 <= axes.get_xlim()[1]:
    car2_x_position2 = 0.0
    car2_y_position2 = 30.0
    car2_line.set_xdata([car2_x_position2])
    car2_line.set_ydata([car2_y_position2])
    position_label2.config(text="Car 2 Position: ({:.1f}, {:.1f})".format(car2_x_position2, car2_y_position2))
    axes.relim()
    axes.autoscale_view(True,True,True)
    canvas.draw()


# Define a function to start the simulation
def start_simulation():
    global x_position1, y_position1, x_position2, y_position2, line1, line2

    # Reset the positions of the cars
    x_position1 = 0.0
    y_position1 = 50.0
    x_position2 = 0.0
    y_position2 = 25.0
    # Update the lines to represent the new positions
    car1_line.set_xdata([car1_x_position1])
    car1_line.set_ydata([car1_y_position1])
    car2_line.set_xdata([car2_x_position2])
    car2_line.set_ydata([car2_y_position2])
    axes.relim()
    axes.autoscale_view(True,True,True)
    canvas.draw()
    update_position()

#start_button = tk.Button(root, text='Start', command=start_simulation)
#start_button.pack()
root.mainloop()
