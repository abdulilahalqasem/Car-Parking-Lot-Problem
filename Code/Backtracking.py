import sys
import random
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import time
import pygame


start = time.time()

sys.setrecursionlimit(5000)


pygame.init()
start_input  = Tk()
start_input.title("Car Parking Lot")
start_input.geometry('600x100+650+400')
start_input.iconbitmap(default="D:\co\Summer\CS340\Project\images\parking_sign.ico")
start_input.attributes("-topmost", True)

# start 
Label(start_input, text="Number of zones from 1-6: ").grid(row=0 , column=3)
Label(start_input, text="Number from 2-7 for the cars color: ").grid(row=1 , column=3)
input1 = IntVar()
input2 = IntVar()
Entry(start_input,textvariable = input1,width=50 , borderwidth= 5 ,).grid(row=0 , column=4)
Entry(start_input,textvariable = input2,width=50 , borderwidth= 5 ,).grid(row=1 , column=4)
Button(start_input,text = 'BackTracking',command=start_input.destroy).grid(row=4, column=4)
start_input.mainloop()
number_of_zones = input1.get()
number_of_colors = input2.get()

BT = Tk()
BT.title("Car Parking Lot")
BT.attributes("-topmost", True)
BT.geometry('1074x630+450+300')
canvas = Canvas(BT, width=1074, height=630)
canvas.pack()
tuple_canvas = ["D:\co\Summer\CS340\Project\images\parking_lot_layout_zoneA.png", "D:\co\Summer\CS340\Project\images\parking_lot_layout_zoneB.png",
                    "D:\co\Summer\CS340\Project\images\parking_lot_layout_zoneC.png",  "D:\co\Summer\CS340\Project\images\parking_lot_layout_zoneD.png",
                    "D:\co\Summer\CS340\Project\images\parking_lot_layout_zoneE.png",  "D:\co\Summer\CS340\Project\images\parking_lot_layout_zoneF.png"]

parking_lot_image = PhotoImage(file=tuple_canvas[number_of_zones - 1])  
canvas.create_image(0, 0, anchor=NW, image=parking_lot_image)

red_car_image = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\RedC.png').resize((45,100)))  # Red car image
blue_car_image = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\BlueC.png').resize((45,100)))  # Blue car image
green_car_image = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\GreenC.png').resize((45,100)))  # Green car image
yellow_car_image = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\YellowC.png').resize((45,100)))  # Yellow car image
indigo_car_image = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\IndigoC.png').resize((45,100)))  # Indigo car image
orange_car_image = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\OrangeC.png').resize((45,100)))  # orange car image
violet_car_image = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\VioletC.png').resize((45,100)))  # Violet car image
Number_of_Cars = ImageTk.PhotoImage(Image.open('D:\co\Summer\CS340\Project\images\\Number_of_Cars.png'))  # Number of Cars


car_tuple = (red_car_image, blue_car_image, green_car_image, yellow_car_image, indigo_car_image, orange_car_image, violet_car_image)

all_parking_spots = ((35, 38), (87, 38), (139, 38), (191, 38), (243, 38), (35, 145), (87, 145), (139, 145), (191, 145), (243, 145),
                     (408, 38), (460, 38), (512, 38), (564, 38), (616, 38), (408, 145), (460, 145), (512, 145), (564, 145), (616, 145),
                     (786, 38), (838, 38), (890, 38), (942, 38), (994, 38), (786, 147), (838, 147), (890, 147), (942, 147), (994, 147),
                     (35, 385), (87, 385), (139, 385), (191, 385), (243, 385), (35, 492), (87, 492), (139, 492), (191, 492), (243, 492),
                     (408, 385), (460, 385), (512, 385), (564, 385), (616, 385), (408, 492), (460, 492), (512, 492), (564, 492), (616, 492),
                     (786, 385), (838, 385), (890, 385), (942, 385), (994, 385), (786, 492), (838, 492), (890, 492), (942, 492), (994, 492))
                     # contains all spots positions.


n = number_of_zones * 10
m = number_of_colors

car_list = []
tuple1 = ('red', 'blue', 'green', 'yellow', 'indigo', 'orange', 'violet')

list1 = []  # The list that will have colors based on the user's amount.
i = 0
while i < m:  # While loop filling list1 from tuple1, with the amount of colors the user inputted.
    # Always fills from left to right of tuple1.
    list1.append(tuple1[i])
    i += 1
max_num = n / 2  # maximum number of cars for one color.
dict1 = {'red': max_num, 'blue': max_num, 'green': max_num, 'yellow': max_num, 'indigo': max_num,
         'orange': max_num, 'violet': max_num}  # a dictionary with all the 7 colors with their maximum amount.
while i < n+m:  # while loop filling list2 randomly, and making sure the list is solvable. *read
        # Note#1*
        r = random.choice(list1)
        dict1[r] = dict1[r] - 1
        if dict1[r] <= 0:
            list1.remove(r)
        
        car_list.append(r)
        i += 1


