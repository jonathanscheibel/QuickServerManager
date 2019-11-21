#!/usr/bin/python
from classes.ClientesSSH import ClientsSSH
from classes.SecureShell import SecureShell


class Server:
    def __init__(self):
        self.all_clients = ClientsSSH()

    def list_all_clients(self):
        dict_clients = self.all_clients.dict_clients_ssh()
        for client in dict_clients:
            print(dict_clients[client])

    def list_all_clients_pwd_not_exists(self):
        dict_clients = self.all_clients.dict_clients_ssh()
        for client in dict_clients:
            if dict_clients[client][4] == '':
                print(dict_clients[client])

    def list_all_clients_pwd_not_valid(self):
        dict_clients = self.all_clients.dict_clients_ssh()
        for client in dict_clients:
            if len(dict_clients[client][4]) < 4:
                print(dict_clients[client])

    def exec_cmd_all_clients(self, cmd):
        # dict_clients = self.all_clients.dict_clients_ssh()
        dict_clients = self.all_clients.load_dict_clients()
        for client in dict_clients:
            try:
                ssh = SecureShell(dict_clients[client][2], dict_clients[client][3], dict_clients[client][4])
                try:
                    try:
                        print(dict_clients[client][0] + ' - ' + dict_clients[client][1] + ' -> ' + ssh.exec_cmd_out_str(
                            cmd))
                    except:
                        print(
                            dict_clients[client][0] + ' - ' + dict_clients[client][1] + ' -> ERRO AO EXECUTAR COMANDO!')
                finally:
                    del ssh
            except:
                print(dict_clients[client][0] + ' - ' + dict_clients[client][1] + ' -> ERRO AO CONECTAR!')

    def exec_script_all_clients(self, script):
        # dict_clients = self.all_clients.dict_clients_ssh()
        dict_clients = self.all_clients.load_dict_clients()
        for client in dict_clients:
            try:
                ssh = SecureShell(dict_clients[client][2], dict_clients[client][3], dict_clients[client][4])
                try:
                    try:
                        print(dict_clients[client][0] + ' - ' + dict_clients[client][1] + ' -> ' +
                              ssh.exec_script_out_str(script))
                    except:
                        print(
                            dict_clients[client][0] + ' - ' + dict_clients[client][1] + ' -> ERRO AO EXECUTAR SCRIPT!')
                finally:
                    del ssh
            except:
                print(dict_clients[client][0] + ' - ' + dict_clients[client][1] + ' -> ERRO AO CONECTAR!')

if __name__ == '__main__':
    dev_ops = Server()
    dev_ops.exec_cmd_all_clients('date')
