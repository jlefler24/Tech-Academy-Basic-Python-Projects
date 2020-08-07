people_dictionary = {'Brett' : ['Male' , 'Weight 175'], 'Nancy' : ['Female' , 'Weight 125'], 'Patrick' : ['Male' , 'Weight 195'], 'Diane' : ['Female' , 'Weight 115'], 'Adam' : ['Male' , 'Weight 215']}
print(people_dictionary)


Name = input('Please type in a name: ')
print('You typed in the name ' + Name)
Persons_Date = people_dictionary[Name]
print(Persons_Data)


people_dictionary = {'Brett' : ['Male' , 'Weight 175'], 'Nancy' : ['Female' , 'Weight 125'], 'Patrick' : ['Male' , 'Weight 195'], 'Diane' : ['Female' , 'Weight 115'], 'Adam' : ['Male' , 'Weight 215']}
print(people_dictionary)
Name = input('Please type in a name: ')
print('You typed in the name ' + Name + '!')
try:
    Persons_Data = people_dictionary[Name]
    print(Persons_Data)
except:
    print('That name, ' + Name + ', was not found in the dictionary.')


try:
    Persons_Data = people_dictionary[Name]
    print('Name: ' + Name.capitalize())
    print('Sex: ' + Persons_Data[0])
    print('Weight: ' + Persons_Data[1])


    
