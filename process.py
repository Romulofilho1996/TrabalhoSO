class Process:

	def __init__(self,iden,init,priority,processor,memory,printer,scanner,modem,disc):
		self.id = iden
		self.offset = 0
		self.init = init
		self.priority = priority
		self.processor = processor
		self.memory = memory
		self.printer = printer
		self.scanner = scanner
		self.modem = modem
		self.disc = disc

	def get_init(self):
		return self.init
