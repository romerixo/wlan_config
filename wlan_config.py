import argparse
import telnetlib

parser = argparse.ArgumentParser(
    usage="%(prog)s <host> <user> <passwd> <on | off>")
parser.add_argument("host", help="HOST (IP) for connection")
parser.add_argument("user", help="USER for connection")
parser.add_argument("password", help="PASSWORD for connection")
parser.add_argument("action", choices=["on", "off"], 
    help="[on | off] Enable or disable Wiffi")
parser.add_argument("-p", "--port", default=23, 
    help="PORT for connection (default 23)")

args = parser.parse_args()

#vars
HOST = args.host
USER = args.user
PASSWORD = args.password
PORT = args.port
ACTION = args.action

# connection
telnet = telnetlib.Telnet(HOST, PORT)

# credentials
telnet.read_until("Login: ")
telnet.write(USER + "\n")

telnet.read_until("Password: ")
telnet.write(PASSWORD + "\n")

# enabling - disabling WLAN
telnet.read_until(" > ")
telnet.write("wlctl radio " + ACTION + "\n")
telnet.write("quit \n")

# uncoment for debuggin
#print telnet.read_all()

print "WLAN is %s" % ACTION
