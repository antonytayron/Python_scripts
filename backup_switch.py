#!/usr/bin/python
import pexpect
import sys
import time

from datetime import datetime

logfilepath = ('/var/log/backup_switch.log')

now = datetime.now()
dateformat = "%Y%m%d%H%M"
dataname = now.strftime(dateformat)

ip=sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
switchname=sys.argv[4]
tftp_server=sys.argv[5]

filename = (switchname + "_"  + datetime.now().strftime(dateformat))

child = pexpect.spawn("ssh "+user+"@"+ip)
child.expect ("Password:")
child.sendline (password)

try:
    child.expect(b"#")
    child.sendline ("copy running-config tftp:")
    child.sendline (tftp_server)
    child.sendline (filename)

    if child.expect(b"#") == 0:

        mensagem = (datetime.now().strftime(dateformat) + ": OK Backup " +filename+ " realizado com sucesso\n")
        logfile = open (logfilepath, 'a')
        logfile.write(mensagem)
        logfile.close()

    else:

        mensagem = (datetime.now().strftime(dateformat) + ': ERROR Backup nao realizado.\n')
        logfile = open (logfilepath, 'a')
        logfile.write(mensagem)
        logfile.close()

except:

    mensagem = (datetime.now().strftime(dateformat) + ': ERROR Backup nao realizado.\n')
    logfile = open (logfilepath, 'a')
    logfile.write(mensagem)
    logfile.close()

child.close()
