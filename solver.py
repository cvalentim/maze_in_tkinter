#-*- coding: utf8 -*-
from collections import deque

class Solver:
	def __init__(self):
		self.delta = [(-1, 0), (0, -1), (1, 0), (0, 1)]

	def bfs(self, where):
		self.mark = set()
		q = deque()
		q.appendleft(where)
		self.mark.add(where)
		self.parent = {where: (-1, -1)}

		while len(q) > 0:
			now = q.pop()
			for k in self.delta:
				viz = k[0] + now[0], k[1] + now[1]
				if viz[0] < 0 or viz[0] >= self.n \
					or viz[1] < 0 or viz[1] >= self.m:	
						continue
				if self.maze[viz[0]][viz[1]] == 1:
						continue
				if viz not in self.mark:
					q.appendleft(viz)
					self.mark.add(viz)
					self.parent[viz] = now

	def construct_path(self, end):
		res = []
		while end != (-1, -1):
			res.append(end)
			assert self.parent.has_key(end)
			end = self.parent[end]
		res.reverse()
		return res
			
	"""
	Recebe uma matriz de 0's e 1's e uma posição inicial e final.
	Células com 1 representam barreiras. Essa função encontra
	o menor caminho entre start e end no labirinto e retorna esse caminho.
	"""
	def solve(self, maze, start = (0, 0), end = (0, 0)):
		self.n = len(maze)
		self.m = len(maze[0])
		if self.n == 0 or self.m == 0:
			return (False, [])
		self.maze = maze
		self.bfs(start)
		if (0, 0) in self.mark:
			return (True, self.construct_path((0, 0)))
		else:
			return  (False, [])
