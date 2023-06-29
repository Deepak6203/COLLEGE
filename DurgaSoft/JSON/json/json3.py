#demo program for Deserialization from json file
 
import json

with open("desjson.json","r") as f:
    employee = json.load(f) #return all data in dict form

#here print
for k,v in employee.items():
    print(k,":",v)

#print manulay
print(employee["name"])