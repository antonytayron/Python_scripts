import pexpect
import sys
import time

from datetime import datetime

now = datetime.now()
dateformat = "%Y%m%d%H%M"
dataname = now.strftime(dateformat)

ip=sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
switchname=sys.argv[4]
tftp_server="192.168.10.4"


child = pexpect.spawn("ssh "+user+"@"+ip)
child.expect ("Password:")
child.sendline (password)

child.expect(b"#")
child.sendline ("copy running-config tftp:")

child.sendline (tftp_server)

child.sendline (switchname + "_"  + datetime.now().strftime(dateformat))

child.expect(b"#")
child.close()