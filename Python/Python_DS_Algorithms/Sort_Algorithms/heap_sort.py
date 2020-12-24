#heap sort
#in a binary heap values are stored where the nodes are smaller or groter than their parent node (min or max heap)
#the idea behind heapsort is that we insert our data into a binary heap and then extract it, the extracted data is sorted
#each time we extract data from binary heap, we have to heapify the binary heap to ensure next time we extract in a sorted manner

def heapify(customList, n, i):
    smallest = i #we grab the top node as smallest
    left = 2*i + 1 #our left child node
    right = 2*i + 2 #our right child node
    if left < n and customList[left] < customList[smallest]: #if left child node is smaller
        smallest = left #we make it our new smallest

    if right < n and customList[right] < customList[smallest]: #if right child node is smaller
        smallest = right #we make it our new smalles tnode

    if smallest != i: #if our smallest isnt equal to top node
        customList[i], customList[smallest] = customList[smallest], customList[i] #we swap the smallest we found with top node
        heapify(customList, n, smallest) #we call this funttion recursively until our top node is smallest

def heapSort(customList):
    n = len(customList)
    for i in range(int(n/2)-1, -1, -1): #amount of times we have to heapify until max heap
        heapify(customList, n, i) #here we build a max heap
    for i in range(n-1,0,-1): #one by one we extract elements
        customList[i], customList[0] = customList[0], customList[i] #swap elements in sorted order
        heapify(customList, i, 0) #afterwards we heapify again 
    customList.reverse() #we can reverse our list to have large to small

#quick sort is O(NlogN) and space complexity of O(1), it is not stable however
lst = [2, 1, 7, 6, 5, 3, 4, 9, 8]
heapSort(lst)
print(lst)
