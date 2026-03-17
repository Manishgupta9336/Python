marks = {"Manish" : 78,
       "Alok" : 87,
       "Shivam" : 100,
}
print(marks.get("Alok"))
print(marks.get("Manish2")) #return none if not exist
print(marks["Manish2"])  #return error if not exist