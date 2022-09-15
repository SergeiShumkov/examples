
from aristester.ariscmder import Aris
from aristester.arisconnector import ArisWebCfgConnector
import time

def testing(ip):
    aris = Aris(ip)
    aris.connect_to_web()

    assert aris.check_conflicts() == False

    params_web = {
    "ip": aris.ip,
    "port": aris.port_web,
    "login": aris.usr_web,
    "pass": aris.pwd_web,
    "timeout": aris.timeout
    }

    url = "events_system_list_full.html?type_id=0"

    aris_get_web_page = ArisWebCfgConnector(params_web).get_web_page(url, params_web).encode('iso-8859-1').decode('utf-8')


    index_1 = aris_get_web_page.find('"d":') + 8
    index_2 = aris_get_web_page.find('"', index_1)

    index_3 = aris_get_web_page.find('"t":') + 8
    index_4 = aris_get_web_page.find('.', index_3)

    temp_time = "{} {}".format(aris_get_web_page[index_1:index_2], aris_get_web_page[index_3:index_4])

    index_5 = index_1 - 300
    index_6 = index_4 + 1000

    timestamp = int(time.mktime(time.strptime(temp_time, "%d/%m/%Y %H:%M:%S"))) + 18000    # 18000 - 5 часов разницы

    different = aris.get_time() - timestamp

    if different <= 3800:
        print(aris_get_web_page[index_5:index_6])

    assert different > 3800    # 3800 сек(чуть больше часа) - проверка, что критическое сообщение пришло недавно




def test_21():
    ip = "10.2.23.21"

    testing(ip)


def test_22():
    ip = "10.2.23.22"

    testing(ip)


def test_23():
    ip = "10.2.23.23"

    testing(ip)


def test_24():
    ip = "10.2.23.24"

    testing(ip)

def test_25():
    ip = "10.2.23.25"

    testing(ip)



"""test_21()
test_22()
test_23()
test_24()
test_25()"""




