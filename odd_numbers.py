def is_odd_number(mylist):
    oddnumbers = []
    for numbers in mylist:
        if numbers % 2 == 1:
            oddnumbers.append(numbers)
    return oddnumbers

print(is_odd_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))        