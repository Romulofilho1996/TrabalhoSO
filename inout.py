class Resources:

	def __init__(self):
		self.scanner = 1
		self.printer = 2
		self.modem = 1
		self.sata = 2

	def checkResources(self, proc):
		if (proc.scanner <= self.scanner and proc.printer <= self.printer and proc.modem <= self.modem and proc.disc <= self.sata):
			self.scanner -= proc.scanner
			self.printer -= proc.printer
			self.modem -= proc.modem
			self.sata -= proc.disc
			return True
		else:
			return False

