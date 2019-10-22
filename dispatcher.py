import read

class Dispatcher:

	def __init__(self):
		self.reader = read.Reader()
		self.reader.readProcesses()
		self.reader.printProcesses()

	def dispatch(self):
		i = 0

		while i < len(self.reader.iden):
			print("dispatcher =>")
			print("PID:", self.reader.iden[i])
			print("offset:", )
			print("blocks:", self.reader.memory[i])
			print("priority:", self.reader.priority[i])
			print("time:", self.reader.init[i])
			print("printers:", self.reader.printer[i])
			print("scanners:", self.reader.scanner[i])
			print("modems:", self.reader.modem[i])
			print("drivers:", self.reader.disc[i])
			print("Filas: ", self.reader.fila.filaReal[i].priority)
			print("\n")
			i += 1