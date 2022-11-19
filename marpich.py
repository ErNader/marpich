from turtle import*
from random import*
list=['red','black','green']
for i in range(2*int(input("چند تا لايه ميخواي؟"))):
    color(choice(list))
    circle(i*10,180)
