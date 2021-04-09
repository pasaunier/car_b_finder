import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from classes.mediator import Mediator

print("Result : ", Mediator.processUserInput("img/audi.jpg"))