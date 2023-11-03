#Project MASTERMIND by Zunnash Khan (MTS B)
import pygame, sys
from pygame import mouse
from pygame.locals import* #locals module
import random, time
pygame.init()
FPS = 60
frames_per_sec = pygame.time.Clock()

#DICTIONARY
color_dict = dict({1: "blue", 2: "red", 3: "green", 4: "yellow",5: "white", 6: "pink"})
#print ("Mastercode: ")
#Mastercode generated for Single Player Game
Mastercode = []
code = []
for i in range(0,4):
    n=random.randint(1,6)
    Mastercode.append(n)
    code.append(color_dict[n])
#print(Mastercode)
#print (code)


#(width, height)= (692,650)
#screen = pygame.display.set_mode((width,height))

#SP

#Setting up a pygame window of constant size
(width, height)= (1200,651)
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('MASTERMIND')
#defining colors
blue = (0,0,255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
white = (255,255,255)
black = (0,0,0)

#loading sounds 
pygame.mixer.init()
bongo = pygame.mixer.Sound("BONGO.wav")
win_music= pygame.mixer.Sound("win_music.wav")
lose_music=pygame.mixer.Sound("lose_music.wav")

#load images
#Loading Background images, sp stands for single player
background_sp = pygame.image.load("_res 1.png").convert()
background = pygame.image.load("ddd.png").convert()
menu =  pygame.image.load("MENU.png").convert()

zero = pygame.image.load("zero.png").convert()
zero.set_colorkey(black)
one = pygame.image.load("one.png").convert()
one.set_colorkey(black)
two = pygame.image.load("two.png").convert()
two.set_colorkey(black)
three = pygame.image.load("three.png").convert()
three.set_colorkey(black)
four = pygame.image.load("four.png").convert()
four.set_colorkey(black)

ball_1 = pygame.image.load("blue_ball.png").convert()
ball_1.set_colorkey(black)
ball_2 = pygame.image.load("red_ball.png").convert()
ball_2.set_colorkey(black)
ball_4 = pygame.image.load("yellow_ball.png").convert()
ball_4.set_colorkey(black)
ball_5 = pygame.image.load("white_ball.png").convert()
ball_5.set_colorkey(black)
ball_6 = pygame.image.load("pink_ball.png").convert()
ball_6.set_colorkey(black)
ball_3 = pygame.image.load("green_ball.png").convert()
ball_3.set_colorkey(black)
ball_x = [ball_1,ball_2,ball_3,ball_4,ball_5,ball_6]

locked = pygame.image.load("locked.png").convert()
locked.set_colorkey(black)
draw = pygame.image.load("draw.png").convert()
draw.set_colorkey(black)

win = pygame.image.load("win.png").convert()
win.set_colorkey(black)
lose = pygame.image.load("lose.png").convert()
lose.set_colorkey(white)

#Defining rectangles on the screen, MC_rect are mastercode rects for two player
MC_rect1= pygame.Rect(10,116,66,47)
MC_rect2= pygame.Rect(76,116,66,47)
MC_rect3= pygame.Rect(151,116,66,47)
MC_rect4= pygame.Rect(224,116,66,47)

MC_rect5= pygame.Rect(692,112,66,47)
MC_rect6= pygame.Rect(758,112,66,47)
MC_rect7= pygame.Rect(832,112,66,47)
MC_rect8= pygame.Rect(906,112,66,47)

Rect1= pygame.Rect(11,588,65,44)
Rect2= pygame.Rect(84,588,65,44)
Rect3= pygame.Rect(153,588,65,44)
Rect4= pygame.Rect(222,588,65,44)

Rect1b= pygame.Rect(11,537,65,44)
Rect2b= pygame.Rect(84,537,65,44)
Rect3b= pygame.Rect(153,537,65,44)
Rect4b= pygame.Rect(222,537,65,44)

Rect1c= pygame.Rect(11,494,65,44)
Rect2c= pygame.Rect(84,494,65,44)
Rect3c= pygame.Rect(153,494,65,44)
Rect4c= pygame.Rect(222,494,65,44)

Rect1d= pygame.Rect(11,445,65,44)
Rect2d= pygame.Rect(84,445,65,44)
Rect3d= pygame.Rect(153,445,65,44)
Rect4d= pygame.Rect(222,445,65,44)

Rect1e= pygame.Rect(11,399,65,44)
Rect2e= pygame.Rect(84,399,65,44)
Rect3e= pygame.Rect(153,399,65,44)
Rect4e= pygame.Rect(222,399,65,44)

Rect1f= pygame.Rect(11,353,65,44)
Rect2f= pygame.Rect(84,353,65,44)
Rect3f= pygame.Rect(153,353,65,44)
Rect4f= pygame.Rect(222,353,65,44)

Rect1g= pygame.Rect(11,307,65,44)
Rect2g= pygame.Rect(84,307,65,44)
Rect3g= pygame.Rect(153,307,65,44)
Rect4g= pygame.Rect(222,307,65,44)

Rect1h= pygame.Rect(11,261,65,44)
Rect2h= pygame.Rect(84,261,65,44)
Rect3h= pygame.Rect(153,261,65,44)
Rect4h= pygame.Rect(222,261,65,44)

Rect1i= pygame.Rect(11,215,65,44)
Rect2i= pygame.Rect(84,215,65,44)
Rect3i= pygame.Rect(153,215,65,44)
Rect4i= pygame.Rect(222,215,65,44)

Rect1j= pygame.Rect(11,169,65,44)
Rect2j= pygame.Rect(84,169,65,44)
Rect3j= pygame.Rect(153,169,65,44)
Rect4j= pygame.Rect(222,169,65,44)

Rect1k= pygame.Rect(692,578,65,42)
Rect2k= pygame.Rect(756,578,72,42)
Rect3k= pygame.Rect(832,578,72,42)
Rect4k= pygame.Rect(906,578,72,42)

Rect1L= pygame.Rect(692,532,65,46)
Rect2L= pygame.Rect(756,532,72,46)
Rect3L= pygame.Rect(832,532,72,46)
Rect4L= pygame.Rect(906,532,72,46)

Rect1m= pygame.Rect(692,486,65,46)
Rect2m= pygame.Rect(756,486,72,46)
Rect3m= pygame.Rect(832,486,72,46)
Rect4m= pygame.Rect(906,486,72,46)

Rect1n= pygame.Rect(692,440,65,46)
Rect2n= pygame.Rect(756,440,72,46)
Rect3n= pygame.Rect(832,440,72,46)
Rect4n= pygame.Rect(906,440,72,46)

Rect1o= pygame.Rect(692,394,65,46)
Rect2o= pygame.Rect(756,394,72,46)
Rect3o= pygame.Rect(832,394,72,46)
Rect4o= pygame.Rect(906,394,72,46)

Rect1p= pygame.Rect(692,348,65,46)
Rect2p= pygame.Rect(756,348,72,46)
Rect3p= pygame.Rect(832,348,72,46)
Rect4p= pygame.Rect(906,348,72,46)

Rect1q= pygame.Rect(692,302,65,46)
Rect2q= pygame.Rect(756,302,72,46)
Rect3q= pygame.Rect(832,302,72,46)
Rect4q= pygame.Rect(906,302,72,46)

Rect1r= pygame.Rect(692,256,65,46)
Rect2r= pygame.Rect(756,256,72,46)
Rect3r= pygame.Rect(832,256,72,46)
Rect4r= pygame.Rect(906,256,72,46)

Rect1s= pygame.Rect(692,210,65,46)
Rect2s= pygame.Rect(756,210,72,46)
Rect3s= pygame.Rect(832,210,72,46)
Rect4s= pygame.Rect(906,210,72,46)

Rect1t= pygame.Rect(692,164,65,46)
Rect2t= pygame.Rect(756,164,72,46)
Rect3t= pygame.Rect(832,164,72,46)
Rect4t= pygame.Rect(906,164,72,46)

#these are mastercode rects for Single Player game
RectM1= pygame.Rect(12,118,66,45)
RectM2= pygame.Rect(78,118,66,45)
RectM3= pygame.Rect(153,118,66,45)
RectM4= pygame.Rect(227,118,66,45)

#Rect array for multiplayer
rectiq_mp = [MC_rect1,MC_rect2,MC_rect3,MC_rect4,
          MC_rect5,MC_rect6,MC_rect7,MC_rect8,
          Rect1,Rect2,Rect3,Rect4,
          Rect1k,Rect2k,Rect3k,Rect4k,
          Rect1b,Rect2b,Rect3b,Rect4b,
          Rect1L,Rect2L,Rect3L,Rect4L,
          Rect1c,Rect2c,Rect3c,Rect4c,
          Rect1m,Rect2m,Rect3m,Rect4m,
          Rect1d,Rect2d,Rect3d,Rect4d,
          Rect1n,Rect2n,Rect3n,Rect4n,
          Rect1e,Rect2e,Rect3e,Rect4e,
          Rect1o,Rect2o,Rect3o,Rect4o,
          Rect1f,Rect2f,Rect3f,Rect4f,
          Rect1p,Rect2p,Rect3p,Rect4p,
          Rect1g,Rect2g,Rect3g,Rect4g,
          Rect1q,Rect2q,Rect3q,Rect4q,
          Rect1h,Rect2h,Rect3h,Rect4h,
          Rect1r,Rect2r,Rect3r,Rect4r,
          Rect1i,Rect2i,Rect3i,Rect4i,
          Rect1s,Rect2s,Rect3s,Rect4s,
          Rect1j,Rect2j,Rect3j,Rect4j,
          Rect1t,Rect2t,Rect3t,Rect4t]
#Rect array for single player
rectiq_sp = [Rect1,Rect2,Rect3,Rect4,
          Rect1b,Rect2b,Rect3b,Rect4b,
          Rect1c,Rect2c,Rect3c,Rect4c,
          Rect1d,Rect2d,Rect3d,Rect4d,
          Rect1e,Rect2e,Rect3e,Rect4e,
          Rect1f,Rect2f,Rect3f,Rect4f,
          Rect1g,Rect2g,Rect3g,Rect4g,
          Rect1h,Rect2h,Rect3h,Rect4h,
          Rect1i,Rect2i,Rect3i,Rect4i,
          Rect1j,Rect2j,Rect3j,Rect4j,
          RectM1,RectM2,RectM3,RectM4]

#FUNCTIONS USED IN THE PROGRAM       

# 1- Checks which color is clicked
def check_domain(X, Y):
   domain = 0
   if X>520 and X < 677 and Y>444 and Y<540:
      domain = 1
   if X>520 and X < 677 and Y>351 and Y<444:
      domain = 3
   if X>520 and X < 677 and Y>540 and Y<677:
      domain = 2
   if X>520 and X < 677 and Y>253 and Y<351:
      domain = 4
   if X>520 and X < 677 and Y>162 and Y<253:
      domain = 5
   if X>520 and X < 677 and Y>73 and Y<162:
      domain = 6
   return domain

# 2-These blit row functions basically print a row of 1,2,3, or 4 colors depending on the num of arguments they get
A = [0,0,0,0]
def blit_row (x1,x2,x3,x4,row):
   A[0] = x1
   A[1] = x2
   A[2] = x3
   A[3]= x4
   for i in range(4):
      if A[i] == 1:
         screen.blit(ball_1, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 2:
         screen.blit(ball_2, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 3:
         screen.blit(ball_3, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 4:
         screen.blit(ball_4, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 5:
         screen.blit(ball_5, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 6:
         screen.blit(ball_6, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
# 3-
def blit_one(x1,row):
   A[0] = x1
   for i in range(1):
      if A[i] == 1:
         screen.blit(ball_1, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 2:
         screen.blit(ball_2, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 3:
         screen.blit(ball_3, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 4:
         screen.blit(ball_4, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 5:
         screen.blit(ball_5, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 6:
         screen.blit(ball_6, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
# 4-    
def blit_two(x1,x2,row):
   A[0] = x1
   A[1] = x2
   for i in range(2):
      if A[i] == 1:
         screen.blit(ball_1, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 2:
         screen.blit(ball_2, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 3:
         screen.blit(ball_3, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 4:
         screen.blit(ball_4, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 5:
         screen.blit(ball_5, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 6:
         screen.blit(ball_6, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
# 5-
def blit_three(x1,x2,x3,row):
   A[0] = x1
   A[1] = x2
   A[2] = x3
   for i in range(3):
      if A[i] == 1:
         screen.blit(ball_1, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 2:
         screen.blit(ball_2, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 3:
         screen.blit(ball_3, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 4:
         screen.blit(ball_4, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 5:
         screen.blit(ball_5, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
      if A[i] == 6:
         screen.blit(ball_6, (rectiq[i+(row*4)].center[0]-25,rectiq[i+(row*4)].center[1]-25))
#6-
#checks the TOTAL number of correct colors in the user's attempt 
def check_attempt (m1,m2,m3,m4,d1,d2,d3,d4):
   correct_colors = 0
   if m1==d1 or m1 == d2 or m1 == d3 or m1==d4:
      correct_colors = correct_colors+1
   if (m2==d1 and m2 != m1) or (m2 == d2 and m2 != m1)or (m2 == d3 and m2 != m1) or (m2==d4 and m2 != m1):
      correct_colors = correct_colors+1
   if (m3==d1 and (m3 != m1 and m3 != m2)) or (m3 == d2 and (m3 != m1 and m3 != m2))or (m3 == d3 and (m3 != m1 and m3 != m2)) or (m3==d4 and (m3 != m1 and m3 != m2)):
      correct_colors = correct_colors+1
   if (m4==d1 and (m4 != m1 and m4 != m2 and m4 != m3))or (m4 == d2 and (m4 != m1 and m4 != m2 and m4 != m3)) or (m4 == d3 and (m4 != m1 and m4 != m2 and m4 != m3)) or (m4==d4 and (m4 != m1 and m4 != m2 and m4 != m3)):
      correct_colors = correct_colors+1
   return correct_colors
# 7-
#Checks how many balls have been placed EXACTLY WHERE THEY BELONG
def check_color_and_place (m1,m2,m3,m4,d1,d2,d3,d4):
   correct_color_and_place = 0
   if m1==d1:
      correct_color_and_place = correct_color_and_place +1
   if m2==d2:
      correct_color_and_place = correct_color_and_place +1
   if m3==d3:
      correct_color_and_place = correct_color_and_place +1
   if m4==d4:
      correct_color_and_place = correct_color_and_place +1
   return  correct_color_and_place
# 8-
#Function for blitting (printing) the correct number in the second column
def blit_correct_color(num,x_coord,y_coord):
   if num == 0 or num <0:
      screen.blit(zero,(x_coord-30,y_coord-30))
   if num == 1:
      screen.blit(one,(x_coord-30,y_coord-30))
   if num == 2:
      screen.blit(two,(x_coord-30,y_coord-30))
   if num == 3:
      screen.blit(three,(x_coord-30,y_coord-30))
   if num == 4:
      screen.blit(four,(x_coord-30,y_coord-30))
   #print (num)

# 9 -
#Function for blitting (printing) the correct number in the first column
def blit_color_and_place(num,x_coord,y_coord):
   if num == 0:
      screen.blit(zero,(x_coord-30,y_coord-30))
   if num == 1:
      screen.blit(one,(x_coord-30,y_coord-30))
   if num == 2:
      screen.blit(two,(x_coord-30,y_coord-30))
   if num == 3:
      screen.blit(three,(x_coord-30,y_coord-30))
   if num == 4:
      screen.blit(four,(x_coord-30,y_coord-30))
      
# 10 - A very important function
      
#Checks if user attempt has one duplicate color, if so, checks if the duplicates have been placed at their accurate positions
#if so, returns 1, which should be added to the value to be printed in the second column

def check_duplicates_SP(s1,s2,s3,s4):
    M_array=[0,0,0,0]
    duplicates = 0
    duplicate_array=[]
    if Mastercode[0]==s1:
        M_array[0]=1
    if Mastercode[1]==s2:
        M_array[1]=1
    if Mastercode[2]==s3:
        M_array[2]=1
    if Mastercode[3]==s4:
        M_array[3]=1
    correct =0
    for i in range(4):
        if M_array[i]==1:
            correct= correct +1
    
    if correct > 1:
        for i in range(4):
            if M_array[i]==1:
                duplicate_array.append(i)
    if (len(duplicate_array))>1:           
        if (Mastercode[duplicate_array[0]]==Mastercode[duplicate_array[1]]):
            duplicates = 1
    #print("duplicate_array : ",duplicate_array)
    return duplicates
# 11 - Additonal DUPLICATES functions for two player module    
def check_duplicates(s1,s2,s3,s4):
    M_array=[0,0,0,0]
    duplicates = 0
    duplicate_array=[]
    if d_list[0]==s1:
        M_array[0]=1
    if d_list[1]==s2:
        M_array[1]=1
    if d_list[2]==s3:
        M_array[2]=1
    if d_list[3]==s4:
        M_array[3]=1
    correct =0
    for i in range(4):
        if M_array[i]==1:
            correct= correct +1
    
    if correct > 1:
        for i in range(4):
            if M_array[i]==1:
                duplicate_array.append(i)
    if (len(duplicate_array))>1:           
        if (d_list[duplicate_array[0]]==d_list[duplicate_array[1]]):
            duplicates = 1
    return duplicates
# 12-  
def check_duplicates_P2(s1,s2,s3,s4):
    M_array=[0,0,0,0]
    duplicates = 0
    duplicate_array=[]
    if d_list[4]==s1:
        M_array[0]=1
    if d_list[5]==s2:
        M_array[1]=1
    if d_list[6]==s3:
        M_array[2]=1
    if d_list[7]==s4:
        M_array[3]=1
    correct =0
    for i in range(4):
        if M_array[i]==1:
            correct= correct +1
    
    if correct > 1:
        for i in range(4):
            if M_array[i]==1:
                duplicate_array.append(i+4)
    if (len(duplicate_array))>1:           
        if (d_list[duplicate_array[0]]==d_list[duplicate_array[1]]):
            duplicates = 1
    return duplicates


#d_list is a cont. growing list, keeps on recording (and appending to itself) which color the user has clicked on
d_list=[]
WIN = False
WIN2 = False
DRAW = False
#Turn[0] records how many attempts user 1 has made, Turn[1] records no of attempts for user two
Turns=[0,0]
single_player=False
multi_player=False
display_menu=True
#Infinite Loop Starts, will terminate on clicking the cross button
while True:
        if display_menu==True:
            screen.blit(menu,(0,0))
            frames_per_second= FPS
            pygame.display.update()
        #if display_menu==False:
            
            
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type== MOUSEBUTTONDOWN:
                test_coord = pygame.mouse.get_pos()
                test_x= test_coord[0]
                test_y=test_coord[1]
                #print (test_coord)
                if single_player ==False and multi_player==False:
                    if test_x >198 and test_x<264 and test_y>289 and test_y<380:
                        single_player=True
                        #print("SP")
                    if test_x >198 and test_x<264 and test_y>409 and test_y<499:
                        multi_player=True
                        #print("MP")

                    screen.blit(menu,(0,0))
                    frames_per_second= FPS
                    pygame.display.update()
                elif single_player == True:
                        display_menu=False
                        rectiq = rectiq_sp
                        screen.blit(background_sp, (0,0))
                        if test_x > 521 and test_x < 677 and test_y >76 and test_y <630 and WIN==False:
                               bongo.play()
                               domain =check_domain(test_x,test_y)
                               d_list.append(domain)
                               #print (d_list)
                        if WIN == False and len(d_list)>39:
                                lose_music.play()

                        if (len(d_list))>0:
                           blit_one(d_list[0],0)
                        if (len(d_list))>1:
                           blit_two(d_list[0],d_list[1],0)
                        if (len(d_list))>2:
                           blit_three(d_list[0],d_list[1],d_list[2],0)
                        
                        
                        if (len(d_list))>3:
                           blit_row(d_list[0],d_list[1],d_list[2],d_list[3],0)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[0],d_list[1],d_list[2],d_list[3])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[0],d_list[1],d_list[2],d_list[3])
                           blit_color_and_place(correct_color_and_place,354,615)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[0],d_list[1],d_list[2],d_list[3])) ==1:
                               blit_correct_color((difference+1),461,615)
                           else:
                               blit_correct_color(difference,461,615)
                           if correct_color_and_place == 4:
                              WIN = True
                        if (len(d_list))>4:
                           blit_one(d_list[4],1)
                        if (len(d_list))>5:
                           blit_two(d_list[4],d_list[5],1)
                        if (len(d_list))>6:
                           blit_three(d_list[4],d_list[5],d_list[6],1)

                           
                        if (len(d_list))>7:
                           blit_row(d_list[4],d_list[5],d_list[6],d_list[7],1)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[4],d_list[5],d_list[6],d_list[7])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[4],d_list[5],d_list[6],d_list[7])
                           blit_color_and_place(correct_color_and_place,354,566)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[4],d_list[5],d_list[6],d_list[7]))==1:
                               blit_correct_color((difference+1),461,566)
                           else:
                               blit_correct_color(difference,461,566)
                           if correct_color_and_place == 4:
                              WIN = True
                              
                        if (len(d_list))>8:
                           blit_one(d_list[8],2)
                        if (len(d_list))>9:
                           blit_two(d_list[8],d_list[9],2)
                        if (len(d_list))>10:
                           blit_three(d_list[8],d_list[9],d_list[10],2)

                              
                        if (len(d_list))>11:
                           blit_row(d_list[8],d_list[9],d_list[10],d_list[11],2)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[8],d_list[9],d_list[10],d_list[11])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[8],d_list[9],d_list[10],d_list[11])
                           blit_color_and_place(correct_color_and_place,354,521)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[8],d_list[9],d_list[10],d_list[11]))==1:
                               blit_correct_color((difference+1),461,521)
                           else:
                               blit_correct_color(difference,461,521)
                           if correct_color_and_place == 4:
                              WIN = True

                        if (len(d_list))>12:
                           blit_one(d_list[12],3)
                        if (len(d_list))>13:
                           blit_two(d_list[12],d_list[13],3)
                        if (len(d_list))>14:
                           blit_three(d_list[12],d_list[13],d_list[14],3)

                        
                        if (len(d_list))>15:
                           blit_row(d_list[12],d_list[13],d_list[14],d_list[15],3)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[12],d_list[13],d_list[14],d_list[15])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[12],d_list[13],d_list[14],d_list[15])
                           blit_color_and_place(correct_color_and_place,354,472)
                           difference = correct_colors - correct_color_and_place
                           if(check_duplicates_SP(d_list[12],d_list[13],d_list[14],d_list[15]))==1:
                               blit_correct_color((difference+1),461,472)
                           else:
                               blit_correct_color(difference,461,472)
                           if correct_color_and_place == 4:
                              WIN = True


                        if (len(d_list))>16:
                           blit_one(d_list[16],4)
                        if (len(d_list))>17:
                           blit_two(d_list[16],d_list[17],4)
                        if (len(d_list))>18:
                           blit_three(d_list[16],d_list[17],d_list[18],4)

                           
                        if (len(d_list))>19:
                           blit_row(d_list[16],d_list[17],d_list[18],d_list[19],4)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[16],d_list[17],d_list[18],d_list[19])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[16],d_list[17],d_list[18],d_list[19])
                           blit_color_and_place(correct_color_and_place,354,426)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[16],d_list[17],d_list[18],d_list[19]))==1:
                               blit_correct_color((difference+1),461,426)
                           else:
                               blit_correct_color(difference,461,426)
                           if correct_color_and_place == 4:
                              WIN = True

                        if (len(d_list))>20:
                           blit_one(d_list[20],5)
                        if (len(d_list))>21:
                           blit_two(d_list[20],d_list[21],5)
                        if (len(d_list))>22:
                           blit_three(d_list[20],d_list[21],d_list[22],5)

                           
                        if (len(d_list))>23:
                           blit_row(d_list[20],d_list[21],d_list[22],d_list[23],5)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[20],d_list[21],d_list[22],d_list[23])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[20],d_list[21],d_list[22],d_list[23])
                           blit_color_and_place(correct_color_and_place,354,380)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[20],d_list[21],d_list[22],d_list[23]))==1:
                               blit_correct_color((difference+1),461,380)
                           else:
                               blit_correct_color(difference,461,380)
                           
                           if correct_color_and_place == 4:
                              WIN = True

                        if (len(d_list))>24:
                           blit_one(d_list[24],6)
                        if (len(d_list))>25:
                           blit_two(d_list[24],d_list[25],6)
                        if (len(d_list))>26:
                           blit_three(d_list[24],d_list[25],d_list[26],6)

                           
                        if (len(d_list))>27:
                           blit_row(d_list[24],d_list[25],d_list[26],d_list[27],6)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[24],d_list[25],d_list[26],d_list[27])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[24],d_list[25],d_list[26],d_list[27])
                           blit_color_and_place(correct_color_and_place,354,327)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[24],d_list[25],d_list[26],d_list[27]))==1:
                               blit_correct_color((difference+1),461,332)
                           else:
                               blit_correct_color(difference,461,332)
                           if correct_color_and_place == 4:
                              WIN = True
                              
                        if (len(d_list))>28:
                           blit_one(d_list[28],7)
                        if (len(d_list))>29:
                           blit_two(d_list[28],d_list[29],7)
                        if (len(d_list))>30:
                           blit_three(d_list[28],d_list[29],d_list[30],7)

                           
                        if (len(d_list))>31:
                           blit_row(d_list[28],d_list[29],d_list[30],d_list[31],7)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[28],d_list[29],d_list[30],d_list[31])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[28],d_list[29],d_list[30],d_list[31])
                           blit_color_and_place(correct_color_and_place,354,285)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[28],d_list[29],d_list[30],d_list[31]))==1:
                               blit_correct_color((difference+1),461,285)
                           else:
                               blit_correct_color(difference,461,285)
                           if correct_color_and_place == 4:
                              WIN = True

                        if (len(d_list))>32:
                           blit_one(d_list[32],8)
                        if (len(d_list))>33:
                           blit_two(d_list[32],d_list[33],8)
                        if (len(d_list))>34:
                           blit_three(d_list[32],d_list[33],d_list[34],8)

                           
                        if (len(d_list))>35:
                           blit_row(d_list[32],d_list[33],d_list[34],d_list[35],8)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[32],d_list[33],d_list[34],d_list[35])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[32],d_list[33],d_list[34],d_list[35])
                           blit_color_and_place(correct_color_and_place,354,240)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[32],d_list[33],d_list[34],d_list[35]))==1:
                               blit_correct_color((difference+1),461,240)
                           else:
                               blit_correct_color(difference,461,240)
                           if correct_color_and_place == 4:
                              WIN = True

                        if (len(d_list))>36:
                           blit_one(d_list[36],9)
                        if (len(d_list))>37:
                           blit_two(d_list[36],d_list[37],9)
                        if (len(d_list))>38:
                           blit_three(d_list[36],d_list[37],d_list[38],9)


                        if (len(d_list))>39:
                           blit_row(d_list[36],d_list[37],d_list[38],d_list[39],9)
                           correct_colors = check_attempt(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[36],d_list[37],d_list[38],d_list[39])
                           correct_color_and_place = check_color_and_place(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],d_list[36],d_list[37],d_list[38],d_list[39])
                           blit_color_and_place(correct_color_and_place,354,197)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_SP(d_list[36],d_list[37],d_list[38],d_list[39]))==1:
                               blit_correct_color((difference+1),461,197)
                           else:
                               blit_correct_color(difference,461,197)
                           if correct_color_and_place == 4:
                              WIN = True
                           
                        if (len (d_list))>39 and WIN == False:
                            screen.blit(lose, (40,250))
                        if WIN == True:
                           win_music.set_volume(0.30)
                           win_music.play()
                           screen.blit(win, (10,200))
                        if WIN == False and (len (d_list))<40:
                           screen.blit(locked,(8,116))
                        if WIN == True or ((len (d_list))>39 and WIN == False):
                            blit_row(Mastercode[0],Mastercode[1],Mastercode[2],Mastercode[3],10)
                            
                        
                        
                        pygame.display.update()
                        frames_per_sec.tick(FPS)
                elif multi_player == True:
                    display_menu=False
                    rectiq = rectiq_mp
                    screen.blit(background, (0,0))
                    if test_x>521 and test_x < 673 and test_y > 73 and test_y < 627 and len(d_list)<89 and WIN2 ==False and (not(WIN==True and Turns[0]==Turns[1])):
                        bongo.play()
                        domain =check_domain(test_x,test_y)
                        d_list.append(domain)
                    if WIN == False and len(d_list)==84:
                            lose_music.play()
                    if WIN2 == False and len(d_list)>87:
                            lose_music.play()
                    if (len(d_list))>0:
                           blit_one(d_list[0],0)
                    if (len(d_list))>1:
                           blit_two(d_list[0],d_list[1],0)
                    if (len(d_list))>2:
                           blit_three(d_list[0],d_list[1],d_list[2],0)
                        
                        
                    if (len(d_list))>3:
                           blit_row(d_list[0],d_list[1],d_list[2],d_list[3],0)
                           if WIN == False and WIN2 == False and len(d_list)<84:
                               screen.blit(locked,(10,115))
                           
                    if (len(d_list))>4:
                           blit_one(d_list[4],1)
                    if (len(d_list))>5:
                           blit_two(d_list[4],d_list[5],1)
                    if (len(d_list))>6:
                           blit_three(d_list[4],d_list[5],d_list[6],1)

                           
                    if (len(d_list))>7:
                           blit_row(d_list[4],d_list[5],d_list[6],d_list[7],1)
                           if WIN2 == False and len(d_list)<88 and (not(WIN == True and WIN2==False and Turns[0]==Turns[1])):
                              screen.blit(locked,(693,110))

                    if (len(d_list))>8:
                           blit_one(d_list[8],2)
                    if (len(d_list))>9:
                           blit_two(d_list[8],d_list[9],2)
                    if (len(d_list))>10:
                           blit_three(d_list[8],d_list[9],d_list[10],2)

                              
                    if (len(d_list))>11:
                           Turns[0]=1
                           blit_row(d_list[8],d_list[9],d_list[10],d_list[11],2)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[8],d_list[9],d_list[10],d_list[11])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[8],d_list[9],d_list[10],d_list[11])
                           blit_color_and_place(correct_color_and_place,354,615)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[8],d_list[9],d_list[10],d_list[11])) ==1:
                               blit_correct_color((difference+1),461,615)
                           else:
                               blit_correct_color(difference,461,615)
                           if correct_color_and_place == 4:
                              WIN = True

                    if (len(d_list))>12:
                           blit_one(d_list[12],3)
                    if (len(d_list))>13:
                           blit_two(d_list[12],d_list[13],3)
                    if (len(d_list))>14:
                           blit_three(d_list[12],d_list[13],d_list[14],3)

                        
                    if (len(d_list))>15:
                           Turns[1]=1
                           blit_row(d_list[12],d_list[13],d_list[14],d_list[15],3)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[12],d_list[13],d_list[14],d_list[15])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[12],d_list[13],d_list[14],d_list[15])
                           blit_color_and_place(correct_color_and_place,1038,604)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[12],d_list[13],d_list[14],d_list[15])) ==1:
                               blit_correct_color((difference+1),1140,604)
                           else:
                               blit_correct_color(difference,1140,604)
                           if correct_color_and_place == 4:
                              WIN2 = True

                    if (len(d_list))>16:
                           blit_one(d_list[16],4)
                    if (len(d_list))>17:
                           blit_two(d_list[16],d_list[17],4)
                    if (len(d_list))>18:
                           blit_three(d_list[16],d_list[17],d_list[18],4)

                           
                    if (len(d_list))>19:
                           Turns[0]=2
                           blit_row(d_list[16],d_list[17],d_list[18],d_list[19],4)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[16],d_list[17],d_list[18],d_list[19])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[16],d_list[17],d_list[18],d_list[19])
                           blit_color_and_place(correct_color_and_place,354,568)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[16],d_list[17],d_list[18],d_list[19])) ==1:
                               blit_correct_color((difference+1),461,568)
                           else:
                               blit_correct_color(difference,461,568)
                           if correct_color_and_place == 4:
                              WIN = True
                        
                    if (len(d_list))>20:
                           blit_one(d_list[20],5)
                    if (len(d_list))>21:
                           blit_two(d_list[20],d_list[21],5)
                    if (len(d_list))>22:
                           blit_three(d_list[20],d_list[21],d_list[22],5)

                           
                    if (len(d_list))>23:
                           Turns[1]=2
                           blit_row(d_list[20],d_list[21],d_list[22],d_list[23],5)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[20],d_list[21],d_list[22],d_list[23])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[20],d_list[21],d_list[22],d_list[23])
                           blit_color_and_place(correct_color_and_place,1038,557)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[20],d_list[21],d_list[22],d_list[23])) ==1:
                               blit_correct_color((difference+1),1140,557)
                           else:
                               blit_correct_color(difference,1140,557)
                           if correct_color_and_place == 4:
                              WIN2 = True
                           
                    if (len(d_list))>24:
                           blit_one(d_list[24],6)
                    if (len(d_list))>25:
                           blit_two(d_list[24],d_list[25],6)
                    if (len(d_list))>26:
                           blit_three(d_list[24],d_list[25],d_list[26],6)

                           
                    if (len(d_list))>27:
                           Turns[0]=3
                           blit_row(d_list[24],d_list[25],d_list[26],d_list[27],6)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[24],d_list[25],d_list[26],d_list[27])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[24],d_list[25],d_list[26],d_list[27])
                           blit_color_and_place(correct_color_and_place,354,521)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[24],d_list[25],d_list[26],d_list[27])) ==1:
                               blit_correct_color((difference+1),461,521)
                           else:
                               blit_correct_color(difference,461,521)
                           if correct_color_and_place == 4:
                              WIN = True

                    if (len(d_list))>28:
                           blit_one(d_list[28],7)
                    if (len(d_list))>29:
                           blit_two(d_list[28],d_list[29],7)
                    if (len(d_list))>30:
                           blit_three(d_list[28],d_list[29],d_list[30],7)

                           
                    if (len(d_list))>31:
                           Turns[1]=3
                           blit_row(d_list[28],d_list[29],d_list[30],d_list[31],7)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[28],d_list[29],d_list[30],d_list[31])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[28],d_list[29],d_list[30],d_list[31])
                           blit_color_and_place(correct_color_and_place,1038,510)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[28],d_list[29],d_list[30],d_list[31])) ==1:
                               blit_correct_color((difference+1),1140,510)
                           else:
                               blit_correct_color(difference,1140,510)
                           if correct_color_and_place == 4:
                              WIN2 = True
                           
                    if (len(d_list))>32:
                           blit_one(d_list[32],8)
                    if (len(d_list))>33:
                           blit_two(d_list[32],d_list[33],8)
                    if (len(d_list))>34:
                           blit_three(d_list[32],d_list[33],d_list[34],8)

                           
                    if (len(d_list))>35:
                           Turns[0]=4
                           blit_row(d_list[32],d_list[33],d_list[34],d_list[35],8)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[32],d_list[33],d_list[34],d_list[35])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[32],d_list[33],d_list[34],d_list[35])
                           blit_color_and_place(correct_color_and_place,354,474)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[32],d_list[33],d_list[34],d_list[35])) ==1:
                               blit_correct_color((difference+1),461,474)
                           else:
                               blit_correct_color(difference,461,474)
                           if correct_color_and_place == 4:
                              WIN = True
                           
                    if (len(d_list))>36:
                           blit_one(d_list[36],9)
                    if (len(d_list))>37:
                           blit_two(d_list[36],d_list[37],9)
                    if (len(d_list))>38:
                           blit_three(d_list[36],d_list[37],d_list[38],9)


                    if (len(d_list))>39:
                           Turns[1]=4
                           blit_row(d_list[36],d_list[37],d_list[38],d_list[39],9)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[36],d_list[37],d_list[38],d_list[39])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[36],d_list[37],d_list[38],d_list[39])
                           blit_color_and_place(correct_color_and_place,1038,463)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[36],d_list[37],d_list[38],d_list[39])) ==1:
                               blit_correct_color((difference+1),1140,463)
                           else:
                               blit_correct_color(difference,1140,463)
                           if correct_color_and_place == 4:
                              WIN2 = True   
                           
                    if (len(d_list))>40:
                           blit_one(d_list[40],10)
                    if (len(d_list))>41:
                           blit_two(d_list[40],d_list[41],10)
                    if (len(d_list))>42:
                           blit_three(d_list[40],d_list[41],d_list[42],10)
                        
                        
                    if (len(d_list))>43:
                           Turns[0]=5
                           blit_row(d_list[40],d_list[41],d_list[42],d_list[43],10)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[40],d_list[41],d_list[42],d_list[43])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[40],d_list[41],d_list[42],d_list[43])
                           blit_color_and_place(correct_color_and_place,354,427)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[40],d_list[41],d_list[42],d_list[43])) ==1:
                               blit_correct_color((difference+1),461,427)
                           else:
                               blit_correct_color(difference,461,427)
                           if correct_color_and_place == 4:
                              WIN = True
                          
                    if (len(d_list))>44:
                           blit_one(d_list[44],11)
                    if (len(d_list))>45:
                           blit_two(d_list[44],d_list[45],11)
                    if (len(d_list))>46:
                           blit_three(d_list[44],d_list[45],d_list[46],11)

                           
                    if (len(d_list))>47:
                           Turns[1]=5
                           blit_row(d_list[44],d_list[45],d_list[46],d_list[47],11)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[44],d_list[45],d_list[46],d_list[47])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[44],d_list[45],d_list[46],d_list[47])
                           blit_color_and_place(correct_color_and_place,1038,416)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[44],d_list[45],d_list[46],d_list[47])) ==1:
                               blit_correct_color((difference+1),1140,416)
                           else:
                               blit_correct_color(difference,1140,416)
                           if correct_color_and_place == 4:
                              WIN2 = True
                          
                    if (len(d_list))>48:
                           blit_one(d_list[48],12)
                    if (len(d_list))>49:
                           blit_two(d_list[48],d_list[49],12)
                    if (len(d_list))>50:
                           blit_three(d_list[48],d_list[49],d_list[50],12)

                              
                    if (len(d_list))>51:
                           Turns[0]=6
                           blit_row(d_list[48],d_list[49],d_list[50],d_list[51],12)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[48],d_list[49],d_list[50],d_list[51])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[48],d_list[49],d_list[50],d_list[51])
                           blit_color_and_place(correct_color_and_place,354,380)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[48],d_list[49],d_list[50],d_list[51])) ==1:
                               blit_correct_color((difference+1),461,380)
                           else:
                               blit_correct_color(difference,461,380)
                           if correct_color_and_place == 4:
                              WIN = True

                    if (len(d_list))>52:
                           blit_one(d_list[52],13)
                    if (len(d_list))>53:
                           blit_two(d_list[52],d_list[53],13)
                    if (len(d_list))>54:
                           blit_three(d_list[52],d_list[53],d_list[54],13)

                        
                    if (len(d_list))>55:
                           Turns[1]=6
                           blit_row(d_list[52],d_list[53],d_list[54],d_list[55],13)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[52],d_list[53],d_list[54],d_list[55])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[52],d_list[53],d_list[54],d_list[55])
                           blit_color_and_place(correct_color_and_place,1038,369)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[52],d_list[53],d_list[54],d_list[55])) ==1:
                               blit_correct_color((difference+1),1140,369)
                           else:
                               blit_correct_color(difference,1140,369)
                           if correct_color_and_place == 4:
                              WIN2 = True

                    if (len(d_list))>56:
                           blit_one(d_list[56],14)
                    if (len(d_list))>57:
                           blit_two(d_list[56],d_list[57],14)
                    if (len(d_list))>58:
                           blit_three(d_list[56],d_list[57],d_list[58],14)

                           
                    if (len(d_list))>59:
                           Turns[0]=7
                           blit_row(d_list[56],d_list[57],d_list[58],d_list[59],14)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[56],d_list[57],d_list[58],d_list[59])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[56],d_list[57],d_list[58],d_list[59])
                           blit_color_and_place(correct_color_and_place,354,333)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[56],d_list[57],d_list[58],d_list[59])) ==1:
                               blit_correct_color((difference+1),461,333)
                           else:
                               blit_correct_color(difference,461,333)
                           if correct_color_and_place == 4:
                              WIN = True

                    if (len(d_list))>60:
                           blit_one(d_list[60],15)
                    if (len(d_list))>61:
                           blit_two(d_list[60],d_list[61],15)
                    if (len(d_list))>62:
                           blit_three(d_list[60],d_list[61],d_list[62],15)

                           
                    if (len(d_list))>63:
                           Turns[1]=7
                           blit_row(d_list[60],d_list[61],d_list[62],d_list[63],15)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[60],d_list[61],d_list[62],d_list[63])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[60],d_list[61],d_list[62],d_list[63])
                           blit_color_and_place(correct_color_and_place,1038,322)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[60],d_list[61],d_list[62],d_list[63])) ==1:
                               blit_correct_color((difference+1),1140,322)
                           else:
                               blit_correct_color(difference,1140,322)
                           if correct_color_and_place == 4:
                              WIN2 = True
                        
                    if (len(d_list))>64:
                           blit_one(d_list[64],16)
                    if (len(d_list))>65:
                           blit_two(d_list[64],d_list[65],16)
                    if (len(d_list))>66:
                           blit_three(d_list[64],d_list[65],d_list[66],16)

                           
                    if (len(d_list))>67:
                           Turns[0]=8
                           blit_row(d_list[64],d_list[65],d_list[66],d_list[67],16)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[64],d_list[65],d_list[66],d_list[67])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[64],d_list[65],d_list[66],d_list[67])
                           blit_color_and_place(correct_color_and_place,354,286)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[64],d_list[65],d_list[66],d_list[67])) ==1:
                               blit_correct_color((difference+1),461,286)
                           else:
                               blit_correct_color(difference,461,286)
                           if correct_color_and_place == 4:
                              WIN = True
                           
                    if (len(d_list))>68:
                           blit_one(d_list[68],17)
                    if (len(d_list))>69:
                           blit_two(d_list[68],d_list[69],17)
                    if (len(d_list))>70:
                           blit_three(d_list[68],d_list[69],d_list[70],17)

                           
                    if (len(d_list))>71:
                           Turns[1]=8
                           blit_row(d_list[68],d_list[69],d_list[70],d_list[71],17)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[68],d_list[69],d_list[70],d_list[71])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[68],d_list[69],d_list[70],d_list[71])
                           blit_color_and_place(correct_color_and_place,1038,275)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[68],d_list[69],d_list[70],d_list[71])) ==1:
                               blit_correct_color((difference+1),1140,275)
                           else:
                               blit_correct_color(difference,1140,275)
                           if correct_color_and_place == 4:
                              WIN2 = True

                    if (len(d_list))>72:
                           blit_one(d_list[72],18)
                    if (len(d_list))>73:
                           blit_two(d_list[72],d_list[73],18)
                    if (len(d_list))>74:
                           blit_three(d_list[72],d_list[73],d_list[74],18)

                           
                    if (len(d_list))>75:
                           Turns[0]=9
                           blit_row(d_list[72],d_list[73],d_list[74],d_list[75],18)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[72],d_list[73],d_list[74],d_list[75])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[72],d_list[73],d_list[74],d_list[75])
                           blit_color_and_place(correct_color_and_place,354,239)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[72],d_list[73],d_list[74],d_list[75])) ==1:
                               blit_correct_color((difference+1),461,239)
                           else:
                               blit_correct_color(difference,461,239)
                           if correct_color_and_place == 4:
                              WIN = True
                          

                    if (len(d_list))>76:
                           blit_one(d_list[76],19)
                    if (len(d_list))>77:
                           blit_two(d_list[76],d_list[77],19)
                    if (len(d_list))>78:
                           blit_three(d_list[76],d_list[77],d_list[78],19)


                    if (len(d_list))>79:
                           Turns[1]=9
                           blit_row(d_list[76],d_list[77],d_list[78],d_list[79],19)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[76],d_list[77],d_list[78],d_list[79])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[76],d_list[77],d_list[78],d_list[79])
                           blit_color_and_place(correct_color_and_place,1038,228)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[76],d_list[77],d_list[78],d_list[79])) ==1:
                               blit_correct_color((difference+1),1140,228)
                           else:
                               blit_correct_color(difference,1140,228)
                           if correct_color_and_place == 4:
                              WIN2 = True

                    if (len(d_list))>80:
                           blit_one(d_list[80],20)
                           if (len(d_list))>81:
                              blit_two(d_list[80],d_list[81],20)
                           if (len(d_list))>82:
                              blit_three(d_list[80],d_list[81],d_list[82],20)


                    if (len(d_list))>83:
                           Turns[0]=10
                           blit_row(d_list[80],d_list[81],d_list[82],d_list[83],20)
                           correct_colors = check_attempt(d_list[0],d_list[1],d_list[2],d_list[3],d_list[80],d_list[81],d_list[82],d_list[83])
                           correct_color_and_place = check_color_and_place(d_list[0],d_list[1],d_list[2],d_list[3],d_list[80],d_list[81],d_list[82],d_list[83])
                           blit_color_and_place(correct_color_and_place,354,192)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates(d_list[80],d_list[81],d_list[82],d_list[83])) ==1:
                               blit_correct_color((difference+1),461,192)
                           else:
                               blit_correct_color(difference,461,192)
                           if correct_color_and_place == 4:
                              WIN = True
                        
                    if (len(d_list))>84:
                           blit_one(d_list[84],21)
                    if (len(d_list))>85:
                           blit_two(d_list[84],d_list[85],21)
                    if (len(d_list))>86:
                           blit_three(d_list[84],d_list[85],d_list[86],21)


                    if (len(d_list))>87:
                           Turns[1]=10
                           blit_row(d_list[84],d_list[85],d_list[86],d_list[87],21)
                           correct_colors = check_attempt(d_list[4],d_list[5],d_list[6],d_list[7],d_list[84],d_list[85],d_list[86],d_list[87])
                           correct_color_and_place = check_color_and_place(d_list[4],d_list[5],d_list[6],d_list[7],d_list[84],d_list[85],d_list[86],d_list[87])
                           blit_color_and_place(correct_color_and_place,1038,181)
                           difference = correct_colors - correct_color_and_place
                           if (check_duplicates_P2(d_list[84],d_list[85],d_list[86],d_list[87])) ==1:
                               blit_correct_color((difference+1),1140,181)
                           else:
                               blit_correct_color(difference,1140,181)
                           if correct_color_and_place == 4:
                              WIN2 = True
                              
                    if WIN == True and WIN2==True and Turns[0]==Turns[1]:
                            DRAW= True
                            screen.blit(draw,(450,300))
                    elif WIN == True and Turns[0]==Turns[1]:
                            screen.blit(win, (10,200))
                            win_music.set_volume(0.30)
                            win_music.play()
                    elif WIN2 == True and Turns[0]==Turns[1]:
                               screen.blit(win, (700,200))
                               win_music.set_volume(0.30)
                               win_music.play()

                    if (len (d_list))>83 and WIN == False:
                           screen.blit(lose, (40,250))
                    if (len (d_list))>87 and WIN2 == False:
                           screen.blit(lose, (730,250))
                        
                    pygame.display.update()
                    frames_per_sec.tick(FPS)
        





                                        
                                        
                                    




