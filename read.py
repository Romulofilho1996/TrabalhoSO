import sys
import process
import filas

class Reader:

	def __init__(self):
		self.iden = []				# <ID_processo>
		self.init = []				# <tempo de inicialização>
		self.priority = []			# <prioridade>
		self.processor = []			# <tempo de processador>
		self.memory = []			# <blocos em memória>
		self.printer = []			# <númerocódigo da impressora requisitada>
		self.scanner = []			# <requisição do scanner>
		self.modem = []				# <requisição do modem>
		self.disc = []				# <númerocódigo do disco>
		self.blocks = 0				# <quantidade de blocos do disco>
		self.segocup = 0			# <quantidade de segmentos ocupados no disco>
		self.files = []				# <arquivos em disco>
		self.operations = []		# <operações a serem efetivadas>
		self.fila = []

	def readProcesses(self):
		self.fila = filas.Filas()
		i = 0
		fileProcesses = sys.argv[1]
		fileExecution = sys.argv[2]
		f = open(fileProcesses, "r")
		fl = f.readlines()
		size = len(fl)
		while i < size:
			x = fl[i].split(',')
			self.iden.append(i)
			self.init.append(int(x[0]))
			self.priority.append(int(x[1]))
			self.processor.append(int(x[2]))
			self.memory.append(int(x[3]))
			self.printer.append(int(x[4]))
			self.scanner.append(int(x[5]))
			self.modem.append(int(x[6]))
			self.disc.append(int(x[7]))
			proc = process.Process(self.iden[i], self.init[i], self.priority[i], self.processor[i], self.memory[i], self.printer[i], self.scanner[i], self.modem[i], self.disc[i])
			if((proc.priority == 0 and proc.printer == 0 and proc.scanner == 0 and proc.modem == 0 and proc.disc == 0 and proc.memory <= 64) or (proc.priority != 0 and proc.printer <= 2 and proc.scanner <= 1 and proc.modem <= 1 and proc.disc <= 2 and proc.memory <= 960)):
				self.fila.filaGeral.append(proc)
			else:
				print("Processo ", i, " não pode ser executado por falta de recursos")
			i += 1
		self.fila.distribuiFilas()
		f.close()
		f = open(fileExecution, "r")
		fl = f.readlines()
		self.blocks = int(fl[0])
		self.segocup = int(fl[1])
		i = 2
		while i < (2 + self.segocup):
			self.files.append(fl[i])
			i += 1
		size = len(fl)
		while i < size:
			self.operations.append(fl[i])
			i += 1

		f.close()

	def printProcesses(self):	

		print("Quantidade de blocos do disco: ")
		print(self.blocks)
		print("Quantidade de segmentos ocupados do disco: ")
		print(self.segocup)
		print("Arquivos em disco: ")
		print(self.files)
		print("Operações a serem efetivadas: ")
		print(self.operations)

		print("Identificador do processo: ")
		print(self.iden)
		print("Vetor de tempo de inicialização: ")
		print(self.init)
		print("Vetor de prioridade: ")
		print(self.priority)
		print("Vetor de tempo de processador: ")
		print(self.processor)
		print("Vetor de blocos de memória: ")
		print(self.memory)
		print("Vetor de código da impressora requisitada: ")
		print(self.printer)
		print("Vetor de requisição do scanner: ")
		print(self.scanner)
		print("Vetor de requisição do modem: ")
		print(self.modem)
		print("Vetor de código do disco: ")
		print(self.disc)
				
