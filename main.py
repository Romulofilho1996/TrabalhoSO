import dispatcher
import memory 
import filas

mem = memory.Memory()

filas = filas.Filas(mem)

disp = dispatcher.Dispatcher(filas)

disp.dispatch()