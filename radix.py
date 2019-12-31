import pygame
import random

running = True

pygame.init()
width = 800
height = 400
display = pygame.display.set_mode((width, height))
display.fill((0,0,0))
pygame.display.update()

arrlen = 800
heightr = height/arrlen
unsorted = [int(i*heightr) for i in range(1, arrlen+1)]
random.shuffle(unsorted)

def disparr(arr, length, hl=-1):
    global width, height, display
    linwidth = int(width/length)

    pygame.time.delay(5)
    display.fill((0,0,0))
    
    for i in range(length):
        color = (255, 255, 255)
        if i == hl:
            color = (255, 0, 0)
        pygame.draw.line(display, color, (i*linwidth, height), (i*linwidth, height-arr[i]), linwidth)

    pygame.display.update()

#disparr(unsorted, arrlen)

def getmaxdig(nums):
    dig = 0
    for num in nums:
        if len(str(num)) > dig:
            dig = len(str(num))

    return dig

def sigdig(num, place):
    strnum = str(num)
    if place <= len(strnum):
        return int(strnum[-place])
    else:
        return 0

def radix(unsorted):
    sorting = unsorted.copy()

    maxdig = getmaxdig(unsorted)

    buckets = []

    for i in range(10):
        buckets.append([])

    for i in range(1, maxdig +1):        
        for j in range(len(sorting)):
            sig = sigdig(sorting[j], i)
            buckets[sig].append(sorting[j])

            disparr(sorting, arrlen, j)

        temp = []
        for j in range(len(buckets)):
            temp += buckets[j]
            buckets[j] = []

        for j in range(len(temp)):
            sorting[j] = temp[j]

            disparr(sorting, arrlen, j)

    return sorting

"""
#Try to figure out how to do it step by step so I can close it nicely

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
"""
    
sort = radix(unsorted)
disparr(sort, arrlen)
#pygame.time.delay(10)

input("Exit: ")
pygame.quit()
quit()













