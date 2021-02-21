from algorithms.bubbleSort import bubble_sort
from algorithms.mergeSort import merge_sort
from algorithms.selectionSort import selection_sort

from tkinter import *
from tkinter import ttk

import threading

# Random to create array
import random

# Import colors from colors.py
from colors import *

# Create basic app window
window = Tk()
window.title("Sorting Algorithms Visualizer")
window.maxsize(1000, 700)
window.config(bg = WHITE)

algorithm_name = StringVar()
# Algorithm List to select from
algo_list = ["Bubble Sort", "Merge Sort", "Selection Sort"]

speed_name = StringVar()
# Speed list for selecting sorting speed
speed_list = ["Fast", "Medium", "Slow"]

# Empty list to be filled with random values when generating new array
data = []

stop_list = ["Stop"]

# This function will draw randomly generated list data[] on the canvas as vertical bars
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[1])

    window.update_idletasks()

# This function will generate array with random values every time generate button clicked
def generate():
    global data

    data = []

    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)
    
    drawData(data, [BLUE for x in range (len(data))])

# This function will set sorting speed
def set_speed():
    if speed_menu.get() == "Slow":
        return 0.3
    elif speed_name.get() == "Medium":
        return 0.1
    else:
        return 0.001

# This function will trigger selected algorithm and start sorting
def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == "Bubble Sort":
        bubble_sort(data, drawData, timeTick)
    elif algo_menu.get() == "Merge Sort":
        merge_sort(data, 0, len(data)-1, drawData, timeTick)
    elif algo_menu.get() == "Selection Sort":
        selection_sort(data, drawData, timeTick)

# This function will strop current algorithm sort
def stop():
    pass

### User Interface Here ###

UI_frame = Frame(window, width = 900, height = 300, bg = WHITE)
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

# Dropdown to select sorting algorithm
l1 = Label(UI_frame, text = "Algorithm: ", bg = WHITE)
l1.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
algo_menu = ttk.Combobox(UI_frame, textvariable = algorithm_name, values = algo_list)
algo_menu.grid(row = 0, column = 1, padx = 5, pady = 5)
algo_menu.current(0)

# Dropdown to select sorting speed
l2 = Label(UI_frame, text = "Speed: ", bg = WHITE)
l2.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)
speed_menu = ttk.Combobox(UI_frame, textvariable = speed_list, values = speed_list)
speed_menu.grid(row = 1, column = 1, padx = 5, pady = 5)
speed_menu.current(0)

# Sort Button
b1 = Button(UI_frame, text = "Sort", command = sort, bg = LIGHT_GRAY)
b1.grid(row = 2, column = 1, padx = 5, pady = 5)

# Generate Array Button
b2 = Button(UI_frame, text = "Generate Array", command = generate, bg = LIGHT_GRAY)
b2.grid(row = 2, column = 0, padx = 5, pady = 5)

# Stop Button
b3 = Button(UI_frame, text = "Stop", command = stop, bg = LIGHT_GRAY)
b3.grid(row = 2, column = 3, padx = 5, pady = 5)

# Canvas to draw Array
canvas = Canvas(window, width = 800, height = 400, bg = WHITE)
canvas.grid(row = 1, column = 0, padx = 10, pady = 5)

window.mainloop()

# TO DO
# Add stop button
# Add more algorithms
# Create better GUI