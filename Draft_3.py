#coding: utf-8

from ariscmder import Aris
from arisconnector import ArisWebCfgConnector
import json

aris = Aris("10.2.23.23")
aris.connect_to_web()

params_web = {
            "ip": aris.ip,
            "port": aris.port_web,
            "login": aris.usr_web,
            "pass": aris.pwd_web,
            "timeout": aris.timeout
            }

aris_1 = Aris("10.2.23.1")
aris_1.connect_to_web()


params_web_1 = {
            "ip": aris_1.ip,
            "port": aris_1.port_web,
            "login": aris_1.usr_web,
            "pass": aris_1.pwd_web,
            "timeout": aris_1.timeout
            }



"""
Выдача команды ТУ через web (Контроллер нужно перевести в режим наладки)
"""

aris_connect_1_tag = ArisWebCfgConnector(params_web_1).get_tag_from_name('IEC 60870-5-104 Req.Клиент 104(Управление выключателем ввода).DO-323')
# aris_connect_1 = ArisWebCfgConnector(params_web_1).send_command_to_tag("0", aris_connect_1_tag)       # 
# print(aris_connect_1)



"""
Получение веб-страниц в формате Str
"""
url = "log//crq.log"

aris_get_web_page = ArisWebCfgConnector(params_web).get_web_page(url, params_web).encode('iso-8859-1').decode('utf-8')
aris_temp = aris_get_web_page.split("\n")

for i in range(5):
    if " 18:04:21.540 INFO : uspd" in aris_temp[i]:
        print(aris_temp[i])


"""
Получение значения по ключу в словаре, полученном как элемент списка(список получили преобразовав JSON)
"""
url1 = "KC/warehouse_subst.3.json"

aris_get_web_page1 = ArisWebCfgConnector(params_web).get_web_page(url1, params_web).encode('iso-8859-1').decode('utf-8')
aris_get_web_page2 = json.loads(aris_get_web_page1)  # list
aris_get_web_page3 = aris_get_web_page2[4]           # dict

print(aris_get_web_page3['value'])
print(aris_get_web_page2[4]['value'])



url2 = "translation_sendcommand.html"

aris_get_web_page4 = ArisWebCfgConnector(params_web).get_web_page(url2, params_web).encode('iso-8859-1').decode('utf-8')    # str
aris_get_web_page5 = json.loads(aris_get_web_page4)  # dict
if "Управление из конфигуратора запрещено." in aris_get_web_page5["message"]:
    print(True)
else:
    print(False)          

print(type(aris_get_web_page5))
# print(aris_get_web_page5)
print(aris_get_web_page5["message"])

# print(aris_get_web_page2)






"""
выполнить подстановку по тегу
        
"""
aris_set_subst_tag = ArisWebCfgConnector(params_web).get_tag_from_name('LOC.Control.Alarm')
aris_set_subst = ArisWebCfgConnector(params_web).set_substitute(aris_set_subst_tag, '0', 'true')