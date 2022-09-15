from ariscmder import Aris

import time
import requests

aris = Aris("10.2.23.23")
aris.connect_to_web()

i = 0
s = requests.session()

url = "http://{}/system_module_dm_cswi.html?command=update_dm_cswi&module_id=6".format(aris.ip)   # &module_id= поставить значение модуля в крейте

while True:
    tag = aris.get_current_tag("LOC.DM_CSWI06.Ia")
    if float(tag.val) < 0.9:
        print(tag.val)
        break
    else:
        i += 1
        print("NO  " + str(i))
        r = requests.get(url, auth = ('admin', 'admin'))
    time.sleep(20)

