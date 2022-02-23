import json     #imported json library
import re       #imported regular expression library
with open("Project root folder/websiteData.txt", encoding='utf-8') as file:   #loading file
    # print(file.read())        
    lines= file.readlines()
    # print(type(lines))
    personal=re.findall(r"[a-z]+\.[a-z]+@[a-z0-9]+\.[a-z]+", str(lines))
    others= re.findall(r"[a-z]+@[a-z]+\.[a-z]+",str(lines))
    all_emails= personal+others
    # print(all_emails)


dicts={}  # empty dictionary
for h_email in personal:    #looped over personal emails
    if h_email in dicts:
        dicts[h_email]["Occurance"]+=1
    else:
        dicts[h_email]={"Occurance":1,"EmailType":"Human"}

for o_email in others:     #looped over other emails
    if o_email in dicts:
        dicts[o_email]["Occurance"]+=1
    else:
        dicts[o_email]={"Occurance":1,"EmailType":"Non-Human"}
# print(dicts)

#to create json file
with open("Project root folder/result.json", "w") as out_file:
    json.dump(dicts, out_file)

