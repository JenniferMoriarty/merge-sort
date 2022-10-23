import random

def mergeSort(myList, side):
    if len(myList) > 1:
 
        #add comment here
        leftList = []
        rightList = []

        #add comment here
        for i in range ((len(myList)//2)):
            leftList.append(myList[i])
        #add comment here
        for i in range ((len(myList)//2), len(myList)):
            #add missing line here!
            
        #add comment here
        mergeSort(leftList, "left")
 
        #add comment here 
        mergeSort(rightList, "right")
 
 
 # Now onto the actual logic of the swapping and merging! 
 # Our base case is length 1. So nothing happens there and you can ignore it. And this
 # code probably could be better if it didnt call that last base. Case 2 in the base case.
 # But anyway here we are and we have a list of 2 things and we've cut them into left and
 # right. So in the (Real) base case we have two lists of 1 thing each. As we step out
 # the two lists we're comparing are going to grow and have like 1 and 2, 2 and 3, whatever.
 # but for your brain, think of the base case as just LeftIndex is 1 number, and Rightindex is too
 
        #create indexes to walk through the left, right, and main lists
        LeftIndex = 0
        RightIndex = 0
        mainIndex = 0
        #note: myList gets REPLACED with leftList on line 42, so it starts off really small
 
        #have we reached the end of either sublists? No!
        while LeftIndex < len(leftList) and RightIndex< len(rightList): 
            #compare current elemnts of both lists, copy the smaller element into the sorted array, increment index
            if leftList[LeftIndex] <= rightList[RightIndex]:
                #add missing line here!
                LeftIndex += 1
            else:
                myList[mainIndex] = rightList[RightIndex]
                RightIndex += 1
            mainIndex += 1
          
        # Checking if any element was left, put into main list, increment index
        while LeftIndex < len(leftList):
            myList[mainIndex] = leftList[LeftIndex]
            LeftIndex += 1
            mainIndex += 1
 
        #add missing line here!
            myList[mainIndex] = rightList[RightIndex]
            #add missing line here!
            mainIndex += 1
            
        print(side, myList) #print to see the main list being rebuilt
        

# Note that if this is the base case we EXIT AND DO NOTHING
# So its not really so much the base case as the case under the
# base case. The Subbase Case.
#Driver Code ------------------------------------------------------------
nums = [3,1,4,1,5,9,2,6,5,4]

#uncomment this if you'd like to have random numbers in the list
#for i in range (9): 
    #nums.append(random.randrange(0,100))

print("List before sorting:", end = " ")
print(nums)
mergeSort(nums, "first")
print("List after sorting:", end = " ")
print(nums)


