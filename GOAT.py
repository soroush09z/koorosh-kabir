from tkinter import*
from tkinter import simpledialog
import random
import time
tk=Tk()
tk.title('soroush,vakil paye yek')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas=Canvas(tk,width=500,height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()
game_started=False
ball_color=simpledialog.askstring('Input','Please enter the ball color',parent=tk)
paddle_color=simpledialog.askstring('Input','Please enter the paddle color',parent=tk)
def start_game(event):
    global game_started
    game_started=True
canvas.bind_all('<KeyPress>',start_game)
class Ball:         
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        self.starts=[-3,-2,-1,1,2,3]
        random.shuffle(self.starts)
        self.x=self.starts[0]
        self.y=-1
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False
        self.score=0
        self.score_text=canvas.create_text(50,20,text='Score:0',font=('Helvetica',16))
    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[1]<=paddle_pos[3]:
                self.score=self.score+1
                #in itemconfig oon textemoono berooz mikone ta ro ham naioftan
                self.canvas.itemconfig(self.score_text,text=f'Score:{self.score}')
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=3
        if pos[3]>=self.canvas_height:
            self.hit_bottom=True
            #bare inke stringo moteghayero ghati konim ghabl az cotation aval baiad f bezarim va dore moteghyer azina {} bezarim
            canvas.create_text(250,200,text=f'Score:{ball.score}',font=('Helvetica',16))
            canvas.create_text(300,250,text='GameOver shodi nooooob',font=('Helvetica',16))
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        if ball.hit_paddle(pos)==True:
            self.y=-3
class Paddle:         
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
    def draw(self):
        self.canvas.move(self.id, self.x,0)
        pos=self.canvas.coords(self.id)  
        if pos[0]<=0:
            self.x=0
        elif pos[2]>self.canvas_width:
            self.x=0
    def turn_right(self,event):
        self.x=3        
    def turn_left(self,event):
        self.x=-3
    
paddle=Paddle(canvas,paddle_color)
ball=Ball(canvas,paddle,ball_color) 
    
          

while True:
    if game_started==True:
        if ball.hit_bottom==False:
            ball.draw()
            paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
