# <tempo de inicialização>
# <prioridade>
# <tempo de processador>
# <blocos em memória>
# <númerocódigo da impressora requisitada>
# <requisição do scanner>
# <requisição do modem>
# <númerocódigo do disco>

import sys

class Reader:

	def __init__(self):
		self.iden = []
		self.init = []
		self.priority = []
		self.processor = []
		self.memory = []
		self.printer = []
		self.scanner = []
		self.modem = []
		self.disc = []
		self.blocks = 0
		self.segocup = 0


	def readProcesses(self):
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
			i += 1

		f.close()
		f = open(fileExecution, "r")
		fl = f.readlines()
		blocks = int(fl[0])
		segocup = int(fl[1])
		print(blocks)
		print(segocup)

		print("Identificador do processo")
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
				
