def build_person(first_name,last_name,age=''):
    person={'first':first_name,'last':last_name}
    if age:
        person['age']=age    
    return person
print(build_person('Roma','Mexanik'))
print(build_person('Max','Maximov',21))
