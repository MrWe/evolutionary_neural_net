import tkinter as tk
import numpy as np
import helper

class App(tk.Frame):
  def __init__( self, parent):
    tk.Frame.__init__(self, parent)
    self.width = 500
    self.height = 500
    self.grid()
    self.createWidgets()
    self._createCanvas()
    self.start()

  def start(self):
    self.harvesters, self.hunters, self.storages, self.supplies = helper.init()
    for j in range(10000):
      self.show_all_elements()
      for i in range(len(self.harvesters)):
        self.harvesters[i].update()
        self.harvesters[i].set_score()
    helper.get_fitness(self.harvesters)


      # self.show_all_elements()
      # for i in range(len(self.harvesters)):
      #   self.harvesters[i].move_to_supplies(self.supplies, 0.1)
      #   self.harvesters[i].sight(self.hunters, self.supplies, self.storages, self.width)


  '''------------------------------GUI---------------------------------------'''
  def createWidgets(self):
    pass

  def show_all_elements(self):
    root.update()
    self.canvas.delete("all")
    for i in range(len(self.harvesters)):
      self.draw_point(self.harvesters[i].coords, '#00ff00')
    for i in range(len(self.hunters)):
      self.draw_point(self.hunters[i].coords, '#ff0000')
    for i in range(len(self.storages)):
      self.draw_point(self.storages[i].coords, '#0000ff')
    for i in range(len(self.supplies)):
      self.draw_point(self.supplies[i].coords, '#00ffff')

  def _createCanvas(self):
    self.canvas = tk.Canvas(width = self.width, height = self.height,
                            bg = "grey" )
    self.canvas.grid(row=0, column=0, sticky='nsew')

  def show_board(self, points):

    self.canvas.delete("all")
    self.draw_polygon(points)
    self.draw_point(point)


  def draw_point(self, point, fill='#ff0000'):
    coords = (point[0],point[1],point[0]+3,point[1]+3)
    self.canvas.create_rectangle(coords, fill=fill, width=1, state='disabled')

if __name__ == "__main__":
  root = tk.Tk()
  root.geometry( "1500x1000" )
  app = App(root)
  root.mainloop()
'''---------------------------------------------------------------------'''