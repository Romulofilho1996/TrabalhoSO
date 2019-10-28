import dispatcher
import memory 
import filas
import inout
import read
import disc

mem = memory.Memory()

resources = inout.Resources()

filas = filas.Filas(mem, resources)

reader = read.Reader(filas)

reader.readProcesses()

disc = disc.Disc(reader.blocks, reader.segocup, reader.files)

disp = dispatcher.Dispatcher(filas, reader, disc)

disp.dispatch()