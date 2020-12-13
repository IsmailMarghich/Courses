# Write a program to find if a list is a permutation of another(if theyre the reverse of each other)

def permutation(list1, list2):
    print(list1)
    list2.reverse()
    print(list2)
    if list1 == list2:
        return True
    else: return False
print(permutation([1,2,3], [3,2,1]))