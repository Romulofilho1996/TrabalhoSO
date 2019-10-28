import dispatcher
import memory 
import filas
import inout

mem = memory.Memory()

resources = inout.Resources()

filas = filas.Filas(mem, resources)

disp = dispatcher.Dispatcher(filas)

disp.dispatch()