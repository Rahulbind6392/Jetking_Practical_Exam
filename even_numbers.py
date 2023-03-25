def is_even_number(mylist):
    evennumbers = []
    for numbers in mylist:
        if numbers % 2 == 0:
            evennumbers.append(numbers)
    return evennumbers
        
print(is_even_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))        
        