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

	def checaDisco(self, tam):			# checa no disco se existe espaço para adicionar o arquivo, a partir do tamanho dele
		size = 0						# size inicial 0
		cont = 0						# contador inicia em 0
		pos = 0							# posicao de inicio 0
		for i in self.disc:				# para todas as posicoes do disco
			if(i == 0):					# se a posicao for 0
				cont += 1				# contador incrementa
				size += 1				# size incrementa
			else:						# se posicao nao for 0
				size = 0				# size retorna a 0, pois devemos buscar o proximo bloco de memoria possivel para a alocacao do arquivo
				cont += 1				# contador continua sendo incrementado
				pos = cont  			# posicao de inicio da alocacao do arquivo vai ser atualizada para a posicao do contador
			if(size == tam):			# se o size for igual ao tamanho necessario para alocar o arquivo
				return pos  			# retornamos essa posicao para fazermos a alocacao
		return (-1)

	def checaDiscoDeletar(self, nome_arq):			# checa se existe o arquivo em disco para deletar
		flag = 0									# flag inicia em 0
		cont = 0									# contador inicio em 0
		for i in self.disc:							# para todos os blocos em disco
			if(i == nome_arq):						# se o bloco tem o nome do arquivo
				self.disc[cont] = 0					# zeramos esse bloco
				flag = 1							# flag vai para 1 pois arquivo foi achado no disco
				cont += 1							# posicao vai ser atualizada
			else:
				cont += 1
		if(flag == 0):
			return False
		else:
			return True

	def setPosition(self, pos, nome_arq):			# atribui a posição em disco para o nome do arquivo
		self.disc[pos] = nome_arq

	def printaDisco(self):
		print("Disco: ", self.disc)