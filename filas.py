class Filas:

	def __init__(self, mem):
		self.filaGeral = []
		self.filaReal = []
		self.fila1 = []
		self.fila2 = []
		self.fila3 = []
		self.memory = mem 			# memoria criada com objeto e enviada como parâmetro

	def preencheMemoria(self, pos, blocks, priority):		# função que preenche a memória de acordo com os processos enviados a ela
		if(priority == 0):
			for x in range(blocks):
				self.memory.realtime[pos] = 1
				pos += 1
		else:
			print("Posição user: ", pos)
			for x in range(blocks):
				self.memory.user[pos] = 1
				pos += 1

	def distribuiFilas(self):				# função de distribuição das filas
		while len(self.filaGeral) > 0:
			flag = 0
			pos = 0
			cont = 0 		# posição inicial da possível área de alocação
			tam = 0
			proc = self.filaGeral.pop(0)			# buscando o primeiro elemento inserido na fila geral
			if(proc.priority == 0):					# se for de tempo real
				for i in self.memory.realtime:		# para cada posição do vetor da memória realtime
					if(i == 0):						# se o bloco i = 0, podemos alocar algo naquele bloco 
						cont += 1					# incrementamos o contador
						tam += 1					# incrementamos o tamanho da alocação
					else:							# se o bloco i estiver ocupado
						tam = 0						# reiniciamos o tamanho para 0, pois deveremos recomeçar a verificação do tamanho da alocação
						cont += 1					# o contador permanece sendo incrementado, pois esse deve pegar a próxima posição
						pos = cont 					# a posição inicial da possível área de alocação vai ser atualizada
					if(tam == proc.memory):			# se o tamanho livre for o necessário para alocarmos o processo em memória
						flag = 1					# flag = 1 indica que podemos adicionar o processo à fila real
						break						# termina aqui o for, pois seguimos pelo algoritmo first-fit
				if(flag == 1):
					self.filaReal.append(proc)		# alocamos à fila real se tiver espaçø para o processo
					self.preencheMemoria(pos, proc.memory, proc.priority)		# realiza a ocupação da memória 
					print("Memoria realtime: ", self.memory.realtime)
				else:
					self.filaGeral.append(proc)		# retornamos o processo para a fila geral, para algum momento futuro da execução em que esse possa ser executado
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















