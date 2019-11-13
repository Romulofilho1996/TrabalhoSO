import time

class Dispatcher:

  def __init__(self, filas, reader, disc):
    self.filas = filas
    self.reader = reader                  # cria um objeto de leitura dos arquivos
    self.reader.printProcesses()
    self.disc = disc                      # cria um objeto de disco de acordo com o numero de blocos do disco, de segmentos ocupados e com os arquivos
    self.disc.inicializaDisco()           # inicialização do objeto disco

  def executa(self, filaEscolhida):  
    while len(filaEscolhida) > 0:         # enquanto tiver processos na fila enviada
        time.sleep(2)
        j = 0
        flag = 0
        proc = filaEscolhida.pop(0)       # vai pegar o primeiro processo que chegou nessa fila
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
        while(j < len(self.reader.operations)):                # para as operacoes no arquivo files.txt
          if(int(self.reader.operations[j][0]) == proc.id):    # se a operacao tiver o ID do processo
            if (proc.opTotal < proc.processor):                # se a operacao atual nao tiver excedido o tempo de CPU
              op = self.reader.operations[j]
              op = op.split(',')
              id_proc = int(op[0])
              cod_op = int(op[1])
              nome_arquivo = op[2]
              if(len(nome_arquivo) == 2):
                nome_arquivo = nome_arquivo[1]
              elif(len(nome_arquivo) == 1):
                nome_arquivo = nome_arquivo[0]
              if(cod_op == 0):                                 # se operacao for de adicionar
                numBlocos = int(op[3])
                numOperacao = int(op[4])
              else:                                            # se operacao for de excluir
                numOperacao = int(op[3])
              while (proc.opTotal != numOperacao):             # enquanto a operacao atual for diferente do numero da operacao, quer dizer que existem instrucoes de CPU
                proc.opTotal += 1                              # incrementamos para a operacao seguinte
                print ("P", proc.id, "instruction ", (proc.opTotal - 1), " - SUCESSO CPU")
                print("\n")
                if(proc.opTotal >= proc.processor):            # se o programa esgotar o tempo por uma instrução de CPU, o processo devera ser encerrado
                  flag = 1                                     # flag 1 se processo vai ser encerrado antes do fim da execucao de suas instrucoes
                  proc.opTotal += 1
                  print ("P", proc.id, "instruction ", (proc.opTotal - 1), " - FALHA")
                  print("O processo ", proc.id, " esgotou o seu tempo de CPU!")
                  print("\n")
                  print ("P", proc.id, "return SIGINT")
                  print("\n")
                  j += 1
                  break
              else:                                            # caso o numero da operacao seja igual ao numero da operacao atual
                proc.opTotal += 1
              if(cod_op == 0 and proc.opTotal <= proc.processor):           # se for uma operacao de adicao
                self.exeggcuteAdd(id_proc, nome_arquivo, proc.opTotal, numBlocos)         # chamada da funcao de adicionar em disco
              elif(cod_op == 1 and proc.opTotal <= proc.processor):         # se for uma operacao de exclusao
                self.exeggcuteDelete(id_proc, cod_op, proc.opTotal, nome_arquivo)         # chamada da funcao de exclusao em disco
            else:                                                           # se operacao atual eh maior ou igual ao tempo de CPU do processo
              proc.opTotal += 1
              print ("P", proc.id, "instruction ", (proc.opTotal - 1), " - FALHA")
              print("O processo ", proc.id, " esgotou o seu tempo de CPU!")
              print("\n")              
              if(proc.opTotal == proc.processor):
                flag = 1                                                    # se ainda existem instrucoes e o processo deve ser encerrado por falta de tempo
                self.filas.resources.freeResources(proc)                    # liberacao de recursos
                self.filas.memory.retiraMemoria(proc.offset, proc.memory, proc.priority)          # retira processo da memoria
                print ("P", proc.id, "return SIGINT")
                self.filas.distribuiFilas()                                 # redistribui filas
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
    while len(self.filas.filaGeral) > 0 or len(self.filas.filaReal) > 0 or len(self.filas.fila1) > 0 or len(self.filas.fila2) > 0 or len(self.filas.fila3) > 0:
      self.executa(self.filas.filaReal)
      self.executa(self.filas.fila1)  
      self.executa(self.filas.fila2)  
      self.executa(self.filas.fila3)      

  def exeggcuteAdd(self, id_proc, nome_arquivo, opTotal, numBlocos):
    pos = self.disc.checaDisco(numBlocos)                                                                 # checa se existem espaco em disco com o numero de blocos necessarios para o arquivo
    if(pos == (-1)):                                                                                      # se retornar -1, nao tem espaco
      print ("P",id_proc, "instruction ", (opTotal - 1), "- FALHA")
      print("O processo ", id_proc, " não pode criar o arquivo", nome_arquivo, " por falta de espaço")
      print("\n")
    else:                                                                                                 # se retornar outro valor, esse valor vai ser o inicial do arquivo em disco
      blocos = []
      for x in range(numBlocos):
        self.disc.setPosition(pos, nome_arquivo)
        blocos.append(pos)
        pos += 1
      print ("P",id_proc, "instruction ", (opTotal - 1), "- SUCESSO")
      print("O processo ", id_proc, " criou o arquivo", nome_arquivo, " (blocos ", blocos, ")")
      print("\n")
    self.disc.printaDisco()

  def exeggcuteDelete(self, id_proc, cod_op, opTotal, nome_arquivo):
    if(self.disc.checaDiscoDeletar(nome_arquivo)):
      print ("P",id_proc, "instruction ", (opTotal - 1), "- SUCESSO")
      print("O processo ", id_proc, " deletou o arquivo", nome_arquivo)
      print("\n")
    else:
      print ("P",id_proc, "instruction ", (opTotal - 1), "- FALHA")
      print("O processo ", id_proc, " não pode deletar o arquivo", nome_arquivo, " porque não existe esse arquivo")
      print("\n")
    self.disc.printaDisco()