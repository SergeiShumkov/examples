import json

with open("rza_event_log.json", "r") as read_file:
    data = json.load(read_file)    # dict

events = data["events"]

f = open("file.txt", 'w+')

for i in events:
    tlabel = i["tlabel"]
    evtype = i["evtype"].encode('WINDOWS-1251').decode('utf-8')
    if len(evtype) < 5:
        evtype = evtype + " " * (5 - len(evtype))
    value = i["value"]
    name = i["name"]
    if len(name) < 40:
        name = name + " " * (40 - len(name))
    desc = i["desc"].encode('WINDOWS-1251').decode('utf-8')
    f.write("{}   {}  {}   {}  {}\n\n ".format(tlabel, evtype, value, name, desc))


f.close



# aris_get_web_page3 = aris_get_web_page2[4] .encode('iso-8859-1').decode('utf-8')