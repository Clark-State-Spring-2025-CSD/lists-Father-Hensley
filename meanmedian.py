#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class

theList = []

for i in range(5):
    theList.append(int(input(f"Number {i+1}:")))

print("as entered: " + str(theList))

theList.sort()

print(f"small to large: {theList}")

theList.sort(reverse=True)

print(f"large to small: {theList}")

median = theList[2]

sum = 0

for i in range(5):
    sum += theList[i]

mean = sum / 5

print(f"The median is {median} and the mean is {mean}")