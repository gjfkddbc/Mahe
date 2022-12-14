import random #random 함수 불러옴.
import pygame
from pygame.locals import *
import os

dice=[0,0,0]
pygame.init() # 초기화

turn = d1 = d2 = d3 = 0
scoreb=0
mode = 0

current_path = os.path.dirname(__file__) # img파일에서 이미지 불러오기 
image_path = os.path.join(current_path, "img")

size=[1080,720] # 창 크기 설정
screen=pygame.display.set_mode(size) 

title="MAHE" # 창 이름 설정
pygame.display.set_caption(title)

icon= pygame.image.load(os.path.join(image_path,"icon.png")).convert_alpha() # icon 생성
pygame.display.set_icon(icon)

clock=pygame.time.Clock() # 시계

Font = pygame.font.SysFont("arial",30,True,False)
BLACK = (0,0,0)
text_Title1 = Font.render("Press the Enter",True,BLACK)
text_Title2 = Font.render("Throw                     Stop",True,BLACK)
text_Title3 = Font.render("Space                     Enter",True,BLACK)
SCREEN_WIDTH=size[0]
SCREEN_HEIGHT=size[1]
ThrowStartY = SCREEN_HEIGHT-200
isClick = 0 #스페이스가 눌렸는지 확인하는 변수
yCurr = SCREEN_HEIGHT/2 #y 좌표 값
diceCurr = 0 #현재 표현하는 주사위 눈
ThrowEndY = 400 # y 한계값
playertime = 0

turn_text = Font.render(str(turn), True, BLACK)
d1_text = Font.render(str(d1), True, BLACK)
d2_text = Font.render(str(d2), True, BLACK)
d3_text = Font.render(str(d3), True, BLACK)






class COM():#computer의 클래스
    def __init__(self, probability=0.0): #기본 정보(이름, 점수, 위치, 확률)
        self.score = 0
        self.position = 0
        self.probability = probability
        
    def play(self): #주사위 던짐
        dice=[0,0,0]
        dice = self.throw_dice()     
        self.move(dice)
        
    def throw_dice(self):
        global isClick, d1, d2, d3, mode
        isClick = 1

        if mode==3:
            d1 = d2 = d3 = 0
            d1 = clickProcess()
            p = (7-d1) / 6.0
            if self.position<=4:
                self.probability=3/6
            elif self.position>=16:
                self.probability=5/6
            else: self.probability=4/6
            if p>=self.probability:
                d2 = random.randint(1, 6)
                p = (7 - d1 - d2) / 6.0
                if p>=self.probability:
                    d3 = random.randint(1, 6)
        elif mode==2:
            d1 = clickProcess()
            p = (7-d1) / 6.0
            self.probability=4/6
            if p>=self.probability:
                d2 = random.randint(1, 6)
                p = (7 - d1 - d2) / 6.0
                if p>=self.probability:
                    d3 = random.randint(1, 6)
        elif mode==1:
            d1 = clickProcess()
            if random.randint(0, 1)==1:
                d2 = random.randint(1, 6)
                if random.randint(0, 1)==1:
                    d3 = random.randint(1, 6)
        
        return (d1, d2, d3)
    
    def move(self, dice):
        global scoreb
        step = 0
        if 7 < dice[0] + dice[1] + dice[2]:
            self.position = 0
        elif dice[2]!=0:
            step = (dice[0] + dice[1] + dice[2]) * 3
        elif dice[1]!=0:
            step = (dice[0] + dice[1]) * 2
        else:
            step = dice[0]
            
        self.position += step
        if self.position == 21:
            self.score += 1 
            scoreb=1
        if scoreb == 0:
            if self.position > 21:
                self.score += 1 
        if scoreb == 1:
            if self.position > 21:
                scoreb = 0
        if self.position > 21:
            self.position -= 21
 


