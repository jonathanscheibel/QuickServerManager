#!/usr/bin/python

from paramiko import SSHClient
import paramiko
from pathlib import Path


class SecureShell:
    def __init__(self, host, user, pwd, intTimeout=10, port=22):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=host, username=user, password=pwd, timeout=intTimeout)
        transport = paramiko.Transport((host, port))
        transport.connect(None, user, pwd)
        self.sftp = paramiko.SFTPClient.from_transport(transport)

    def upload_file(self, source, target):
        self.sftp.put(source, target)

    def download_file(self, source, target):
        self.sftp.get(source, target)

    def remove_file(self, file):
        self.sftp.remove(file)

    def exec_script_out_str(self, file_script):
        file_final = Path(file_script).name
        self.upload_file(file_script, '/root/' + file_final)
        output = self.exec_cmd_out_str('sh /root/' + file_final)
        self.remove_file('/root/' + file_final)
        return output

    def exec_cmd_out_str(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() == 0:
            return stdout.read().decode('utf-8').strip("\n")
        else:
            return stderr.read().decode('utf-8').strip("\n")

    def exec_cmd_exit_status(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            print
            stderr.read()
        else:
            print
            stdout.read()


if __name__ == '__main__':
    server = SecureShell('127.0.0.1', 'root', '123456')
    try:
        server.exec_script_out_str('/home/jonathan/Desktop/script.sh')
    finally:
        del server
