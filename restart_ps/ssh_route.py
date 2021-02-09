#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import paramiko

from restart_ps.Moudle_log import logger


nvidia_com = "nvidia-smi > /dev/null && echo $?"

# create command line to execute in remote machine
def create_command(param):
    fir_command = "sudo netstat -lntup | grep " + param + " | awk '{print $7}' | awk -F '[/]' '{print $1}'"
    sec_command = "sudo ps -ef | grep " + param +" | grep -v grep | awk '{print $9}' | awk -F '[/]' '{print $4}'"
    command_line = [fir_command, sec_command]
    restart_line = "sudo systemctl restart lotus-worker-{}.service".format(param)
    if not param.isdigit():
        return restart_line
    else:
        return command_line

# create remote ssh object
def con_ssh(ip):
    pkey = paramiko.RSAKey.from_private_key_file('/home/shuzhan/.ssh/shuzhan')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许连接不在known_hosts文件中的主机
    try:
        ssh.connect(hostname=ip, port=22, username='shuzhan', pkey=pkey)
    except Exception as e:
        logger.error("ssh can't connet remote machine {} Error is {}".format(ip, e))
    return ssh

# execute command on remote machines
def remote_exe(ssh, com):
    logger.info('ready to execute {}: '.format(com))
    stdin, stdout, stderr = ssh.exec_command(com)
    result = stdout.readline().strip()
    logger.info(result)
    if stderr.read().decode('utf-8'):
        logger.error(stderr.read().decode('utf-8'))
    return result

# the api of the whole process
def transfer(ip, port):
    com = create_command(port)
    con = con_ssh(ip)
    # first_step: to judge Gpu status is correct
    # remote_exe(con, nvida_com)
    if isinstance(com, list):
        pid = remote_exe(con, com[0])
        logger.info('the pid of current process is {}'.format(pid))
        com = create_command(pid.strip())
        character = remote_exe(con, com[1])
        logger.info('the character of current process is {}'.format(character))
    com = create_command(character.strip())
    remote_exe(con, com.lower())
    con.close()


def main():
    transfer('192.168.29.109', '6610')


if __name__ == "__main__":
    main()
