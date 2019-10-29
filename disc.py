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

		self.printaDisco()

	def checaDisco(self, tam):
		size = 0
		cont = 0
		pos = 0
		for i in self.disc:
			if(i == 0):
				cont += 1
				size += 1
			else:
				size = 0
				cont += 1
				pos = cont
			if(size == tam):
				return pos
		return (-1)

	def checaDiscoDeletar(self, nome_arq):
		flag = 0
		cont = 0
		for i in self.disc:
			if(i == nome_arq):
				self.disc[cont] = 0
				flag = 1
				cont += 1
			else:
				cont += 1
		if(flag == 0):
			return False
		else:
			return True

	def setPosition(self, pos, nome_arq):
		self.disc[pos] = nome_arq

	def printaDisco(self):
		print("Disco: ", self.disc)