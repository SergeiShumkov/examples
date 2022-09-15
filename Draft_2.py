#coding: utf-8

from ariscmder import Aris
from arisparser import ArisTag, ArisWebParser
from arisconnector import ArisWebCfgConnector


from lxml import etree
from lxml import html




aris = Aris("10.2.23.22")
aris.connect_to_web()

params_web = {
            "ip": aris.ip,
            "port": aris.port_web,
            "login": aris.usr_web,
            "pass": aris.pwd_web,
            "timeout": aris.timeout
            }

"""
Получение параметров тега по имени
"""

aris_connect = ArisWebCfgConnector(params_web).get_tag_from_name("LOC.DM_CSWI06.Connect")       # Dict
print(aris_connect)


"""
Получение текущего значения, качества, и метки времени по тэгу 
"""
aris_temp2 = ArisWebCfgConnector(params_web).get_data_from_tag(aris_connect)    # class 'bytes'
print(aris_temp2)

"""
Получение значения из дерева типа b'<?xml version="1.0" encoding="utf-8"?>\n<Data>\n\t\n\t<channel_id_907>1</channel_id_907>\n    <quality_val_907 >0xC0</quality_val_907>\n    <time_val_907 >1625022401490</time_val_907>\n\n    \n</Data>\n'
"""

aris_qual = etree.fromstring(aris_temp2).xpath('/Data/quality_val_{}'.format(aris_connect["id"]))[0].text   # Str
print(aris_qual)

t = etree.fromstring(aris_temp2).xpath('/Data/time_val_{}'.format(aris_connect["id"]))[0].text
print(t)


"""
Получение значения качества (целое число или текст) из значения качества, полученного из дерева
"""

aris_teg = ArisTag()
aris_teg.quality_to_int(aris_qual)
print(aris_teg.q, aris_teg.q_text)


"""
Получение значения времени (в секундах с точностью до тысячных) из значения времени, полученного из дерева
"""

aris_teg.get_timestamp(t)
print(aris_teg.t)






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
aris_connect_1 = ArisWebCfgConnector(params_web_1).send_command_to_tag("0", aris_connect_1_tag)       # 
print(aris_connect_1)




# ArisWebParser(aris.web_connector).get_version

aris_page = ArisWebParser(aris.web_connector)._get_page("index.html")

print(aris_page.get_element_by_id("footer").find("p").text)
