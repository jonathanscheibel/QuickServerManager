import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

if len(sys.argv) < 2:
    print('Exemplo de utilizacao: Sh3ScriptExecutarComandos.py "ifconfig" ')
    exit(127)

from Servidores import Server

machine = Server()
machine.exec_cmd_all_clients(sys.argv[1])
