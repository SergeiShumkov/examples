from aristester.arisconnector import ArisTelnetConnector, ArisHttpConnector
from aristester.arisparser import ArisWebParser
import telnetlib

from ariscmder import Aris



aris = Aris("10.2.23.21")
aris.connect_to_web()

params_web = {
    "ip": aris.ip,
    "port": aris.port_web,
    "login": aris.usr_web,
    "pass": aris.pwd_web,
    "timeout": aris.timeout
    }




aris_auth = ArisHttpConnector(params_web).auth

retro = ArisWebParser(aris.web_connector).get_retroarc("LOC.DIO05.DI01")

print(retro)

# Выдает 1-ый элемент массива, отсортированного по значению ключа 't' от наибольшего к наименьшему
retro_temp = sorted(retro, key=lambda rec: rec['t'], reverse=True)[0]
print(retro_temp) 

# Выдает массив, отсортированный по значению ключа 't' от наибольшего к наименьшему
retro_temp = sorted(retro, key=lambda rec: rec['t'], reverse=True)
print(retro_temp) 

# Выдает массив, отсортированный по значению ключа 't' от наименьшего к наибольшему
retro_temp = sorted(retro, key=lambda rec: rec['t'], reverse=False)
print(retro_temp)


tem =[{'a': 1, 'b': 2, 'c': 3}, {'a': 3, 'b': 2, 'c': 1}, {'a': 1, 'b': 1, 'c': 1},]

temp = sorted(tem, key=lambda rec: rec['c'], reverse=True)
print(temp)

# for i in tem:
    # print(i['b'])


"""Выполняет телнет соединение с ARIS"""


aris.connect_to_console()

params_tn = {
            "ip" : aris.ip,
            "port" : aris.port_tn,
            "login" : aris.usr_tn,
            "pass" : aris.pwd_tn,
            "timeout" : aris.timeout
            }

""""Выполняет команду по телнет"""

print(aris.console_run_command("platform"))

# aris.tn_connector.run_command("fullreboot")

aris_telnet = ArisTelnetConnector(params_tn)
aris_telnet.connect()
if  not aris_telnet.connected:
    print("Not connected")
# aris_telnet.run_command("fullreboot")

host=aris_telnet.access_params['ip']
port=int(aris_telnet.access_params['port'])
self_timeout = float(aris_telnet.access_params['timeout'])
login = aris_telnet.access_params['login']
passw = aris_telnet.access_params['pass']
aris_telnet.timeout=float(aris_telnet.access_params['timeout'])

ttt = telnetlib.Telnet(host,port,self_timeout)


ttt.read_until(b"login: ")  # Чтение до тех пор, пока не будет обнаружена байтовая строка данных, "login: ", или до истечения timeout секунд.
ttt.write(login.encode("utf-8") + b"\n")
ttt.read_until(b"Password:")
ttt.write(passw.encode("utf-8") + b"\n")
ttt.read_until(b'#', aris_telnet.timeout)   
ttt.connected=True

# print(ttt)

print(aris.console_read_journal())

"""
выполняет отключение от телнета ARIS

"""
aris.disconnect_console()

