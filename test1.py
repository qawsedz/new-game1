import pygame
from random import*
from math import*
from pickle import*
import os
def load_all_pickle(filename):
    data = []
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            try:
                while True:
                    data.append(load(f))
            except EOFError:
                pass
    return max(data)



def run():
    f222=open("t1","ab")

    pygame.init()
    sc=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    
    class car:
        def __init__(self,pos):
            self.pos=pos
            self.score=randint(1,50)
            self.rect=pygame.Rect(self.pos[0],self.pos[1],100,50)
            self.img=pygame.transform.scale(pygame.image.load("PNG/Cars/ambulance.png PNG/Cars/buggy.png PNG/Cars/bus_school.png PNG/Cars/bus.png PNG/Cars/convertible.png PNG/Cars/cycle_low.png PNG/Cars/cycle.png PNG/Cars/firetruck.png PNG/Cars/formula.png PNG/Cars/hotdog.png PNG/Cars/kart.png PNG/Cars/police.png PNG/Cars/riot.png PNG/Cars/rounded_green.png PNG/Cars/rounded_red.png PNG/Cars/rounded_yellow.png PNG/Cars/scooter.png PNG/Cars/sedan_blue.png PNG/Cars/sedan_vintage.png PNG/Cars/sedan.png PNG/Cars/sports_convertible.png PNG/Cars/sports_green.png PNG/Cars/sports_race.png PNG/Cars/sports_red.png PNG/Cars/sports_yellow.png PNG/Cars/station.png PNG/Cars/suv_closed.png PNG/Cars/suv_green.png PNG/Cars/suv_large.png PNG/Cars/suv_military.png PNG/Cars/suv_travel.png PNG/Cars/suv.png PNG/Cars/taxi.png PNG/Cars/towtruck.png PNG/Cars/tractor.png PNG/Cars/transport.png PNG/Cars/truck_trailer.png PNG/Cars/truck.png PNG/Cars/truckcabin_vintage.png PNG/Cars/truckcabin.png PNG/Cars/truckdark.png PNG/Cars/truckdelivery.png PNG/Cars/trucktank_trailer.png PNG/Cars/trucktank.png PNG/Cars/van_flat.png PNG/Cars/van_large.png PNG/Cars/van_small.png PNG/Cars/van.png PNG/Cars/vendor.png PNG/Cars/vintage.png".split(" ")[self.score-1]),(100,50)).convert_alpha()
        def draw(self):
            self.pos[0]-=p.s
            if -50<=self.pos[0]<=1930:
                self.rect=pygame.Rect(self.pos[0],self.pos[1],100,50)
                sc.blit(self.img,(self.pos[0],self.pos[1]))
    class cars:
        def __init__(self):
            self.list1=[]
        def add(self,x1):
            self.list1.append(x1)
        def draw(self):
            for i in self.list1:
                i.draw()

    c1=cars()
    class fire:
        def __init__(self,pos,dir):
            self.img=pygame.transform.flip(pygame.transform.scale(pygame.image.load("PNG/Default size/tank_bullet"+str(randint(1,6))+".png").convert_alpha(),(50,30)),dir<0,0)
            self.dir=dir
            self.pos=pos
            self.t=0
            self.img1=pygame.image.load("PNG/Default size/tank_explosion4.png")
        def draw(self):
            self.rect=pygame.Rect(self.pos[0],self.pos[1],50,30)
            if p.rect.colliderect(self.rect):
                self.img=self.img1
                p.hp-=5
            if self.t>=50:
                self.pos[0]=-500
            sc.blit(self.img,(self.pos[0],self.pos[1]))
        
            if not self.img==self.img1:
                self.pos[0]+=self.dir
            else:
                self.t+=1
    class fires:
        def __init__(self):
            self.lists=[]
        def add(self,x):
            self.lists.append(x)
        def draw(self):
            for i in self.lists:
                i.draw()
                if i.pos[0]<=-200 or i.pos[0]>=2100:
                    self.lists.remove(i)
    f1=fires() 


    class enemeys():
        def __init__(self,pos):
            player.__init__(self,pos)
            self.speed=uniform(1,1)
            self.t1=0
            self.s5=self.pos[0]
            self.rect=pygame.Rect(self.pos[0],self.pos[1],120,80)
            self.choose=randint(0,6)
            self.img=list(map(lambda x :pygame.transform.scale(pygame.image.load(x),(120,80)).convert_alpha(),"PNG/Retina/tanks_tankDesert2.png PNG/Retina/tanks_tankGrey5.png PNG/Retina/tanks_tankGrey3.png PNG/Retina/tanks_tankGrey4.png PNG/Retina/tanks_tankGreen5.png PNG/Retina/tanks_tankGreen2.png PNG/Retina/tanks_tankGreen2.png".split(" ")))
        def draw(self):
            self.rect=pygame.Rect(self.pos[0],self.pos[1],120,80)
            if -100<=self.pos[0]<=1930:

                a=-self.speed*sin(self.t1)
                if randint(0,250)==1:
                    f1.add(fire(list(self.pos),10*a//(abs(a)+1*(a==0))))
                self.pos[0]+=a
                self.t1+=0.005
                a1=player.collDown(self)
                if (not a1) and not self.pos[1]>=1000:
                    self.t+=0.05
                else:
                    self.t=0
                    self.s1=0
                if randint(0,120)==1 and (a1 or self.pos[1]>=1000):
                    self.s1=7
                self.pos[1]+=self.t-self.s1
                sc.blit(pygame.transform.flip(self.img[self.choose],a<=0,0),(self.pos[0],self.pos[1]))
            self.pos[0]-=p.s
    class e11:
        def __init__(self):
            self.list1=[]
        def add(self,x):
            self.list1.append(x)
        def draw(self):
            for i in self.list1:
                i.draw()
    e111=e11()
    class player:
        def __init__(self,pos):
            self.s=0
            self.pos=pos
            self.wait=100
            self.t=0
            self.s1=0
            self.score=0
            self.hp=200
            self.frame=0
            self.rect=pygame.Rect(self.pos[0],self.pos[1],110,50)
            self.img=[pygame.transform.scale(pygame.image.load("player9.png"),(110,150)).convert_alpha(),pygame.transform.scale(pygame.image.load("player0.png"),(110,150)).convert_alpha()]
        def collDown(self):
            for i in m1.list1:
                for j in i.list2:
                    rect=pygame.Rect(j[1].x,j[1].y,j[1].width,10)
                    if self==p:
                        rect1=pygame.Rect(self.pos[0],self.pos[1]+50,110,5)
                    else:
                        rect1=pygame.Rect(self.pos[0],self.pos[1]+self.img[self.frame].get_height(),110,5)
                    rect2=pygame.Rect(self.pos[0],self.pos[1],110,5)
                    if rect2.colliderect(j[1]) or self.pos[1]<=0:
                        self.s1=0
                        self.t=2
                    if rect.colliderect(rect1):
                    
                        if j[2]<=0:
                            j[1].x=-500
                        if self==p and j[2]!=31:
                            j[2]-=0.1
                        return True
            return False
        def update(self):
            self.wait+=1
            if bot1[pygame.K_m] and self.wait>=100:
                b1.add(bomb(list(self.pos)))
                self.wait=0
            self.rect=pygame.Rect(self.pos[0],self.pos[1],110,50)
            if self.hp<=0:
                self.pos[1]=2000
            a1=self.collDown()
            if not a1:
                self.t+=0.05
            else:
                self.t=0
                self.s1=0
            if bot1[pygame.K_LEFT]:
                self.pos[0]-=3
            if bot1[pygame.K_UP] and a1:
                self.s1=7
            if self.t-self.s1<0:
                self.frame=1
            else:
                self.frame=0
            self.pos[1]+=self.t-self.s1
            if bot1[pygame.K_RIGHT]:
                if self.pos[0]>500:
                    self.s=5
                else:
                    self.pos[0]+=3
            else:
                self.s=0
            pygame.draw.rect(sc,"gray",(self.pos[0]+5,self.pos[1]-50,100,20))
            pygame.draw.rect(sc,"blue",(self.pos[0]+5,self.pos[1]-50,self.hp/2,20))

            sc.blit(self.img[self.frame],(self.pos[0],self.pos[1]))
        
    p=player([1000,250])
    class map1:
        def __init__(self,x1):
            self.list1="PNG/Environment/ground_cake_broken.png PNG/Environment/ground_cake_small_broken.png PNG/Environment/ground_cake_small.png PNG/Environment/ground_cake.png PNG/Environment/ground_grass_broken.png PNG/Environment/ground_grass_small_broken.png PNG/Environment/ground_grass_small.png PNG/Environment/ground_grass.png PNG/Environment/ground_sand_broken.png PNG/Environment/ground_sand_small_broken.png PNG/Environment/ground_sand_small.png PNG/Environment/ground_sand.png PNG/Environment/ground_snow_broken.png PNG/Environment/ground_snow_small_broken.png PNG/Environment/ground_snow_small.png PNG/Environment/ground_snow.png PNG/Environment/ground_stone_broken.png PNG/Environment/ground_stone_small_broken.png PNG/Environment/ground_stone_small.png PNG/Environment/ground_stone.png PNG/Environment/ground_wood_broken.png PNG/Environment/ground_wood_small_broken.png PNG/Environment/ground_wood_small.png PNG/Environment/ground_wood.png".split(" ")
            shuffle(self.list1)
            self.x1=x1
            self.list1=self.list1[:9]
            self.list2=[[pygame.image.load(i).convert_alpha(),pygame.Rect(randint((1930)*x1,x1*1930+1930),randint(0,1130),pygame.image.load(i).get_width(),pygame.image.load(i).get_height()),("broken" in i)*randint(3,30)+(not "broken" in i)*31] for i in self.list1]
            c=True
            while c:
                c=False
                for i in self.list2:
                    for j in self.list2:
                
                        if i!=j and i[1].colliderect(j[1]):
                            c=True
                            break
                    if c:
                        break
                if c:    
                    self.list2=[[pygame.image.load(i).convert_alpha(),pygame.Rect(randint((1930)*x1,x1*1930+1930),randint(0,1130),pygame.image.load(i).get_width(),pygame.image.load(i).get_height()),("broken" in i)*randint(3,30)+(not "broken" in i)*31] for i in self.list1]
            for i in self.list2:
                if randint(1,5)==1:
                    e111.add(enemeys([i[1].x,i[1].y-100]))
            for i in self.list2:
                if randint(1,7)==1:
                    c1.add(car([i[1].x-200,i[1].y-50]))
        def draw(self):
            for i in  self.list2:
                if i[1].x>=-600 and i[1].x<=2300:
                    sc.blit(i[0],(i[1].x,i[1].y))
                i[1].x-=p.s
    class maps:
        def __init__(self,x):
            self.list1=[]
            for i in range(0,x+1):
                pygame.draw.rect(sc,"blue",(1500/2,1000/2,i,30))
                pygame.draw.rect(sc,"red",(1500/2,1000/2,x,30),3)
                pygame.display.update()
                self.list1.append(map1(i))
        def add(self,x1):
            self.list1.append(map(x1))
        def draw(self):
            for i in self.list1:
                i.draw()
    m1=maps(100)



    e111.add(enemeys([randint(0,1930),-500]))
    class bg:
        def __init__(self):
            self.list1=list(map(lambda x : pygame.transform.scale(pygame.image.load(x),(1930,1130)),"Backgrounds/backgroundDesert.png Backgrounds/backgroundEmpty.png Backgrounds/backgroundForest.png Backgrounds/backgroundCastles.png".split(" ")))*100
            shuffle(self.list1)
            self.x1=0
        def draw(self):
            c1=0
            for i in self.list1:
                sc.blit(i,(1930*c1-(self.x1),0))
                self.x1+=p.s/500
                c1+=1
    b2=bg()
    class bomb:
        def __init__(self,pos):
            self.img=[pygame.transform.scale(pygame.image.load("blast.png"),(200,200)),pygame.transform.scale(pygame.image.load("bomb.png"),(100,100))]
            self.b=1
            self.pos=pos
            self.t=0
            self.rect=pygame.Rect(self.pos[0],self.pos[1],200,200)
        def draw(self):
            self.rect=pygame.Rect(self.pos[0],self.pos[1],200,200)
            self.t+=1
            if self.t>=100:
                for i in c1.list1:
                    if i.rect.colliderect(self.rect):
                        p.score+=i.score*10
                        c1.list1.remove(i)
                    for j in e111.list1:
                        if j.rect.colliderect(self.rect):
                            p.score+=randint(1,5)*5
                            e111.list1.remove(j)
                self.b=0
            if self.t>=150:
                self.pos[0]=-500
            self.pos[0]-=p.s
            sc.blit(self.img[self.b],(self.pos[0]-50*(not self.b),self.pos[1]-50*(not self.b)))
    class bombs:
        def __init__(self):
            self.list1=[]
        def add(self,x):
            self.list1.append(x)
        def draw(self):
            for i in self.list1:
                i.draw()
                if i.pos[0]<=-200:
                    self.list1.remove(i)
    b1=bombs()

    font=pygame.font.SysFont("Arial",100)
    c=True
    while c:
        
        bot1=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_i:
                    c=False
                if event.key==pygame.K_o:
                    quit()

        sc.fill("white")
        if p.pos[1]<=1500:
            b2.draw()
            e111.draw()
            m1.draw()
            p.update()
            f1.draw()
            b1.draw()
            c1.draw()
        else:
            try:
                dump(int(p.score),f222)
            except:
                pass
            f222.close()
            label=font.render(str(p.score)+" MAX :"+str(load_all_pickle("t1")),1,"black")
            sc.blit(label,(250,250))
        pygame.display.update()
    f222.close()
while True:
    run()

    

    
