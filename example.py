def add(a,b):
    return a+b

def divide(a,b):
    return a/b

def calculate_discount(price, percent):
    return price - price * percent

def find_duplicates(lst):
    duplicates = []
    for i in lst:
        if lst.count(i) > 1:
            duplicates.append(i)
    return duplicates