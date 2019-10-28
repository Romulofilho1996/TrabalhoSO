class Dispatcher:

  def __init__(self, filas, reader, disc):
    self.filas = filas
    self.reader = reader     # cria um objeto de leitura dos arquivos
    self.reader.printProcesses()
    # self.idProcesso = 
    # self.codigoOperacao
    # self.nomeArquivo
    # self.numBlocos
    # self.numOperacao
    self.disc = disc      # cria um objeto de disco de acordo com o numero de blocos do disco, de segmentos ocupados e com os arquivos
    self.disc.inicializaDisco()      # inicialização do objeto disco

  def dispatch(self):
    while len(self.filas.filaReal) > 0:
      j = 0
      opTotal = 0
      proc = self.filas.filaReal.pop(0)
      print("dispatcher =>")
      print("PID:", proc.id)
      print("offset:", proc.offset)
      print("blocks:", proc.memory)
      print("priority:", proc.priority)
      print("time:", proc.init)
      print("printers:", proc.printer)
      print("scanners:", proc.scanner)
      print("modems:", proc.modem)
      print("drivers:", proc.disc)
      print("\n")
      while(j < len(self.reader.operations)):
        if(int(self.reader.operations[j][0]) == proc.id):
          if (opTotal < proc.processor):
            op = self.reader.operations[j]
            op = op.split(',')
            id_proc = int(op[0])
            cod_op = int(op[1])
            nome_arquivo = op[2]
            if(cod_op == 0):
              numBlocos = int(op[3])
              numOperacao = int(op[4])
            else:
              numOperacao = int(op[3])
            while (opTotal != numOperacao):
              print ("P", proc.id, "instruction ", opTotal, " - SUCESSO CPU")
              opTotal += 1
              if(opTotal >= proc.processor):
                print ("P", proc.id, "instruction ", opTotal, " - FALHA1 CPU")
                break
            else:  
              opTotal += 1
          else:
            print ("P", proc.id, "instruction ", opTotal, " - FALHA CPU")
            break
        j += 1

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

  #def exeggcuteAdd(self, id_proc, cod_op, nome_arquivo, numBlocos):


  #def exeggcuteDelete(self, id_proc, cod_op, nome_arquivo):


