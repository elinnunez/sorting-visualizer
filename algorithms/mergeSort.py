import time
from colors import *

def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArr = []

    for i in range(start, end+1):
        if p > mid:
            tempArr.append(data[q])
            q+=1
        elif q > end:
            tempArr.append(data[p])
            p+=1
        elif data[p] < data[q]:
            tempArr.append(data[p])
            p+=1
        else:
            tempArr.append(data[q])
            q+=1
    
    for p in range(len(tempArr)):
        data[start] = tempArr[p]
        start+=1

def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid 
                            else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])