class PLAYER():#player의 클래스
    def __init__(self):
        self.score = 0
        self.position = 0
         
    def play1(self): #주사위 던짐
        global dice
        dice = [0,0,0]
        dice[0] = self.throw_dice()

    def play2(self):
        global dice
        dice[1] = self.throw_dice2()

    def play3(self):
        global dice
        dice[2] = self.throw_dice3()     
        
    def throw_dice(self):
        global isClick, d1, d2, d3
        isClick = 1
        d1 = d2 = d3 = 0
        d1 = clickProcess()
        return (d1)
            
    def throw_dice2(self):
        global isClick, d2
        isClick = 1
        d2  = 0
        d2 = clickProcess()
        return (d2)

    def throw_dice3(self):
        global isClick, d3
        isClick = 1
        d3 = 0
        d3 = clickProcess()
        return (d3)
    
    def move(self, dice):
        global scoreb
        step = 0
        if 7 < dice[0] + dice[1] + dice[2]:
            self.position = 0
        elif dice[2]!=0:
            step = (dice[0] + dice[1] + dice[2]) * 3
        elif dice[1]!=0:
            step = (dice[0] + dice[1]) * 2
        else:
            step = dice[0]
            
        self.position += step
        if self.position == 21:
            self.score += 1 
            scoreb=1
        if scoreb == 0:
            if self.position > 21:
                self.score += 1 
        if scoreb == 1:
            if self.position > 21:
                scoreb = 0
        if self.position > 21:
            self.position -= 21


             

