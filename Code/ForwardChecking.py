import sys
import random
from tkinter import *
import tkinter
from PIL import ImageTk, Image
import time
import pygame
import copy

sys.setrecursionlimit(5000)

start = time.time()

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
Button(start_input,text = 'ForwardChecking',command=start_input.destroy).grid(row=4, column=4)
start_input.mainloop()
number_of_zones = input1.get()
number_of_colors = input2.get()

FC = Tk()
FC.title("Car Parking Lot")
FC.attributes("-topmost", True)
FC.geometry('1074x630+450+300')
canvas = Canvas(FC, width=1074, height=630)
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

car_image_dict = {'red': car_tuple[0], 'blue': car_tuple[1], 'green': car_tuple[2], 'yellow': car_tuple[3],
                 'indigo': car_tuple[4], 'orange': car_tuple[5], 'violet': car_tuple[6]}



class ForwardCheck:

    def CarMaker(number_of_zones, number_of_colors):
        
        tuple1 = ('red', 'blue', 'green', 'yellow', 'indigo', 'orange', 'violet')  # This tuple contains all possible colors
        # cars can have.
        temp_list = []  # The list that will have colors based on the user's amount.

        i = 0
        while i < number_of_colors:  # While loop filling list1 from tuple1, with the amount of colors the user inputted.
            # Always fills from left to right of tuple1.
            temp_list.append(tuple1[i])
            i += 1


        Domain = []  # this list will contain all the cars that need to be parked. *only the colors from list1*
        number_parking_spots = number_of_zones * 10  # each zone has 10 spots hence the total number of parking spots is:
        # number of zones times 10.
        max_num = number_parking_spots / 2  # maximum number of cars for one color.

        dict1 = {'red': max_num, 'blue': max_num, 'green': max_num, 'yellow': max_num, 'indigo': max_num,
                 'orange': max_num, 'violet': max_num}  # a dictionary with all the 7 colors with their maximum amount.

        i = 0
        while i < number_parking_spots:  # while loop filling list2 randomly, and making sure the list is solvable. *read
            # Note#1*
            r = random.choice(temp_list)
            dict1[r] -= 1

            if dict1[r] == 0:
                temp_list.remove(r)

            Domain.append(r)
            i += 1

        return Domain


    Domain = CarMaker(number_of_zones, number_of_colors)  #function call to CarMaker.
    
    n = number_of_zones * 10
    m = number_of_colors

    color_dict = {1: 'red', 2: 'blue', 3: 'green', 4: 'yellow', 5: 'indigo', 6: 'orange', 7: 'violet'}
    reversed_color_dict = {'red': 1, 'blue': 2, 'green': 3, 'yellow': 4, 'indigo': 5, 'orange': 6, 'violet': 7}
    colors_available = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    spots = [0] * n
    spot_color_list = [0] * n
    temp = [0] * m

    number_of_colors_left = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    b = 1
    d = 0
    while b <= len(color_dict):  
        for d in range(len(Domain)):
            if color_dict[b] == Domain[d]:
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



    def ColorsAvailableAdd(self, c):  # add a color to colors_available dictionary.
        colors_available = self.colors_available
        colors_available[c] = colors_available[c] + 1


    def ColorsAvailableSub(self, c):  # subtract a color from colors_available dictionary.
        colors_available = self.colors_available
        colors_available[c] = colors_available[c] - 1
        

    def ColorCount(self):  # counts all the colors from the given domain, into colors_available dictionary.
        
        color_dict = self.color_dict
        Domain = self.Domain

        i = 1
        while i <= len(color_dict):  
            for j in range(len(Domain)):
                if color_dict[i] == Domain[j]:
                   self.ColorsAvailableAdd(i)
            i = i+1


    def SpotsDomain(self):  # fills all colors each spot can have before starting.

        colors_available = self.colors_available
        temp = self.temp
        reversed_color_dict = self.reversed_color_dict
        color_dict = self.color_dict
        spot_color_list = self.spot_color_list

        j = 1
        for i in range(self.n):
            while j <= self.m:
                if colors_available[j] != 0:
                    temp[j-1] = reversed_color_dict[color_dict[j]]
                    
                j = j + 1
            j = 1
            spot_color_list[i] = temp.copy()

    

    def CheckConstraints(self, k, c):  # checks if the constraints are violated, and returns true or false based on violation occurrence.
        
        spots = self.spots
        color_dict = self.color_dict

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

        if k%10 == 0:  
            return True

        if spots[k-1] == color_dict[c]:
            return False
        return True


    def NextBestValue(self, k, c):
        
        spot_color_list = self.spot_color_list
        colors_available = self.colors_available

        if c == self.m:
            return 0

        c = c + 1
        while c <= self.m:
            if spot_color_list[k][c-1] != 0 and colors_available[c] != 0:
                return c
            c = c + 1

        return 0    


    def SpotRetriveValue(self, k): 

        spot_color_list = self.spot_color_list
        colors_available = self.colors_available

        i = 1
        while i <= self.m:
            if spot_color_list[k][i-1] != 0 and colors_available[i] != 0:       
                return i
            i = i + 1

        sys.exit(0)


    def SpotColorListAdd(self, k, c):

        spot_color_list = self.spot_color_list
        
        if k == 0:
            spot_color_list[5][c-1] = c
            spot_color_list[k+1][c-1] = c
            return
        if 5 <= k <= 9 or 15 <= k <= 19 or 25 <= k <= 29 or 35 <= k <= 39 or 45 <= k <= 49 or 55 <= k <= 59:
            if (k+1)%5 == 0:  # if spot k= 9,19,29,39,49 or 59 then no need to check any spots. 
                return
            else:
                if spot_color_list[k+1-5][c-1] != c:
                    spot_color_list[k+1][c-1] = c
                return 

        elif (k+1)%5 == 0:  # if spot k= 4,14,24,34,44 or 54 then no need to check k+1. 
            spot_color_list[k+5][c-1] = c
            return
        else:
            spot_color_list[k+1][c-1] = c
            spot_color_list[k+5][c-1] = c
            return


    def BringBackColor(self, k, c):
        
        spot_color_list = self.spot_color_list
        spots = self.spots
        reversed_color_dict = self.reversed_color_dict

        while k < self.n:
            if k == 0:
                spot_color_list[5][c-1] = c
                spot_color_list[k+1][c-1] = c
                k = k + 1
                continue

            if 5 <= k <= 9 or 15 <= k <= 19 or 25 <= k <= 29 or 35 <= k <= 39 or 45 <= k <= 49 or 55 <= k <= 59:
                if k%5 == 0:  # if spot k= 9,19,29,39,49 or 59 then no need to check any spots. 
                    if spots[k-5] == 0 or reversed_color_dict[spots[k-5]] != c:
                        spot_color_list[k][c-1] = c  
                        k = k + 1
                        continue   
                    
                elif (spots[k-5] == 0 or reversed_color_dict[spots[k-5]] != c) and (spots[k-1] == 0 or reversed_color_dict[spots[k-1]] != c):
                    spot_color_list[k][c-1] = c 
                    k = k + 1
                    continue   

            elif spots[k-1] == 0 or reversed_color_dict[spots[k-1]] != c: 
                spot_color_list[k][c-1] = c  
                k = k + 1
                continue 

            k = k + 1

    def UpdateSpotColorList(self, k, clone_spot_color_list, clone_colors_available):

        i = 1
        while i <= self.m:

            j = k
            while j < len(clone_spot_color_list):
                
                if clone_colors_available[i] == 0:
                    clone_spot_color_list[j][i-1] = 0
                j = j + 1
            
            i = i + 1


    def IsEmpty(self, k, c):

        spot_color_list = self.spot_color_list
        spots = self.spots
        colors_available = self.colors_available
        color_dict = self.color_dict

        clone_spot_color_list = copy.deepcopy(spot_color_list)
        clone_colors_available = copy.deepcopy(colors_available)
        clone_spots = copy.deepcopy(spots)

        clone_spots[k] = color_dict[c]
        clone_colors_available[c] = clone_colors_available[c] - 1
        self.UpdateSpotColorList(k, clone_spot_color_list, clone_colors_available)

        k = k + 1
        while k < self.n:
        
            j = 0
            counter = 0
            while j < self.m:
                if clone_spot_color_list[k][j] == 0:
                    counter = counter + 1
                j = j + 1

            if counter == self.m:
                return True

            k = k + 1
        
        return False


    def BeforeCheck(self, k, c):

        def Helper(k, c):

            spot_color_list = self.spot_color_list
        
            clone = []
            clone = copy.deepcopy(spot_color_list)

            clone[k][c-1] = 0

            i = 1
            while i <= self.m:  
                
                if clone[k][i-1] != 0:        
                    del clone
                    return True
                i = i + 1

            del clone
            return False


        if k == 0:
            t1 = Helper(5, c)
            t2 = Helper(k+1, c)
            if t1 and t2:
                return True
            return False

        if 5 <= k <= 9 or 15 <= k <= 19 or 25 <= k <= 29 or 35 <= k <= 39 or 45 <= k <= 49 or 55 <= k <= 59:
            if (k+1)%5 == 0:  # if spot k= 9,19,29,39,49 or 59 then no need to check any spots. 
                return True
            else:
                t1 = Helper(k+1, c)
                return t1

        elif (k+1)%5 == 0:  # if spot k= 4,14,24,34,44 or 54 then no need to check k+1.
            t1 = Helper(k+5, c)
            return t1
        else:  
            t1 = Helper(k+1, c)
            t2 = Helper(k+5, c)
            if t1 and t2:
                return True
            return False


    def checked2(self, k, c):  

        spot_color_list = self.spot_color_list
        
        spot_color_list[k][c-1] = 0  

        i = 1
        while i <= self.m:
            
            if spot_color_list[k][i-1] != 0:        
                return
            i = i + 1

        return False
        

    def checked1(self, k, c):

        if k == 0:
            self.checked2(5, c)
            self.checked2(k+1, c)
            return

        if 5 <= k <= 9 or 15 <= k <= 19 or 25 <= k <= 29 or 35 <= k <= 39 or 45 <= k <= 49 or 55 <= k <= 59:
            if (k+1)%5 == 0:  # if spot k= 9,19,29,39,49 or 59 then no need to check any spots. 
                return
            else:
                self.checked2(k+1, c)
                return

        elif (k+1)%5 == 0:  # if spot k= 4,14,24,34,44 or 54 then no need to check k+1.
            self.checked2(k+5, c)
            return
        else:
            self.checked2(k+1, c)
            self.checked2(k+5, c)
            return


    def CheckAll(self, k, c):

        reversed_color_dict = self.reversed_color_dict
        spots = self.spots
        spot_color_list = self.spot_color_list

        te = self.NextBestValue(k, c)
        
        if te == 0:
            while te == 0:
    
                k = k - 1

                t1 = reversed_color_dict[spots[k]]  # pop!
                spots[k] = 0  # pop! 
                
                self.ColorsAvailableAdd(t1)
                self.SpotColorListAdd(k, t1)
                self.BringBackColor(k+1, t1)

                te = self.NextBestValue(k, t1)
            
            self.RunForwardChecking(k, te)
            return
        else:
            self.RunForwardChecking(k, te)
            return

    def RunForwardChecking(self, k, c):
        
        if self.CheckConstraints(k, c):
            if self.BeforeCheck(k, c):  # if FALSE then try another color if there is no more colors backtrack.
                if self.IsEmpty(k, c):
                    self.CheckAll(k, c)
                else:
                    self.checked1(k, c)
                
                spots = self.spots
                spot_color_list = self.spot_color_list
                color_dict = self.color_dict
                colors_available = self.colors_available

                spots[k] = color_dict[c]
                
                canvas.create_image(all_parking_spots[k][0], all_parking_spots[k][1], anchor=NW, image=car_image_dict[spots[k]])
                time.sleep(0.3)
                #pygame.mixer.music.load("D:\co\Summer S6+\CS340\Project\images\Sound1.mp3") #Sound with each car
                #pygame.mixer.music.play()  # Playing It In The Whole Device.
                canvas.update()

                self.ColorsAvailableSub(c)
                self.UpdateSpotColorList(k+1, spot_color_list, colors_available)
                
                if k+1 < self.n:
                    self.RunForwardChecking(k+1, self.SpotRetriveValue(k+1))
                else:
                    canvas.create_text(340,270,anchor=NW,font=("Arial" , 60),fill="green",text="SUCCESS")
                    canvas.update()
                    canvas.update()
                   
                    end = time.time()
                    Ax = (end - start)
                    run_time = float("{0:.3f}".format(Ax))
                    
                    canvas.update()
                    
                    canvas.create_text(800,270,anchor=NW,font=("Arial" , 60),fill="red",text= run_time)
                    self.canvas1.update()
                    
                    time.sleep(10)
                    
                    sys.exit(0)

            else:
                self.CheckAll(k, c)
                
        else:
            self.RunForwardChecking(k, self.SpotRetriveValue(k))


FC_object = ForwardCheck()  # an instance of class ForwardCheck.

FC_object.ColorCount()  # run ColorCount.
FC_object.SpotsDomain()  # run SpotsDomain.

FC_object.RunForwardChecking(0, 1)  # function call to RunForwardChecking

FC.mainloop()