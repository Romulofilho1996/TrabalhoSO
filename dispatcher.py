class Dispatcher:

  def __init__(self, filas, reader, disc):
    self.filas = filas
    self.reader = reader     # cria um objeto de leitura dos arquivos
    self.reader.printProcesses()
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
            nome_arquivo = nome_arquivo[1]
            if(cod_op == 0):
              numBlocos = int(op[3])
              numOperacao = int(op[4])
            else:
              numOperacao = int(op[3])
            while (opTotal != numOperacao):
              opTotal += 1
              print ("P", proc.id, "instruction ", opTotal, " - SUCESSO CPU")
              print("\n")
              if(opTotal >= proc.processor):
                opTotal += 1
                print ("P", proc.id, "instruction ", opTotal, " - FALHA")
                print("O processo ", proc.id, " esgotou o seu tempo de CPU!")
                print("\n")
                j += 1
                break
            else:  
              opTotal += 1
            if(cod_op == 0 and opTotal <= proc.processor):
              self.exeggcuteAdd(id_proc, nome_arquivo, opTotal, numBlocos)
            elif(cod_op == 1 and opTotal <= proc.processor):
              self.exeggcuteDelete(id_proc, cod_op, opTotal, nome_arquivo)
          else:
            opTotal += 1
            print ("P", proc.id, "instruction ", opTotal, " - FALHA")
            print("O processo ", proc.id, " esgotou o seu tempo de CPU!")
            print("\n")
            break
          if(opTotal == proc.processor):
            print ("P", proc.id, "SIGINT")
            print("\n")
        j += 1

  def exeggcuteAdd(self, id_proc, nome_arquivo, opTotal, numBlocos):
    pos = self.disc.checaDisco(numBlocos)
    if(pos == (-1)):
      print ("P",id_proc, "instruction ", opTotal, "- FALHA")
      print("O processo ", id_proc, " não pode criar o arquivo", nome_arquivo, " por falta de espaço")
      print("\n")
    else:
      blocos = []
      for x in range(numBlocos):
        self.disc.setPosition(pos, nome_arquivo)
        blocos.append(pos)
        pos += 1
      print ("P",id_proc, "instruction ", opTotal, "- SUCESSO")
      print("O processo ", id_proc, " criou o arquivo", nome_arquivo, " (blocos ", blocos, ")")
      print("\n")
    #self.disc.printaDisco()

  def exeggcuteDelete(self, id_proc, cod_op, opTotal, nome_arquivo):
    if(self.disc.checaDiscoDeletar(nome_arquivo)):
      print ("P",id_proc, "instruction ", opTotal, "- SUCESSO")
      print("O processo ", id_proc, " deletou o arquivo", nome_arquivo)
      print("\n")
    else:
      print ("P",id_proc, "instruction ", opTotal, "- FALHA")
      print("O processo ", id_proc, " não pode deletar o arquivo", nome_arquivo, " porque não existe esse arquivo")
      print("\n")
    #self.disc.printaDisco()