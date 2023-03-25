def unique_list(mylist):
    new_list = []
    for numbers in mylist:
        if numbers not in  new_list:
            new_list.append(numbers)
    return new_list

print(unique_list([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]))         