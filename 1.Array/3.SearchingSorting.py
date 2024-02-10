# Create an array of integers
integerArray = [1, 2, 3, 4, 5]

# Print the array
print("Array of integers:", integerArray)
print("Length:", len(integerArray))  # Get the length of the array

# extending with self twice
integerArray.extend(integerArray)
integerArray.extend(integerArray)

# Print the array
print("Array of integers:", integerArray)
print("Length:", len(integerArray))  # Get the length of the array

# searching element in array
# let's say targetValue is the variable

def findValueInArray(array, value):
    if value in array:
        return True
    else:
        return False
    
targetValue = 5

if findValueInArray(integerArray, targetValue):
    print("Value", targetValue,"present in array")
else:
    print("Value", targetValue,"is not present in the array")
    

targetValue = 8

if findValueInArray(integerArray, targetValue):
    print("Value", targetValue,"present in array")
else:
    print("Value", targetValue,"is not present in the array")
    

# sorting the array in ascending way

integerArray.sort()
print("After sorting: ", integerArray)

# reversing the array

integerArray.reverse()
print("After reversing: ", integerArray)