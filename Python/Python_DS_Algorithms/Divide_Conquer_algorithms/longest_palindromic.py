#S is a given string
#Find the length of longest palidromic subsequence
#Subsequence : A sequence that can be driven from another sequence by deleting some elements without changing order of them
#palindrome is a string that reads the same backward as well as forward (e.g MADAM)

def findLPS(s, startIndex, endIndex):
    if startIndex > endIndex: #basecase if we run out of string
        return 0
    elif startIndex == endIndex: #basecase if inedx are the same
        return 1
    elif s[startIndex] == s[endIndex]: #basecase if we find the same letter
        return 2 + findLPS(s, startIndex+1, endIndex-1)
    else:
        op1 = findLPS(s, startIndex, endIndex-1) #otherwise we try new indexes and return max
        op2 = findLPS(s, startIndex+1, endIndex)
        return max(op1, op2)

print(findLPS("ELRMENMET", 0, 8))
