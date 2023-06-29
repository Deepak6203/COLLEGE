#Demo program for deserialization from json string  to python dictionary

# multiline line string ko tripal quots se denot karte hai
 
import json
json_string = '''{
    "name" : "Deepak",
    "salary": 120000,
    "isMarried" : true,
    "isHavingGF" : null
}'''

employee = json.loads(json_string)
#employee is python dic
print(type(employee))
print()
#====================================
#print dic data
print("Employee Name : ",employee["name"])
print("Employee Salary : ",employee["salary"])
print("Employee Ismarried : ",employee["isMarried"])
print("Employee IsHavingGF : ",employee["isHavingGF"])
#========================================
#print all data at a time
print()
for k,v in employee.items():
    print(k,":",v)