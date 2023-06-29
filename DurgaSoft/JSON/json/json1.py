# python file to json file convert
import json

employee = {
    'name' : 'Deepak',
    'salary': '120000',
    'isMarried' : True,
    'isHavingGF' : None
}

json_strint = json.dumps(employee)
print(json_strint)
print()
#=========================================
# json_string is a json obj 
#indent is space taken
#here 4 space taken to make readble
json_strint = json.dumps(employee,indent=4)
print(json_strint)
#==========================================
# key short using key_sort in alphabetical order
print()
json_strint = json.dumps(employee,indent=4,sort_keys=True)
print(json_strint)
#=======================================

with open('json11.json',"w") as f:
    json.dump(employee, f, indent=4)
print("open emp json file created ") 