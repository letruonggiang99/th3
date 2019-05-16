#import các thư viện cần dùng
from tkinter import*
import time
import random
#lớp bóng
class Ball:
    def __init__(seft,canvas,color,van,thanh,thanh2):
        seft.canvas = canvas
        seft.vando=van
        seft.thanhchan=thanh
        seft.thanhchan2=thanh2
        seft.id = canvas.create_oval(10,10,25,25,fill=color)
        seft.canvas.move(seft.id, 100, 200)
        start=[-3,-2,-1,1,2,3]
        random.shuffle(start)
        seft.x=start[0];
        seft.y=1;
        seft.canvas_height=500;
        seft.canvas_width=400;
        seft.over= False
    def vacham1(seft,pos):
        pos_vando=seft.canvas.coords(seft.vando.id)
        
        if pos[0]>=pos_vando[0] and pos[0] <= pos_vando[2]:
            if pos[1]>= pos_vando[1] and pos[3]<=pos_vando[3]:
                return True
        return False
    def vacham2(seft,pos):
        pos_thanhchan=seft.canvas.coords(seft.thanhchan.id)
        if pos[0]>=pos_thanhchan[0] and pos[0] <= pos_thanhchan[2]:
            if pos[1]>= pos_thanhchan[1] and pos[3]<=pos_thanhchan[3]:
                return True
        return False 
    def vacham3(seft,pos):
        pos_thanhchan2=seft.canvas.coords(seft.thanhchan2.id)
        if pos[0]>=pos_thanhchan2[0] and pos[0] <= pos_thanhchan2[2]:
            if pos[1]>= pos_thanhchan2[1] and pos[3]<=pos_thanhchan2[3]:
                return True
        return False 
    def draw(seft):
        seft.canvas.move(seft.id, seft.x, seft.y)
        pos= seft.canvas.coords(seft.id)
        if pos[1]<=0:
            seft.y=2
        if pos[3] >= seft.canvas_height:
            seft.over= True
        if seft.vacham1(pos)==True:
            seft.y=-2
        if seft.vacham2(pos)==True:
            seft.y=-2
        if seft.vacham3(pos)==True:
            seft.y=2
        if pos[0]<=0:
            seft.x=2;
        if pos[2] >= seft.canvas_width:
            seft.x= -2;
    

#lớp ván đỡ bóng            
class vando:
    def __init__(seft,canvas,color):
        seft.canvas= canvas
        seft.id=canvas.create_rectangle(0,0,100,20,fill=color)
        seft.canvas.move(seft.id,300,400)
        seft.canvas.bind_all('<KeyPress-Left>',seft.trai)
        seft.canvas.bind_all('<KeyPress-Right>',seft.phai)
        seft.x=0;
        seft.y=0;
        seft.canvas_width=450;
    def draw(seft):
        seft.canvas.move(seft.id,seft.x,seft.y)
        por=seft.canvas.coords(seft.id)
        if por[0]<=0:
            seft.x=2;
        if por[2]>=seft.canvas_width:
            seft.x=-2;
    def trai(seft,event):
        seft.x=-2;
    def phai(seft,event):
        seft.x=2;

#lớp thanh chan bóng            
class thanhchan:
    def __init__(seft,canvas,color):
        seft.canvas= canvas
        seft.id=canvas.create_rectangle(0,0,100,20,fill=color)
        seft.canvas.move(seft.id,0,100)
    def draw(seft):
        seft.canvas.move(seft.id,0,0)
#lớp thanh chan bóng 2            
class thanhchan2:
    def __init__(seft,canvas,color):
        seft.canvas= canvas
        seft.id=canvas.create_rectangle(0,0,100,20,fill=color)
        seft.canvas.move(seft.id,0,101)
    def draw(seft):
        seft.canvas.move(seft.id,0,0)
        
        
#tạo khung        
tk=Tk()
#tên game
tk.title("game do bong")
#lệnh ngăn cản sự thay đổi kích cỡ khung
tk.resizable(0,0)
can=Canvas(tk, width=400, height=500)
can.pack()
van=vando(can,"blue")
thanh=thanhchan(can,"black")
thanh2=thanhchan2(can,"black")
bong=Ball(can,"red",van,thanh,thanh2)




while 1:
    if bong.over !=True:
        bong.draw()
        van.draw()
        thanh.draw()
        thanh2.draw()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)
    else:
        break;
print("game over")

 
