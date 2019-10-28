class Disc:

	def __init__(self, size, segocup, discfiles):
		self.size = size				# tamanho do disco
		self.disc = [0]*self.size		# cria um vetor com valores iniciais 0 do tamanho especificado
		self.segocup = segocup			# guarda o valor de segmentos ocupados
		self.discfiles = discfiles		# guarda os arquivos salvos no disco
		
	def inicializaDisco(self):
		i = 0
		j = 0
		while i < self.segocup:			# para o numero de segmentos ocupados, alocamos o arquivo em seu devido local na memória
			x = self.discfiles[i].split(',')
			while(j < int(x[2])):
				self.disc[int(x[1]) + j] = x[0]
				j += 1
			j = 0
			i += 1

		print(self.disc)