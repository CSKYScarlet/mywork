# 터틀 가져오기
import os
import time
from turtle import *

showturtle()
shape("turtle")
setup(width=1000, height=1000)
count = 0
# 이동
speed(0)
# for value in range(120):
#     circle(50)
#     left(3)
# clear()
for value in range(90):
    left(10)
    forward(50)
    right(10)
    forward(50)
    right(170)
    forward(50)
    right(10)
    forward(50)
    left(2)
forward(100)
for value in range(36):
    circle(20)
    right(10)
while True:
    right(5)
    forward(10)
    
os.system("pause")