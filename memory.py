class Memory:

	def __init__(self):
		self.realtime = [0]*64
		self.user = [0]*960

	def preencheMemoria(self, pos, blocks, priority):		# função que preenche a memória de acordo com os processos enviados a ela
		if(priority == 0):
			for x in range(blocks):
				self.realtime[pos] = 1
				pos += 1
		else:
			print("Posição user: ", pos)
			for x in range(blocks):
				self.user[pos] = 1
				pos += 1