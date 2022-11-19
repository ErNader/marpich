from turtle import*
from random import*
list=['red','black','green']
sp=int(input("سرعت را وارد کنيد:"))
zavie=int(input("زاويه را وارد کنيد:[براي مارپيچ شدن بايد از 180 استفاده کنيئ]"))
for i in range(2*int(input("چند تا لايه ميخواي:"))):
    color(choice(list))
    speed(sp)
    circle(i*10,zavie)
