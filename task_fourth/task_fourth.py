def swap(listik):
    if len(listik) < 2:
        print(listik)
    else:
       print(list(reversed(listik)))

print(swap([1, 2, 3, 4, 5]))
print(swap([]))
print(swap([1,2]))
print(swap(['one', 'two', 'three']))
print(swap([1]))