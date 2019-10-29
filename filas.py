class Filas:

	def __init__(self, mem, resources):
		self.filaGeral = []
		self.filaReal = []
		self.fila1 = []
		self.fila2 = []
		self.fila3 = []
		self.memory = mem 			# memoria criada com objeto e enviada como parâmetro
		self.resources = resources

	def distribuiFilas(self):				# função de distribuição das filas
		j = len(self.filaGeral)
		while j > 0:
			flag = 0
			pos = 0
			cont = 0 		# posição inicial da possível área de alocação
			tam = 0
			proc = self.filaGeral.pop(0)			# buscando o primeiro elemento inserido na fila geral
			if(proc.priority == 0):					# se for de tempo real
				j -= 1
				for i in self.memory.realtime:		# para cada posição do vetor da memória realtime
					if(i == 0):						# se podemos alocar algo no bloco i = 0
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
					self.memory.preencheMemoria(pos, proc.memory, proc.priority)		# realiza a ocupação da memória 
					proc.offset = pos
					self.filaReal.append(proc)		# alocamos à fila real se tiver espaço para o processo
					#print("Fila real: ", self.filaReal)
					#print("Memoria realtime: ", self.memory.realtime)
				else:
					self.filaGeral.append(proc)		# retornamos o processo para a fila geral, para algum momento futuro da execução em que esse possa ser executado
			elif(proc.priority == 1):
				j -= 1
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
					if(self.resources.checkResources(proc)):
						proc.offset = pos
						self.memory.preencheMemoria(pos, proc.memory, proc.priority)
						self.fila1.append(proc)
						#print("Memoria usuario: ", self.memory.user)
					else:
						print("Processo ", proc.id, " não possui os recursos necessários para sua execução, retornando ele para a fila geral")
						self.filaGeral.append(proc)
				else:
					self.filaGeral.append(proc)
			elif(proc.priority == 2):
				j -= 1
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
					if(self.resources.checkResources(proc)):
						proc.offset = pos
						self.memory.preencheMemoria(pos, proc.memory, proc.priority)
						self.fila2.append(proc)
						#print("Memoria usuario: ", self.memory.user)
					else:
						print("Processo ", proc.id, " não possui os recursos necessários para sua execução, retornando ele para a fila geral")
						self.filaGeral.append(proc)
				else:
					self.filaGeral.append(proc)
			elif(proc.priority == 3):
				j -= 1
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
					if(self.resources.checkResources(proc)):
						proc.offset = pos
						self.memory.preencheMemoria(pos, proc.memory, proc.priority)
						self.fila3.append(proc)
						#print("Memoria usuario: ", self.memory.user)
					else:
						print("Processo ", proc.id, " não possui os recursos necessários para sua execução, retornando ele para a fila geral")
						self.filaGeral.append(proc)
				else:
					self.filaGeral.append(proc)















