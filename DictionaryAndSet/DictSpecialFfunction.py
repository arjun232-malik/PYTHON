student={
    "name":"aryan",
    "subjects":{
        "physics":78,
        "chemistry":89,
        "math":91
    }  
}
# print(len(list(student.keys()))) # to print keys of dictionary
# print(len(student)) # total numbers of keys and value pairs ko count krte hai 
# print(list(student.values())) # print the values of keys  
# pair=list(student.items()) # print all the pairs in tuple
# print(pair[0])
# print(student["name2"]) # error
# print(student.get("name2")) # no error--->>None
student.update({"city":"ghaziabad","name":"arjun"}) # add kr skte hai new pairs
print(student)