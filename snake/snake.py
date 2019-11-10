
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# program created by owner of page obliczeniowo.jcom.pl
# Licence GPL-3.0 www.gnu.org/licenses/gpl-3.0.en.html

# This is a simple snake game program

import tkinter as tk

import random as rn

def main():

    dt = 200 # snake speed

    window = tk.Tk() # create window

    window.title("Snake") # window title

    c_draw = tk.Canvas(window, width = 600, height = 400) # create canvas
    c_draw.pack() # pack canvas

    class Snake: # snake class
        def __init__(self, width, height):
            self.width = int(width) # area width
            self.height = int(height) # area height
            self.msnake = [[self.width / 2, self.height / 2], [self.width / 2 + 1, self.height / 2], [self.width / 2 + 2, self.height / 2]] # snake elements
            self.move = 0 # index of vector described direction of snake move
            self.tmove = [[0 ,1] ,[1 ,0] ,[0 ,-1] ,[-1 ,0]] # vectors of direacion of snake move
            self.size = 10
            self.col = False # określa, czy doszło do kolizji
            self.food = [rn.randint(1, self.width - 2), rn.randint(1, self.height - 2)]
        def drawBox(self ,x, y, color = 'green'):
            c_draw.create_rectangle([x, y, x + self.size, y + self.size], fill=color)
        def draw(self):
            c_draw.delete("all")
            if self.col:
                c_draw.create_text([self.width / 2 * self.size, self.height / 2 * self.size], text = "Przegrałeś")
            else:
                for i in range(self.width):
                    self.drawBox(i * self.size, 0)
                    self.drawBox(i * self.size, (self.height - 1) * self.size)
                for i in range(1, self.height):
                    self.drawBox(0, i * self.size)
                    self.drawBox((self.width - 1) * self.size, i * self.size)
                for i in self.msnake:
                    self.drawBox(i[0] * self.size, i[1] * self.size)
                self.drawBox(self.food[0] * self.size, self.food[1] * self.size, color = 'red')
        def eat(self): # snake must eat
            if self.msnake[0][0] == self.food[0] and self.msnake[0][1] == self.food[1]: # if head of snake is on food, then snake eat
                self.msnake.append([0 ,0]) # add snake element
                self.food = [rn.randint(1, self.width - 2), rn.randint(1, self.height - 2)] # random new food for snake
        def move_snake(self):
            for i in range(len(self.msnake) - 1 ,0 ,-1):
                self.msnake[i][0] = self.msnake[ i -1][0]
                self.msnake[i][1] = self.msnake[ i -1][1]
            self.msnake[0][0] += self.tmove[self.move][0]
            self.msnake[0][1] += self.tmove[self.move][1]
            self.colision()
            self.eat()
            self.draw()
        def turnLeft(self):
            self.move = (self.move + 1) % len(self.tmove)
        def turnRight(self):
            self.move = (self.move - 1) if self.move > 0 else len(self.tmove) - 1
        def colision(self):
            if self.msnake[0][0] == 0 or self.msnake[0][1] == 0 or self.msnake[0][0] == self.width - 1 or self.msnake[0][1] == self.height - 1:
                self.col = True
            for i in self.msnake[1:]: # colision snake - snake
                if self.msnake[0][0] == i[0] and self.msnake[0][1] == i[1]:
                    self.col = True
        def reset(self):
            self.col = False
            self.msnake = [[self.width / 2, self.height / 2], [self.width / 2 + 1, self.height / 2], [self.width / 2 + 2, self.height / 2]] # snake elements
            self.move = 0 # index of vector described direction of snake move
            self.tmove = [[0 ,1] ,[1 ,0] ,[0 ,-1] ,[-1 ,0]] # vectors of direacion of snake move
            self.size = 10
            self.col = False # określa, czy doszło do kolizji
            self.food = [rn.randint(1, self.width - 2), rn.randint(1, self.height - 2)]
            window.after(dt, move)

    sn = Snake(600 / 10, 400 / 10)

    menubar = tk.Menu(window)
    menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Program", menu=menu)
    menu.add_command(label="Od nowa", command = sn.reset)
    menu.add_command(label="Wyjście", command = window.quit)
    window.config(menu=menubar)

    sn.draw()
    def move():
        sn.move_snake()
        if not sn.col:
            window.after(dt, move)
    def turnLeft(event):
        sn.turnLeft()
    def turnRight(event):
        sn.turnRight()
    window.after(dt, move)
    window.bind_all("<KeyPress-Left>", turnLeft)
    window.bind_all("<KeyPress-Right>", turnRight)

    window.mainloop()

    return 0

if __name__ == '__main__':
    main()