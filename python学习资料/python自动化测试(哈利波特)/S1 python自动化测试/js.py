
import json

data={
    "name":["jerry",'nice'],
    "age":26,
    "gender":"man"
}
data1=json.dumps(data)
print(data1)
print(type(data1))

data2=json.loads((data1))
print(type(data2))
