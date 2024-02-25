id1 = {
    "name":"Dinesh adhikari",
    "age": 22,
    "id":78,
    "college":"ascol"
}
id2 = {
    "name":"Ajit adhikari",
    "age": 21,
    "roll":76,
    "college":"ascol"
}
id1.update(id2)
print(id1)
# id1.clear()
# print(id1)
id1.pop("id")
print(id1)
id1.popitem()
print(id1)
# del id1
# print(id1)
