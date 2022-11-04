#https://storm-coder-dojo.github.io/activities/python/text-animations.html
import os
import time

def animate_space_invader():
  distance_from_top = 0
  distance_from_left_side = 0
  step = 1
  while True:
    print("\n" * distance_from_top)
    print((" " * distance_from_left_side) + "_SEXTOU!_")
    print((" " * distance_from_left_side) + "COM PYTHON")
    distance_from_left_side += step
    if distance_from_left_side > 20 or distance_from_left_side <= 0:
      step = -step 
      distance_from_top += 2
      if distance_from_top > 20:
        distance_from_top = 0
        distance_from_left_side = 0
        step = 1
    time.sleep(0.05)
    os.system('cls')  
  
#Main Program Starts Here....
animate_space_invader()
