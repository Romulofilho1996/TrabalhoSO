class Memory:

	def __init__(self):
		self.realtime = [0]*64
		self.user = [0]*960

	def preencheMemoria(self, pos, blocks, priority):		# funcao que preenche a memoria de acordo com os processos enviados a ela
		if(priority == 0):									# se for processo realtime
			for x in range(blocks):							# para o tamanho de blocos do processo
				self.realtime[pos] = 1						# setamos o valor para 1
				pos += 1									# sempre atualizando a posicao para a seguinte
		else:												# se for processo usuario
			for x in range(blocks):
				self.user[pos] = 1
				pos += 1

	def retiraMemoria(self, offset, blocks, priority):		# funcao que retira da memoria processos ja executados
		if(priority == 0):
			for x in range(blocks):
				self.realtime[offset] = 0
				offset += 1
		else:
			for x in range(blocks):
				self.user[offset] = 0
				offset += 1