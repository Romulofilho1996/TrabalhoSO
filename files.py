class Files:

	def __init__(self, size, segocup, discfiles):
		self.size = size
		self.disc = [0]*self.size
		self.segocup = segocup
		self.discfiles = discfiles
		
	def inicializaDisco(self):
		i = 0
		j = 0
		while i < self.segocup:
			x = self.discfiles[i].split(',')
			while(j < int(x[2])):
				self.disc[int(x[1]) + j] = x[0]
				j += 1
			j = 0
			i += 1

		print(self.disc)