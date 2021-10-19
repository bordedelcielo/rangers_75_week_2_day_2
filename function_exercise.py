def fullName(first_name,last_name):
    for index, value in enumerate(first_name):
        print(f'My first name is {value}, {last_name[index]}')

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']
print(fullName(first_name, last_name))

# Combining elements from list
# step one: acquire elements by index position
# step two: concat elements by index position

# first_name = ['John', 'Evan', 'Jordan', 'Max']
# last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# print(f"{first_name[0]} {last_name[0]}")



# first_name = ['John', 'Evan', 'Jordan', 'Max']
# last_name = ['Smith', 'Smith', 'Williams', 'Bell']
# print(fullName(first_name))
# # call function here

# def fullName(first_name,last_name):
#     full_name = []
#     for i in first_name:
#         return full_name.append(f"{first_name[0]} {last_name[0]}")

# first_name = ['John', 'Evan', 'Jordan', 'Max']
# last_name = ['Smith', 'Smith', 'Williams', 'Bell']

# print(fullName(first_name,last_name)