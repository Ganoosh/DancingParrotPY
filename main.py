from os import system, name 
import os
from time import sleep 
from playsound import playsound
import time




def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

num = 0

print("Id like to note that I did not creat parrot.live and all credit goes to hugomd for the utility\nWith that said I did port the animation to python.")
time.sleep(3)
clear()

playsound('audio/song.mp3', False)

while True:
  if num > 9:
    num = 0
  file_c = f"frames/{num}.txt"
  f = open(file_c, 'r')
  file_contents = f.read()
  time.sleep(0.1)
  clear()
  print(file_contents)
  f.close
  num += 1
  
