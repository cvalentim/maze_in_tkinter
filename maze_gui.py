from Tkinter import *
import tkMessageBox
from solver import Solver

class Maze:
	def __init__(self, parent):
		self.margin = 30
		self.pixel_width = 500
		self.canvas = Canvas(parent, width = self.pixel_width + 2 * self.margin,
									 height = self.pixel_width + 2 * self.margin)
		self.canvas.pack(side = TOP)
		self.canvas.bind("<Button-1>", self.on_click)
		self.canvas.bind("<Button-3>", self.set_start)

		self.button_solve = Button(parent, text = 'Solve', pady = 3, command = self.solve)
		self.button_solve.pack(side = TOP)
		#self.button_solve.bind("<Button-1>", self.solve)

		self.button_random = Button(parent, text = 'Random Maze', pady = 3)
		self.button_random.pack(side = TOP)
		self.button_random.bind("<Button-1>", self.random_maze)

		self.m = {}
		self.rev_m = {}
		self.start = -1, -1
		self.solver = Solver()

	def on_click(self, event):
		self.canvas.focus_set()
		ret = self.canvas.find_closest(event.x, event.y)
		if self.canvas.type(ret) == 'rectangle':
			i, j = self.m[ret[0]]
			color = self.canvas.itemcget(ret, 'fill')
			if color == '':
				self.canvas.itemconfig(ret, fill = 'black')
				self.maze[i][j] = 1
			elif color == 'black':
				self.canvas.itemconfig(ret, fill = '')
				self.maze[i][j] = 0

	def set_start(self, event):
		self.canvas.focus_set()
		ret = self.canvas.find_closest(event.x, event.y)
		if self.canvas.type(ret) == 'rectangle':
			i, j = self.m[ret[0]]
			color = self.canvas.itemcget(ret, 'fill')
			if self.start == (-1, -1) and color == '':
				self.start = (i, j)
				self.canvas.itemconfig(ret, fill = 'red')
			elif self.start == (i, j):
				self.start = (-1, -1)
				self.canvas.itemconfig(ret, fill = '')

	def solve(self):
		if self.start == (-1, -1):
			tkMessageBox.showerror("Fail", "Start position must be set.")	
			return 
		can, ans = self.solver.solve(self.maze, self.start)
		if can:
			ans = ans[1:]
			for cell in ans:
				index = self.rev_m[cell]
				self.canvas.itemconfig(index, fill = 'blue')	
		else:
			tkMessageBox.showerror("No way out", "There is no way to scape")

	def draw_cell(self, i, j, cellsize, color = ''):
		x1 = self.margin + i * cellsize
		y1 = self.margin + j * cellsize
		x2 = x1 + cellsize
		y2 = y1 + cellsize
		index = self.canvas.create_rectangle(x1, y1, x2, y2, fill = color)
		self.m[index] = (i, j)
		self.rev_m[(i, j)] = index

	def random_maze(self, event, ncell = 20):
		self.canvas.focus_set()
		self.canvas.delete('all')
		cellsize = self.pixel_width/ncell
		self.maze = [[0] * ncell for x in xrange(ncell)]
		self.start = (-1, -1)
		for i in xrange(ncell):
			for j in xrange(0, ncell):
				import random
				if random.randint(0, 1) and (i, j) != (0, 0):
					self.draw_cell(i, j, cellsize, color = 'black')
					self.maze[i][j] = 1
				else:
					self.draw_cell(i, j, cellsize, color = '')

	def draw_maze(self, ncell):
		cellsize = self.pixel_width/ncell
		self.maze = [[0] * ncell for x in xrange(ncell)]
		self.start = -1, -1
		for i in xrange(ncell):
			for j in xrange(0, ncell):
				self.draw_cell(i, j, cellsize)

if __name__ == '__main__':
	root = Tk()
	maze = Maze(root)
	maze.draw_maze(20)
	root.mainloop()
