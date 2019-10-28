import read
import disc

class Dispatcher:

  def __init__(self, filas):
    self.filas = filas
    self.reader = read.Reader(self.filas)      # cria um objeto de leitura dos arquivos
    self.reader.readProcesses()
    self.reader.printProcesses()
    self.disc = disc.Disc(self.reader.blocks, self.reader.segocup, self.reader.files)      # cria um objeto de disco de acordo com o numero de blocos do disco, de segmentos ocupados e com os arquivos

  def dispatch(self):
    i = 0

    while i < len(self.filas.filaReal):
      print("dispatcher =>")
      print("PID:", self.filas.filaReal[i].id)
      print("offset:", self.filas.filaReal[i].offset)
      print("blocks:", self.filas.filaReal[i].memory)
      print("priority:", self.filas.filaReal[i].priority)
      print("time:", self.filas.filaReal[i].init)
      print("printers:", self.filas.filaReal[i].printer)
      print("scanners:", self.filas.filaReal[i].scanner)
      print("modems:", self.filas.filaReal[i].modem)
      print("drivers:", self.filas.filaReal[i].disc)
      print("\n")
      i += 1

    # while i < len(self.reader.iden):
    #   print("dispatcher =>")
    #   print("PID:", self.reader.iden[i])
    #   print("offset:", )
    #   print("blocks:", self.reader.memory[i])
    #   print("priority:", self.reader.priority[i])
    #   print("time:", self.reader.init[i])
    #   print("printers:", self.reader.printer[i])
    #   print("scanners:", self.reader.scanner[i])
    #   print("modems:", self.reader.modem[i])
    #   print("drivers:", self.reader.disc[i])
    #   print("\n")
    #   i += 1

    self.disc.inicializaDisco()      # inicialização do objeto disco