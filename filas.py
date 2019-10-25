import memory

class Filas:

	def __init__(self):
		self.filaGeral = []
		self.filaReal = []
		self.fila1 = []
		self.fila2 = []
		self.fila3 = []
		self.memory = memory.Memory()

	def preencheMemoria(self, pos, blocks, priority):
		if(priority == 0):
			for x in range(blocks):
				self.memory.realtime[pos] = 1
				pos += 1
		else:
			print("Posição user: ", pos)
			for x in range(blocks):
				self.memory.user[pos] = 1
				pos += 1

	def distribuiFilas(self):
		while len(self.filaGeral) > 0:
			flag = 0
			pos = 0
			cont = 0
			tam = 0
			proc = self.filaGeral.pop(0)
			if(proc.priority == 0):
				for i in self.memory.realtime:
					if(i == 0):
						cont += 1
						tam += 1
					else:
						tam = 0
						cont += 1
						pos = cont
					if(tam == proc.memory):
						flag = 1
						break
				if(flag == 1):
					self.filaReal.append(proc)
					self.preencheMemoria(pos, proc.memory, proc.priority)
					print("Memoria realtime: ", self.memory.realtime)
				else:
					self.filaGeral.append(proc)
			elif(proc.priority == 1):
				for i in self.memory.user:
					if(i == 0):
						cont += 1
						tam += 1
					else:
						tam = 0
						cont += 1
						pos = cont
					if(tam == proc.memory):
						flag = 1
						break
				if(flag == 1):
					self.fila1.append(proc)
					self.preencheMemoria(pos, proc.memory, proc.priority)
					print("Memoria usuario: ", self.memory.user)
				else:
					self.filaGeral.append(proc)
			elif(proc.priority == 2):
				for i in self.memory.user:
					if(i == 0):
						cont += 1
						tam += 1
					else:
						tam = 0
						cont += 1
						pos = cont
					if(tam == proc.memory):
						flag = 1
						break
				if(flag == 1):
					self.fila2.append(proc)
					self.preencheMemoria(pos, proc.memory, proc.priority)
					print("Memoria usuario: ", self.memory.user)
				else:
					self.filaGeral.append(proc)
			elif(proc.priority == 3):
				for i in self.memory.user:
					if(i == 0):
						cont += 1
						tam += 1
					else:
						tam = 0
						cont += 1
						pos = cont
					if(tam == proc.memory):
						flag = 1
						break
				if(flag == 1):
					self.fila3.append(proc)
					self.preencheMemoria(pos, proc.memory, proc.priority)
					print("Memoria usuario: ", self.memory.user)
				else:
					self.filaGeral.append(proc)















