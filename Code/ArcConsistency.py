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
Button(start_input,text = 'ArcConsistency',command=start_input.destroy).grid(row=4, column=4)
start_input.mainloop()
number_of_zones = input1.get()
number_of_colors = input2.get()

AC = Tk()
AC.title("Car Parking Lot")
AC.attributes("-topmost", True)
AC.geometry('1074x630+450+300')
canvas = Canvas(AC, width=1074, height=630)
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


class ArcConsistency:

    def CarMaker(number_of_zones, number_of_colors):
        """The class that is responsible for the amount of cars and allowable colors"""
        
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

    Domain = CarMaker(number_of_zones, number_of_colors)

    n = number_of_zones * 10
    m = number_of_colors

    
    car_image_dict = {'red': car_tuple[0], 'blue': car_tuple[1], 'green': car_tuple[2], 'yellow': car_tuple[3],
                 'indigo': car_tuple[4], 'orange': car_tuple[5], 'violet': car_tuple[6]}

    color_dict = {1: 'red', 2: 'blue', 3: 'green', 4: 'yellow', 5: 'indigo', 6: 'orange', 7: 'violet'}
    reversed_color_dict = {'red': 1, 'blue': 2, 'green': 3, 'yellow': 4, 'indigo': 5, 'orange': 6, 'violet': 7}
    colors_available = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    flag = False
    spots = [0] * n
    spot_color_list = [0] * n
    temp = [0] * m
    arc_dict = {}

    spot_color_list_reset = [0] * n
    colors_available_reset = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    descending_color_dict = {1: 'violet', 2: 'orange', 3: 'indigo', 4: 'yellow', 5: 'green', 6: 'blue', 7: 'red'}
    descending_reversed_color_dict = {'violet': 1, 'orange': 2, 'indigo': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'red': 7}
    descending_colors_available = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

    
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
        te = self.m+1
    
        i = 1
        while i <= len(color_dict):  
            for j in range(len(Domain)):
                if color_dict[i] == Domain[j]:
                   self.ColorsAvailableAdd(i)
                   self.descending_colors_available[te-i] = self.descending_colors_available[te-i] + 1
                   self.colors_available_reset[i] = self.colors_available_reset[i] + 1
            i = i+1


    def DeceandingOrder(self):
        
        for i in range(len(self.spots)):
            for j in range(len(self.m)):
                #(self.m+1) - self.reversed_color_dict[self.spots[i]]
                self.spots[i] = self.color_dict[(self.m+1) - self.reversed_color_dict[self.spots[i]]]  




    def SpotsDomain(self):  # fills all colors each spot can have before starting.

        colors_available = self.colors_available
        temp = self.temp
        reversed_color_dict = self.reversed_color_dict
        color_dict = self.color_dict
        spot_color_list = self.spot_color_list
        spot_color_list_reset = self.spot_color_list_reset

        j = 1
        for i in range(self.n):
            while j <= self.m:
                if colors_available[j] != 0:
                    temp[j-1] = reversed_color_dict[color_dict[j]]
                    
                j = j + 1
            j = 1
            spot_color_list[i] = temp.copy()
            spot_color_list_reset[i] = temp.copy


    def FillSpotsList(self, clone_spot_color_list):

        for i in range(len(clone_spot_color_list)):
            for j in range(self.m):
                if clone_spot_color_list[i][j] != 0:
                    self.spots[i] = self.color_dict[j+1]
        print("FILL COMPLETE!")
        

    def Check2(self, clone_spot_color_list, k1, k2, c):

        #print("spot_color_list in check2 =", self.spot_color_list)
        print("clone_spot_color_list in check2 =", clone_spot_color_list)
        
        for i in range(self.m):
            if clone_spot_color_list[k2][i] != 0:
                if clone_spot_color_list[k1][c-1] != clone_spot_color_list[k2][i]:  # from k1 to k2
                    #print("(check2): from k1 to k2 is TRUE!!!")
                    print("(check2): k1 =", k1, "and k2 =", k2, "with c =", c, "are consistent!")
                    print("--------------------------------------------------------------------")
                    return True

        return False


    def Check1(self, clone_spot_color_list, k, c):

        if k == 0:
            t1 = self.Check2(clone_spot_color_list, k, k+1, c)
            t2 = self.Check2(clone_spot_color_list, k, k+5, c)
            if t1 and t2:
                self.Check3(clone_spot_color_list, k+1, c)
                self.Check3(clone_spot_color_list, k+5, c)
                return True
            return False

        if 5 <= k <= 9 or 15 <= k <= 19 or 25 <= k <= 29 or 35 <= k <= 39 or 45 <= k <= 49 or 55 <= k <= 59:
            if k%5 == 0:
                t1 = self.Check2(clone_spot_color_list, k, k+1, c)
                t2 = self.Check2(clone_spot_color_list, k, k-5, c)
                if t1 and t2:
                    self.Check3(clone_spot_color_list, k+1, c)
                    self.Check3(clone_spot_color_list, k-5, c)
                    return True
                return False    

            if (k+1)%10 == 0:  # 9,19,29,...
                t1 = self.Check2(clone_spot_color_list, k, k-1, c)
                t2 = self.Check2(clone_spot_color_list, k, k-5, c)
                if t1 and t2:
                    self.Check3(clone_spot_color_list, k-1, c)
                    self.Check3(clone_spot_color_list, k-5, c)
                    return True
                return False

            else:
                t1 = self.Check2(clone_spot_color_list, k, k-1, c)
                t2 = self.Check2(clone_spot_color_list, k, k+1, c)
                t3 = self.Check2(clone_spot_color_list, k, k-5, c)
                if t1 and t2 and t3:
                    self.Check3(clone_spot_color_list, k-1, c)
                    self.Check3(clone_spot_color_list, k+1, c)
                    self.Check3(clone_spot_color_list, k-5, c)
                    return True
                return False

        else:
            if k%10 == 0:  # 0,10,20,30,40,50,60
                t1 = self.Check2(clone_spot_color_list, k, k+1, c)
                t2 = self.Check2(clone_spot_color_list, k, k+5, c)
                if t1 and t2:
                    self.Check3(clone_spot_color_list, k+1, c)
                    self.Check3(clone_spot_color_list, k+5, c)
                    return True
                return False
        
            if (k+1)%5 == 0:  # 4,,14,24,...
                t1 = self.Check2(clone_spot_color_list, k, k-1, c)
                t2 = self.Check2(clone_spot_color_list, k, k+5, c)
                if t1 and t2:
                    self.Check3(clone_spot_color_list, k-1, c)
                    self.Check3(clone_spot_color_list, k+5, c)
                    return True
                return False

            else:
                t1 = self.Check2(clone_spot_color_list, k, k-1, c)
                t2 = self.Check2(clone_spot_color_list, k, k+1, c)
                t3 = self.Check2(clone_spot_color_list, k, k+5, c)
                if t1 and t2 and t3:
                    self.Check3(clone_spot_color_list, k-1, c)
                    self.Check3(clone_spot_color_list, k+1, c)
                    self.Check3(clone_spot_color_list, k+5, c)
                    return True
                return False


    def Check3(self, clone_spot_color_list, k, c):

        clone_spot_color_list[k][c-1] = 0
    
    
    def NextBestValue(self, k, c):

        spot_color_list = self.spot_color_list
        colors_available = self.colors_available

        if c == self.m:
            print("(NextBestValue1): ERROR NO COLORS REMAINING FOR k =", k)
            return 0

        c = c + 1
        while c <= self.m:
            if spot_color_list[k][c-1] != 0 and colors_available[c] != 0:
                return c

            c = c + 1

        print("(NextBestValue2): ERROR NO COLORS REMAINING FOR k =", k)
        return 0


    def IsEmpty(self, k, clone_spot_color_list):
        
        counter = 0

        i = 0
        while i < len(clone_spot_color_list):
            counter = 0
            j = 0
            while j < self.m:
                
                if clone_spot_color_list[i][j] == 0:
                    counter = counter + 1
                j = j + 1

            if counter == self.m:
                print("(IsEmpty): k =", k, "is empty!!!")
                return True

            i = i + 1

        #print("(IsEmpty): FALSE k =", k, "is NOT empty")
        return False
        
    def UpdateSpotColorList(self, clone_spot_color_list, clone_colors_available, k):
        
        i = 1
        while i <= self.m:
            
            j = k+1
            while j < len(clone_spot_color_list):

                if clone_colors_available[i] == 0:
                    clone_spot_color_list[j][i-1] = 0    
                j = j + 1
                
            i = i + 1

        return self.IsEmpty(k, clone_spot_color_list)


    def SpotRetriveValue(self, k):  # but will reset if new spot interfere.

        spot_color_list = self.spot_color_list
        colors_available = self.colors_available

        i = 1
        while i <= self.m:
            if spot_color_list[k][i-1] != 0 and colors_available[i] != 0:        #if colors_available[i] != 0 and i != c:
                return i
            i = i + 1
        print("(SpotRetriveValue): ERROR NO COLORS REMAINING")
        sys.exit(0)


    def Assign(self, k, c):
        
        self.spot_color_list
        self.colors_available

        print()
        print("(Assign): k =", k, "c =", c)
        #print("spot_color_list =", spot_color_list)

        clone_spot_color_list = copy.deepcopy(self.spot_color_list)
        clone_colors_available = copy.deepcopy(self.colors_available)

        for i in range(self.m):
            if clone_spot_color_list[k][i] != c:
                clone_spot_color_list[k][i] = 0
        
        #print("clone_spot_color_lsit =", clone_spot_color_list)

        clone_colors_available[c] = clone_colors_available[c] - 1
        
        if self.UpdateSpotColorList(clone_spot_color_list, clone_colors_available, k):
            print("(Assign): ERROR TRY FROM START")
            
            

            for i in range(self.m):
                if clone_spot_color_list[0][i] != 0:
                    te = i+1
            
            if te == self.m:
                print("NO SOLUTION!!!!! FOR ASCENDING")
                print()
            
                if self.flag == True:
                    print("flag true!!!!!!!")
                    print("EVEN DESEANDING CAN't SOLVE IT!!!")
                    canvas.create_text(340,270,anchor=NW,font=("Arial" , 60),fill="red",text="FAILURE")
                    canvas.update()
                    end = time.time()
                    Ax = (end - start)
                    run_time = float("{0:.3f}".format(Ax))
                    canvas.create_text(800,270,anchor=NW,font=("Arial" , 60),fill="red",text= run_time)
                    canvas.update()
                    time.sleep(10)
                    sys.exit(0)
                else:
                    print("TRY DECSINDING........")
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    self.flag = True
                    self.colors_available = copy.deepcopy(self.descending_colors_available)

                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    #print("clone_spot_color_list =", clone_spot_color_list)
                    #print("te =", te)

                    


                    for i in range(len(self.spot_color_list)):
                        for j in range(self.m):
                            self.spot_color_list[i][j] = j+1 

                    #self.colors_available = copy.deepcopy(self.colors_available_reset)
                
                    print(self.spot_color_list)
                    self.Assign(0, 1)


            else:
                print("0000000000000000000000000000000000000000000000000000000")
                print("clone_spot_color_list =", clone_spot_color_list)
                print("te =", te)
                
                for i in range(len(self.spot_color_list)):
                    for j in range(self.m):
                        self.spot_color_list[i][j] = j+1 

                self.colors_available = copy.deepcopy(self.colors_available_reset)
                
                print(self.spot_color_list)
                self.Assign(0, te+1)


            '''sys.exit(0)
            #self.RunArcConsistenty(k, self.NextBestValue(k, c))'''
            

        if self.Check1(clone_spot_color_list, k, c):
            print("(Assign): Check1 TRUE!!!!")
            #spot_color_list = copy.deepcopy(clone_spot_color_list)
            #colors_available = copy.deepcopy(clone_colors_available)
            self.spot_color_list = copy.deepcopy(clone_spot_color_list)
            self.spots[k] = self.color_dict[c]
            canvas.create_image(all_parking_spots[k][0], all_parking_spots[k][1], anchor=NW,image=self.car_image_dict[self.spots[k]])
            time.sleep(0.3)
            #pygame.mixer.music.load("D:\co\Summer S6+\CS340\Project\images\Sound1.mp3") #Sound with each car
            #pygame.mixer.music.play() #Playing It In The Whole Device
            canvas.update()
            self.colors_available = copy.deepcopy(clone_colors_available)
            print("spot_color_list =", self.spot_color_list)
            print()
            #print("clone_spot_color_lsit =", clone_spot_color_list)
            #print("spot_color_lsit =", self.spot_color_list)
            #print("colors_available =", clone_colors_available)
            self.RunArcConsistenty(k+1, c)

        else:
            print("(Assign): arc constraint error!!!")
            
            for i in range(self.m):
                if clone_spot_color_list[0][i] != 0:
                    te = i+1
            
            if te == self.m:
                print("NO SOLUTION!!!!!")
                #sys.exit(0)
                if self.flag == True:
                    print("flag true!!!!!!!")
                    print("EVEN DESEANDING CAN't SOLVE IT!!!")
                    canvas.create_text(340,270,anchor=NW,font=("Arial" , 60),fill="red",text="FAILURE")
                    canvas.update()
                    end = time.time()
                    Ax = (end - start)
                    run_time = float("{0:.3f}".format(Ax))
                    canvas.create_text(800,270,anchor=NW,font=("Arial" , 60),fill="red",text= run_time)
                    canvas.update()
                    time.sleep(10)
                    sys.exit(0)
                else:
                    print("TRY DECSINDING........")
                    print()
                    print()
                    print()
                    print()
                    print()
                    print()
                    self.flag = True
                    self.colors_available = copy.deepcopy(self.descending_colors_available)

                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    print("0000000000000000000000000000000000000000000000000000000")
                    #print("clone_spot_color_list =", clone_spot_color_list)
                    #print("te =", te)
                
                    for i in range(len(self.spot_color_list)):
                        for j in range(self.m):
                            self.spot_color_list[i][j] = j+1 

                    #self.colors_available = copy.deepcopy(self.colors_available_reset)
                
                    print(self.spot_color_list)
                    self.Assign(0, 1)
            else:
                print("0000000000000000000000000000000000000000000000000000000")
                print("clone_spot_color_list =", clone_spot_color_list)
                print("te =", te)
                
                for i in range(len(self.spot_color_list)):
                    for j in range(self.m):
                        self.spot_color_list[i][j] = j+1 

                self.colors_available = copy.deepcopy(self.colors_available_reset)
                
                print(self.spot_color_list)
                self.Assign(0, te+1)

            #sys.exit(0)
            #self.RunArcConsistenty(k, self.NextBestValue(k, c))

    def RunArcConsistenty(self, k, c):

        #print(self.spot_color_list) 

        if k < self.n:
            c = self.SpotRetriveValue(k)
            self.Assign(k, c)

        else:
            print()
            #self.FillSpotsList(self.spot_color_list)
            
            if self.flag:
                print("(RunArcConsistency): FLAG TRUE!!!!!!!!")
                self.DeceandingOrder()
                #print(self.spots)
            
            canvas.create_text(340,270,anchor=NW,font=("Arial" , 60),fill="green",text="SUCCESS")
            canvas.update()

            end = time.time()
            Ax = (end - start)
            m = float("{0:.3f}".format(Ax))

            canvas.create_text(800,270,anchor=NW,font=("Arial" , 60),fill="red",text= m)
            canvas.update()
            time.sleep(10)
            sys.exit(0)



AC_object = ArcConsistency()

AC_object.ColorCount()  # run ColorCount.
print("colors_available =", AC_object.colors_available)
print()
print("deceanding_colors_available =", AC_object.descending_colors_available)
print()
AC_object.SpotsDomain()  # run SpotsDomain.
AC_object.RunArcConsistenty(0, 1)  # function call to RunForwardChecking

#AC.mainloop()