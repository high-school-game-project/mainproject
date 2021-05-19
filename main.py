from tkinter import*
import pygame
import os
name = ['潤羽るしあ',]
hp = [300,]
attack = [10,]
defend = [10,]
info_Width = 0
info_Height = 0
class Charactor:
    def __init__(self, id, face, active, x, y, player):
        self.name = name[id]
        self.face = face
        self.active = active
        self.hp = hp[id]
        self.maxhp = hp[id]
        self.ATK = attack[id]
        self.DEF = defend[id]
        self.x = x
        self.y = y
        self.player = player
        self.pic = 1
        self.locate = '.\\8bit'+'\\'+self.name+'\\'+self.active+'\\'+str(self.pic)+'.png'
        self.key = active
    def draw(self, root):
        for i in root.find_withtag(self.player):
            root.delete(i)
        root.create_image(self.x, self.y, image = self.locate)
    def update(self, root):
        if self.key == self.active:
            self.pic %= len([name for name in os.listdir(self.active) if os.path.isfile(os.path.join(self.active, name))])
            self.pic += 1
        else:
            self.pic = 1
            self.active = self.key
        self.locate = '.\\8bit'+'\\'+self.name+'\\'+self.active+'\\'+str(self.pic)+'.png'
        self.draw(root)
    def move(self, root, dx, dy):
        self.x += dx
        self.y += dy
        self.update(root)
class Game:
    def __init__(self):
        self.player1 = None
        self.player2 = None
        self.info = Tk()
        self.info.state("zoomed")
        #self.info.geometry("1920x1080") 
        self.info.title('Hololive Battle Menu')
        self.info.iconbitmap('.\\icon\\icon.ico')
        self.info.resizable(0,0)
        self.info.config(bg="#f0f0f0")
    def set_Game(self):
        self.root = Tk()
        #self.root.geometry("1920x1080")
        self.root.state("zoomed")
        self.root.title('Hololive Battle Game')
        self.root.iconbitmap('.\\icon\\icon.ico')
        self.root.resizable(0,0)
        self.root.config(bg="#f0f0f0")
        self.root.bind("<Key>", self.game_Control)
    def game_Control(self, Event):
        if Event.keycode == 65:
            print('left')
    def exit_Info(self):
        self.info.quit()
        #pygame.mixer.music.stop()
        #pygame.quit()
        self.info.destroy()
    def switch_To_choose(self):
        self.exit_Button.destroy()
        self.start_Button.destroy()
        self.info.config(bg="#FFFFFF")
    def start(self):
        global info_Height, info_Width
        info_Height = self.info.winfo_height()
        info_Width = self.info.winfo_width()
        self.start_Button = Button(self.info, 
                                   text = 'Start', 
                                   relief = "flat", 
                                   bg = '#f0f0f0', 
                                   fg = '#000000', 
                                   activebackground = '#101010', 
                                   activeforeground = '#f0f0f0',
                                   command = self.switch_To_choose,
                                   font = ('',20))
        self.start_Button.place(anchor = CENTER, x = info_Width//2, y = info_Height//2-55,
                                width = 200, height = 100)
        self.exit_Button = Button(self.info, 
                                   text = 'Exit', 
                                   relief = "flat", 
                                   bg = '#f0f0f0', 
                                   fg = '#000000', 
                                   activebackground = '#101010', 
                                   activeforeground = '#f0f0f0',
                                   command = self.exit_Info,
                                   font = ('',20))
        self.exit_Button.place(anchor = CENTER, 
                               x = info_Width//2, y = info_Height//2+55,
                                width = 200, height = 100)
        self.logo = PhotoImage(file = '.\\icon\\title.png')
        self.start_title = Label(self.info,
                                 image = self.logo,
                                 relief = "flat")
        self.start_title.place(anchor = CENTER,
                               x = info_Width//2, y = info_Height//2-250)
        self.info.mainloop()
        
        #self.root.mainloop()
#test = Charactor(id = 0, face = 1, active = 'wait', x = 0, y = 0, player = 'p1')     
if __name__ == '__main__':
    game = Game()
    game.start()