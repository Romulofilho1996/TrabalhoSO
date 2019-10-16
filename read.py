# <tempo de inicialização>
# <prioridade>
# <tempo de processador>
# <blocos em memória>
# <númerocódigo da impressora requisitada>
# <requisição do scanner>
# <requisição do modem>
# <númerocódigo do disco>

import sys

iden = []
init = []
priority = []
processor = []
memory = []
printer = []
scanner = []
modem = []
disc = []
blocks = 0
segocup = 0

def readProcesses():
	i = 0
	fileProcesses = sys.argv[1]
	fileExecution = sys.argv[2]
	f = open(fileProcesses, "r")
	fl = f.readlines()
	size = len(fl)
	while i < size:
		x = fl[i].split(',')
		iden.append(i)
		init.append(int(x[0]))
		priority.append(int(x[1]))
		processor.append(int(x[2]))
		memory.append(int(x[3]))
		printer.append(int(x[4]))
		scanner.append(int(x[5]))
		modem.append(int(x[6]))
		disc.append(int(x[7]))
		i += 1

	f.close()
	f = open(fileExecution, "r")
	fl = f.readlines()
	blocks = int(fl[0])
	segocup = int(fl[1])
	print(blocks)
	print(segocup)

	print("Identificador do processo")
	print(iden)
	print("Vetor de tempo de inicialização: ")
	print(init)
	print("Vetor de prioridade: ")
	print(priority)
	print("Vetor de tempo de processador: ")
	print(processor)
	print("Vetor de blocos de memória: ")
	print(memory)
	print("Vetor de código da impressora requisitada: ")
	print(printer)
	print("Vetor de requisição do scanner: ")
	print(scanner)
	print("Vetor de requisição do modem: ")
	print(modem)
	print("Vetor de código do disco: ")
	print(disc)
			
readProcesses()
