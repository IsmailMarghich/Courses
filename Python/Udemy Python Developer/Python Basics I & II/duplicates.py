# Check for duplicates in list:
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicate_list = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicate_list:
            duplicate_list.append(value)

print(duplicate_list)

