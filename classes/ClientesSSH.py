#!/usr/bin/python
import os
import base64
import inspect
import configparser

from Crypto.Cipher import DES3


class ClientsSSH:
    def __init__(self, filePref=None, dir_configs=None):
        self.dir = dir_configs
        self.file_pref = filePref
        self.current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
        self.parent_dir = os.path.dirname(self.current_dir)

        cfg = configparser.ConfigParser()
        try:
            cfg.read(self.parent_dir + '/configs/configuration.pref')
            if self.file_pref is None:
                self.file_pref = cfg.get('remmina', 'file')
            if self.dir is None:
                self.dir = cfg.get('remmina', 'path')
        finally:
            del cfg
        self.dict_clients = {}

    def clean_password(self, password):
        cfg = configparser.ConfigParser()
        cfg.read(self.file_pref)
        cfgSecret = cfg.get('remmina_pref', 'secret')
        secret = base64.b64decode(cfgSecret)
        password = base64.b64decode(password)
        return str(DES3.new(secret[:24], DES3.MODE_CBC, secret[24:]).decrypt(password), 'ascii')[:-1].rstrip('\x00')

    def files_clients_ssh(self):
        for p, _, files in os.walk(os.path.abspath(self.dir)):
            return files

    def dict_clients_ssh(self):
        files = self.files_clients_ssh()
        for file in files:
            cfg = configparser.ConfigParser()
            try:
                cfg.read(self.dir + '/' + file)
                group = cfg.get('remmina', 'group')
                server = cfg.get('remmina', 'server')
                name = cfg.get('remmina', 'name')
                if cfg.has_option('remmina', 'save_ssh_username'):
                    user = cfg.get('remmina', 'save_ssh_username')
                else:
                    user = cfg.get('remmina', 'ssh_username')
                pwd = cfg.get('remmina', 'ssh_password')
                try:
                    pwd = self.clean_password(pwd)
                except:
                    pass
                self.dict_clients[file] = [group, name, server, user, pwd]
            finally:
                del cfg
        return self.dict_clients

    def save_dict_clients(self):
        dict_clients = self.dict_clients_ssh()
        f = open(self.parent_dir + '/artefacts/dict_clients.json', 'w')
        f.write(str(dict_clients))
        f.close()

    def load_dict_clients(self):
        f = open(self.parent_dir + '/artefacts/dict_clients.json', 'r')
        data = f.read()
        f.close()
        return eval(data)


if __name__ == '__main__':
    clients = ClientsSSH()
    clients.save_dict_clients()
