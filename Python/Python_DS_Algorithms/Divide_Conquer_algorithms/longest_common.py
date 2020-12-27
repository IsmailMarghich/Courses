#S1 and S2 are strings
#Find the length of longest subsequence which is common to both strings
#Subsequence : A sequence that can be driven from another sequence by deleting some elements without changing order of them

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2): #base case if we find no similiarity
        return 0
    if s1[index1] == s2[index2]: #base case if we find a string thats the same
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        op1 = findLCS(s1,s2, index1, index2+1) #otherwise we try to find a new sequence and return which ever is longest
        op2 = findLCS(s1,s2, index1+1, index2)
        return max(op1, op2)

print(findLCS("elephant", "eretpat", 0, 0))