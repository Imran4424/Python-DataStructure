
# Create an array of integers
integerArray = [1, 2, 3, 4, 5]

# Print the array
print("Array of integers:", integerArray)
print("Length:", len(integerArray))  # Get the length of the array

integerArray.append(6)  # Append 6 to the end
print("Appended array:", integerArray)

integerArray.insert(2, 10)  # Insert 10 at index 2
print("Array after insertion:", integerArray)

integerArray.insert(2, 3)  # Insert 3 at index 2
print("Array after insertion:", integerArray)

integerArray.insert(6, 3)  # Insert 3 at index 6
print("Array after insertion:", integerArray)

# remove and return last element
lastElement = integerArray.pop()
print("Removed last element: ", lastElement)

# remove the first element with value 3
integerArray.remove(3)
print("After the removal of 3: ", integerArray)

# remove all ocurrence of value 3
# method to remove all occurence of value
def removeAllOccurence(intArray, value):
    for item in intArray:
        if item == value:
            intArray.remove(value)
    
    return intArray

# remove
integerArray = removeAllOccurence(integerArray, 3)
print("After the removing all occurence of 3: ", integerArray)

# clearing all elements of array
integerArray.clear()
print("After clearing")
print("length: ", len(integerArray))
print("Elements: ", integerArray)
