class Dispatcher:

  def __init__(self, filas, reader, disc):
    self.filas = filas
    self.reader = reader     # cria um objeto de leitura dos arquivos
    self.reader.printProcesses()
    self.disc = disc      # cria um objeto de disco de acordo com o numero de blocos do disco, de segmentos ocupados e com os arquivos
    self.disc.inicializaDisco()      # inicialização do objeto disco

  def executa(self, filaEscolhida):
    while len(filaEscolhida) > 0:
        j = 0
        flag = 0
        proc = filaEscolhida.pop(0)
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
            if (proc.opTotal < proc.processor):
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
              while (proc.opTotal != numOperacao):
                proc.opTotal += 1
                print ("P", proc.id, "instruction ", (proc.opTotal - 1), " - SUCESSO CPU")
                print("\n")
                if(proc.opTotal >= proc.processor):
                  flag = 1
                  proc.opTotal += 1
                  print ("P", proc.id, "instruction ", (proc.opTotal - 1), " - FALHA")
                  print("O processo ", proc.id, " esgotou o seu tempo de CPU!")
                  print("\n")
                  print ("P", proc.id, "return SIGINT")
                  print("\n")
                  j += 1
                  break
              else:  
                proc.opTotal += 1
              if(cod_op == 0 and proc.opTotal <= proc.processor):
                self.exeggcuteAdd(id_proc, nome_arquivo, proc.opTotal, numBlocos)
              elif(cod_op == 1 and proc.opTotal <= proc.processor):
                self.exeggcuteDelete(id_proc, cod_op, proc.opTotal, nome_arquivo)
            else:
              proc.opTotal += 1
              print ("P", proc.id, "instruction ", (proc.opTotal - 1), " - FALHA")
              print("O processo ", proc.id, " esgotou o seu tempo de CPU!")
              print("\n")              
              if(proc.opTotal == proc.processor):
                flag = 1
                self.filas.resources.freeResources(proc)
                self.filas.memory.retiraMemoria(proc.offset, proc.memory, proc.priority)
                print ("P", proc.id, "return SIGINT")
                self.filas.distribuiFilas()
                print("\n")    
                break
          j += 1
        else:
          if(flag == 0):
            self.filas.resources.freeResources(proc)
            self.filas.memory.retiraMemoria(proc.offset, proc.memory, proc.priority)
            print ("P", proc.id, "return SIGINT")
            self.filas.distribuiFilas()
            print("\n")    


  def dispatch(self):
    while len(self.filas.filaGeral) > 0 or len(self.filas.fila1) > 0 or len(self.filas.fila2) > 0 or len(self.filas.fila3) > 0:
      self.executa(self.filas.filaReal)
      self.executa(self.filas.fila1)  
      self.executa(self.filas.fila2)  
      self.executa(self.filas.fila3)      

  def exeggcuteAdd(self, id_proc, nome_arquivo, opTotal, numBlocos):
    pos = self.disc.checaDisco(numBlocos)
    if(pos == (-1)):
      print ("P",id_proc, "instruction ", (opTotal - 1), "- FALHA")
      print("O processo ", id_proc, " não pode criar o arquivo", nome_arquivo, " por falta de espaço")
      print("\n")
    else:
      blocos = []
      for x in range(numBlocos):
        self.disc.setPosition(pos, nome_arquivo)
        blocos.append(pos)
        pos += 1
      print ("P",id_proc, "instruction ", (opTotal - 1), "- SUCESSO")
      print("O processo ", id_proc, " criou o arquivo", nome_arquivo, " (blocos ", blocos, ")")
      print("\n")
    #self.disc.printaDisco()

  def exeggcuteDelete(self, id_proc, cod_op, opTotal, nome_arquivo):
    if(self.disc.checaDiscoDeletar(nome_arquivo)):
      print ("P",id_proc, "instruction ", (opTotal - 1), "- SUCESSO")
      print("O processo ", id_proc, " deletou o arquivo", nome_arquivo)
      print("\n")
    else:
      print ("P",id_proc, "instruction ", (opTotal - 1), "- FALHA")
      print("O processo ", id_proc, " não pode deletar o arquivo", nome_arquivo, " porque não existe esse arquivo")
      print("\n")
    #self.disc.printaDisco()