import json

from Utilities.Input_file import  dic_input as ui

# val = ui()
dic = {
    "Farhad": "Engineer",
    "Place" : "Kupwara",
    "Haseena": "Dr",
    "26166424": "Farhad Reshi"

}
# print(f"Value : ",dic["26166424"])
# print(f"Value : ",dic)
# for key in dic.keys():
#     print(key)
# for value in dic.values():
#     print(value)


for key,val in dic.items():  #items() → returns tuples (key, value) so you can unpack both at once.
        print(f"{key} : {val}")
# print(json.loads(val)) # JSON(avaScript Object Notation)
