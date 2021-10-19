# My first stab at it
def sub_ten(list):
    list_b = []
    for i in list:
        if i < 10:
            list_b.append(i)
    return list_b

print(sub_ten([1,11,14,5,8,9]))

# List comprehension version
def sub_ten(input_list):
    new_list = [i for i in input_list if i < 10]
    return new_list
    

print(sub_ten([1,11,14,5,8,9]))