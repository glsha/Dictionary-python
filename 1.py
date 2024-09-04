# Write the code that uses the lists below to create a dictionary where name_list items are the keys and id_list items are the value,

# name_list = [John, 'Mark', 'Sara', 'Amy', 'Frank', 'Joana']

# id_list = ['203', '500', '100', '400', '1900', '3']

# Hint: use zip() function

 

# Expected Result:

#   {'Paul': '203', 'Mark': '500', 'Sara': '100', 'Amy': '400',   'Frank': '1900', 'Joana': '3'}

name_list = ['John', 'Mark', 'Sara', 'Amy', 'Frank', 'Joana']
id_list = ['203', '500', '100', '400', '1900', '3']
result_dict = dict(zip(name_list, id_list))
print(result_dict)