car_image_dict = {'red': car_tuple[0], 'blue': car_tuple[1], 'green': car_tuple[2], 'yellow': car_tuple[3],
                 'indigo': car_tuple[4], 'orange': car_tuple[5], 'violet': car_tuple[6]}

#random_domain = ['red', 'green', 'red', 'blue', 'green', 'red', 'green', 'red', 'green', 'red', 'red', 'green', 'blue', 'red', 'blue', 'blue', 'green', 'green', 'red', 'blue', 'green', 'green', 'green', 'blue', 'red', 'blue', 'blue', 'blue', 'blue', 'red']
spots = []
temp = []
color_dict = {1: 'red', 2: 'blue', 3: 'green', 4: 'yellow', 5: 'indigo', 6: 'orange', 7: 'violet'}
reversed_color_dict = {'red': 1, 'blue': 2, 'green': 3, 'yellow': 4, 'indigo': 5, 'orange': 6, 'violet': 7}
left_dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
a = m
f = left_dict[a]

number_of_colors_left = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
b = 1
d = 0

while b <= len(color_dict):  
    for d in range(len(car_list)):
        if color_dict[b] == car_list[d]:
            number_of_colors_left[b] = number_of_colors_left[b] + 1
    b = b+1


BE = tkinter.Toplevel()
BE.winfo_toplevel()
BE.title("Number Of Cars")
BE.attributes("-topmost", True)
BE.geometry('933x226+520+0')
canvas1 = Canvas(BE, width=933, height=226)
canvas1.create_image(0, 0, anchor=NW, image=Number_of_Cars)
canvas1.pack()
canvas1.update()
t = 1
listC = ((50,180),(190,180),(333,180),(477,180),(620,180),(770,180),(910,180))
while t <= m:
    canvas1.create_text(listC[t-1][0],listC[t-1][1],anchor=NE,font=("Arial" , 25),fill=color_dict[t],text= number_of_colors_left[t])
    t = t + 1  
canvas1.update()

def left_dict_add(c):
    left_dict[c] = left_dict[c] + 1
def left_dict_sub(c):
    left_dict[c] = left_dict[c] - 1
i = 1
j = 0
while i <= len(color_dict):  
    for j in range(len(car_list)):
        if color_dict[i] == car_list[j]:
            left_dict_add(i)
    i = i+1
def c_value(c):
    i = 1
    while i <= m:
        if left_dict[i] != 0 and i != c:
            return i
        i = i + 1
def check1_helper(k):
    
    while k >= 0:
        te = reversed_color_dict[spots.pop(k)]
        left_dict_add(te)
        if te == m:
            k = k - 1
            continue
    
        else:
            i = te + 1
    
        while i <= m:
        
            if left_dict[i] != 0:
                if is_safe(k, i):
                    backtrack(k, i)
            i = i + 1   
        k = k - 1  
def check1(k):
    
    i = 1
    count = m
    while i <= m:
        if left_dict[i] == 0:
            count = count - 1
        i = i + 1   
    if k <= n-1 and count <= m-1:
        check1_helper(k-1)
    if ((n-f-2) <= k <= n - f - 3) and count == m:  # add all colors except the last color. red=9, blue=14, green=7 --> 9+14=23 --> 23(-2)=21, 23(-3)=20. always (-2) and (-3).
        check1_helper(k-1)



#def check2():
def is_safe(k, c):

    if k <= 0:
        return True
    if 5 <= k <= 9 or 15 <= k <= 19 or 25 <= k <= 29 or 35 <= k <= 39 or 45 <= k <= 49 or 55 <= k <= 59:
        if k%5 == 0:
            if spots[k-5] == color_dict[c]:
                return False
            return True
        elif spots[k-1] == color_dict[c] or spots[k-5] == color_dict[c]:
            return False
        return True
    if k%10 == 0:  # new!!!!!!!
        return True
    if spots[k-1] == color_dict[c]:
        return False
    return True
def backtrack(k, c):
    if left_dict[c] == 0:
        c = c_value(c)
    if is_safe(k, c):
        spots.append(color_dict[c])
        canvas.create_image(all_parking_spots[k][0], all_parking_spots[k][1], anchor=NW,image=car_image_dict[spots[k]])
        time.sleep(0.3)
        #pygame.mixer.music.load("D:\co\Summer S6+\CS340\Project\images\Sound1.mp3") #Sound with each car
        #pygame.mixer.music.play() #Playing It In The Whole Device
        canvas.update()
        left_dict_sub(c)
        if k < n-1:
            backtrack(k+1, 1)
        else:               
            canvas.create_text(340,270,anchor=NW,font=("Arial" , 60),fill="green",text="SUCCESS")
            canvas.update()

            end = time.time()
            Ax = (end - start)
            m = float("{0:.3f}".format(Ax))

            canvas.create_text(800,270,anchor=NW,font=("Arial" , 60),fill="red",text= m)
            canvas.update()
            time.sleep(10)
            sys.exit(0)
    else:
        check1(k)
        c = c_value(c)
        backtrack(k, c)
    
backtrack(0, 1)
BT.mainloop()