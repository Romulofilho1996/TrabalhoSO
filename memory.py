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
			for x in range(blocks):
				self.user[pos] = 1
				pos += 1

	def retiraMemoria(self, offset, blocks, priority):
		if(priority == 0):
			for x in range(blocks):
				self.realtime[offset] = 0
				offset += 1
		else:
			for x in range(blocks):
				self.user[offset] = 0
				offset += 1