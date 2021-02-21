import time
from colors import *

def selection_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        curr_min = i
        for j in range(i+1, size):
            if data[j] < data[curr_min]:
                curr_min = j

        data[curr_min], data[i] = data[i], data[curr_min]
        drawData(data, [YELLOW if x == curr_min or x == i else BLUE for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, [BLUE for x in range(len(data))])