class Dice(): #주사위 클래스
    def __init__(self,idx,y):
        self.image = pygame.image.load(os.path.join(image_path,f"{idx}.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image,(80,80))
        self.x = SCREEN_WIDTH/2-(self.image.get_width()/2)
        self.y=y
        self.angle=0
        self.rotated_image = pygame.transform.rotate(self.image, self.angle)#회전 이미지
        
    def rotate(self,angle=None): #회전 각도
        if angle !=None:
            self.angle=0
        else:
            self.angle = random.randint(0,360) #각도를 랜덤으로
        self.rotated_image = pygame.transform.rotate(self.image, self.angle) #돌린 이미지 출력
        
    def draw(self): #이미지 그리기
        screen.fill(sea)
        main_island.show ()
        island1.show()
        island2.show()
        island3.show()
        island4.show()
        island5.show()
        island6.show()
        island7.show()
        island8.show()
        island9.show()
        island10.show()
        island11.show()
        island12.show()
        island13.show()
        island14.show()
        island15.show()
        island16.show()
        island17.show()
        island18.show()
        island19.show()
        island20.show()
        island21.show()
        raft.show()
        turtle1.show()
        turtle2.show()


        #점수 관련 변수
        s = str(c.score)
        text_color = (255, 255, 255)
        font = pygame.font.SysFont("arial", 30)
        s_text = font.render(f'computer: {s}', True, text_color)


        #점수 관련 변수
        b = str(p.score)
        text_color = (255, 255, 255)
        font = pygame.font.SysFont("arial", 30)
        b_text = font.render(f'player: {b}', True, text_color)

        screen.blit(s_text,(30,0))
        screen.blit(b_text,(950,0))

        d1_text = Font.render(str(d1), True, BLACK)
        screen.blit(d1_text,(600,0))
        d2_text = Font.render(str(d2), True, BLACK)
        screen.blit(d2_text,(700,0))
        d3_text = Font.render(str(d3), True, BLACK)
        screen.blit(d3_text,(800,0))

        first = Font.render('1', True, BLACK)
        screen.blit(first,(563,620))


        screen.blit(self.rotated_image, (self.x + self.image.get_width() / 2 - self.rotated_image.get_width() / 2, self.y + self.image.get_height() / 2 - self.rotated_image.get_height() / 2))
        
        if turn % 2 == 0:
            if isClick == 0:
                screen.blit(text_Title1,(450,110))
        elif turn % 2 == 1:
            if isClick == 0:
                if playertime == 0 or playertime == 3:
                    screen.blit(text_Title1,(450,110))
                else:
                    screen.blit(text_Title2,(390,100))
                    screen.blit(text_Title3,(390,140))
        if mode==0:
            Normal.show()
            Easy.show()
            Hard.show()

        if p.score+c.score>=21:
            if p.score > c.score:
                win.show()
            if p.score < c.score:
                lose.show()

        pygame.display.flip()


dices = [Dice(i,ThrowStartY) for i in range(0,5+1)]


def diceshow():
    global isClick, diceCurr
    diceCurr = random.randint(0,len(dices)-1)

    dices[diceCurr].y=yCurr
    dices[diceCurr].rotate()
    if isClick==0:
        dices[diceCurr].rotate(angle=0)
    dices[diceCurr].draw()

def clickProcess(): #주사위 던지기
    global isClick, diceCurr, yCurr
    while isClick == 1: # space bar : 위로 던질때
        diceshow()
        yCurr-=5
        if yCurr <= ThrowEndY: # 최고 높이가 되었을 때 낙하 시작
            isClick=2
    while isClick==2: # 최고 높이 도달, 떨어질 때
        yCurr+=5
        diceshow()
        if yCurr>=ThrowStartY : # 바닥에 닿았을 때
            isClick = 0 # 키 눌림을 초기화
            break;
    #완료 및 아무것도 안할 때
    yCurr = ThrowStartY
    dices[diceCurr].rotate(angle=0)
    dices[diceCurr].draw()
    return diceCurr + 1
    #주사위 최종 값:dices[diceCurr]

class obj:
    def _init_(self): # 위치 초기화
        self.x = 0
        self.y = 0
        self.move = 0   
    def put_img(self, address): # 이미지 삽입
        if address[-3:] == "png":
            self.img = pygame.image.load(os.path.join(image_path,address)).convert_alpha()
        else:
            self.img = pygame.image.load(os.path.join(image_path,address))
        self.sx, self.sy = self.img.get_size()
    def change_size(self, sx, sy): # 크기 변화
        self.img=pygame.transform.scale(self.img,(sx,sy))
        self.sx, self.sy = self.img.get_size()
    def rotate(self, degree): # 회전
        self.img=pygame.transform.rotate(self.img, degree)
    def show(self): # 화면에 띄우기
            screen.blit(self.img,(self.x,self.y))

c = COM(2/3)
p = PLAYER()


island_sx = 135
island_sy = 90
island_x = [563, 683, 783, 903, 930, 930, 903, 843, 703, 548, 398, 248, 103, 43, 16, 15, 33, 73, 143, 283, 423]
island_y = [620, 575, 440, 400, 350, 250, 155, 70, 30, 15, 15, 30, 70, 155, 250, 350, 440, 530, 610, 625, 625]


island1=obj()
island1.put_img("island.png")
island1.change_size (island_sx, island_sy)
island1.x=round(size[0]/2-island_sx/2+90)
island1.y=size[1]-island_sy-10

island2=obj()
island2.put_img("island.png")
island2.change_size (island_sx, island_sy)
island2.x=round(size[0]/2-island_sx/2+210)
island2.y=size[1]-island_sy-55

island3=obj()
island3.put_img("island.png")
island3.change_size (island_sx, island_sy)
island3.x=round(size[0]/2-island_sx/2+310)
island3.y=size[1]-island_sy-130

island4=obj()
island4.put_img("island.png")
island4.change_size (island_sx, island_sy)
island4.x=round(size[0]/2-island_sx/2+430) 
island4.y=size[1]-island_sy-190

island5=obj()
island5.put_img("island.png")
island5.change_size (island_sx, island_sy)
island5.x=size[0]-island_sx-15
island5.y=size[1]-island_sy-280

island6=obj()
island6.put_img("island.png")
island6.change_size (island_sx, island_sy)
island6.x=round(size[0]/2-island_sx/2+457) 
island6.y=size[1]-island_sy-380

island7=obj()
island7.put_img("island.png")
island7.change_size (island_sx, island_sy)
island7.x=round(size[0]/2-island_sx/2+430)
island7.y=size[1]-island_sy-475

island8=obj()
island8.put_img("island.png")
island8.change_size (island_sx, island_sy)
island8.x=round(size[0]/2-island_sx/2+370)
island8.y=70

island9=obj()
island9.put_img("island.png")
island9.change_size (island_sx, island_sy)
island9.x=round(size[0]/2-island_sx/2+230)
island9.y=30

island10=obj()
island10.put_img("island.png")
island10.change_size (island_sx, island_sy)
island10.x=round(size[0]/2-island_sx/2+75)
island10.y=15 

island11=obj()
island11.put_img("island.png")
island11.change_size (island_sx, island_sy)
island11.x=round(size[0]/2-island_sx/2-75)
island11.y=15

island12=obj()
island12.put_img("island.png")
island12.change_size (island_sx, island_sy)
island12.x=round(size[0]/2-island_sx/2-230)
island12.y=30

island13=obj()
island13.put_img("island.png")
island13.change_size (island_sx, island_sy)
island13.x=round(size[0]/2-island_sx/2-370)
island13.y=70

island14=obj()
island14.put_img("island.png")
island14.change_size (island_sx, island_sy)
island14.x=round(size[0]/2-island_sx/2-430)
island14.y=size[1]-island_sy-475

island15=obj()
island15.put_img("island.png")
island15.change_size (island_sx, island_sy)
island15.x=round(size[0]/2-island_sx/2-457)
island15.y=size[1]-island_sy-380

island16=obj()
island16.put_img("island.png")
island16.change_size (island_sx, island_sy)
island16.x=15
island16.y=size[1]-island_sy-280

island17=obj()
island17.put_img("island.png")
island17.change_size (island_sx, island_sy)
island17.x=round(size[0]/2-island_sx/2-440)
island17.y=size[1]-island_sy-190

island18=obj()
island18.put_img("island.png")
island18.change_size (island_sx, island_sy)
island18.x=round(size[0]/2-island_sx/2-400)
island18.y=size[1]-island_sy-100

island19=obj()
island19.put_img("island.png")
island19.change_size (island_sx, island_sy)
island19.x=round(size[0]/2-island_sx/2-330)
island19.y=size[1]-island_sy-20

island20=obj()
island20.put_img("island.png")
island20.change_size (island_sx, island_sy)
island20.x=round(size[0]/2-island_sx/2-190)
island20.y=size[1]-island_sy-5

island21=obj()
island21.put_img("island.png")
island21.change_size (island_sx, island_sy)
island21.x=round(size[0]/2-island_sx/2-50)
island21.y=size[1]-island_sy-5

main_island=obj()
main_island.put_img("main_island.png")
main_island.change_size (800, 400)
main_island.x=round(size[0]/2-main_island.sx/2)
main_island.y=round(size[1]/2-main_island.sy/2)

raft=obj()
raft.put_img("raft.png")
raft.change_size(300,220)
raft.x=size[0]-raft.sx+20
raft.y=size[1]-raft.sy+20

turtle1=obj()
turtle1.put_img("turtle1.png")
turtle1.change_size(120,150)
turtle1.rotate(90)
turtle1.x=size[0]-turtle1.sx-60
turtle1.y=size[1]-turtle1.sy-60
turtle1.move=5

turtle2=obj()
turtle2.put_img("turtle2.png")
turtle2.change_size(120,150)
turtle2.rotate(90)
turtle2.x=size[0]-turtle2.sx-30
turtle2.y=size[1]-turtle2.sy

win=obj()
win.put_img("ending_win.png")
win.change_size(1000,640)
win.x=40
win.y=40

lose=obj()
lose.put_img("ending_lose.png")
lose.change_size(1000,640)
lose.x=40
lose.y=40

Easy=obj()
Easy.put_img("Button_Easy.png")
Easy.change_size(300,130)
Easy.x=30
Easy.y=400

Hard=obj()
Hard.put_img("Button_Hard.png")
Hard.change_size(300,130)
Hard.x=size[0]-Hard.sx-30
Hard.y=400

Normal=obj()
Normal.put_img("Button_Normal.png")
Normal.change_size(300,130)
Normal.x=round((size[0]-Normal.sx)/2)
Normal.y=400


black=(0,0,0)
white=(255,255,255)
sea=(0,162,232)

SB=0
while SB==0:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            SB=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 400<=pygame.mouse.get_pos()[1]<=530:
                if Easy.x<=pygame.mouse.get_pos()[0]<=Easy.x+400:
                    mode=1
                if Normal.x<=pygame.mouse.get_pos()[0]<=Normal.x+400:
                    mode=2
                if Hard.x<=pygame.mouse.get_pos()[0]<=Hard.x+400:
                    mode=3
        if (event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN):
            if isClick == 0:
                if turn % 2 == 0:
                    c.play()
                    turn+=1
                    if c.position!=0:
                        turtle1.x = island_x[c.position-1]
                        turtle1.y = island_y[c.position-1]
                    elif c.position==0:
                        turtle1.x = raft.x + 70
                        turtle1.y = raft.y

                elif turn % 2 == 1:
                    if playertime == 0:
                        p.play1()
                        playertime = 1
                    elif playertime > 0:
                        p.move(dice)
                        turn+=1
                        playertime = 0
                        if p.position!=0:
                            turtle2.x = island_x[p.position-1]-5
                            turtle2.y = island_y[p.position-1]-5
                        elif p.position==0:
                           turtle2.x = raft.x + 90
                           turtle2.y = raft.y + 5
        if (event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
            if isClick == 0:
                if turn % 2 == 1:
                    if playertime == 1:
                        p.play2()
                        playertime = 2
                    elif playertime == 2:
                        p.play3()
                        playertime=3
             
    dices[diceCurr].draw()


pygame.quit()