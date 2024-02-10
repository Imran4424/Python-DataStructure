# Create an array of integers
integerArray = [1, 2, 3, 4, 5]

# Print the array
print("Array of integers:", integerArray)

# Access elements of the array
print("Length:", len(integerArray))  # Get the length of the array
print("First element:", integerArray[0])  # Access the first element (index 0)
print("Second element:", integerArray[1])  # Access the second element (index 1)
print("Last element:", integerArray[-1])  # Access the last element using negative indexing
print("Subset:", integerArray[1:4])  # Access elements from index 1 to 3

# copying an array to another array - method 1
array2 = integerArray.copy()
print("Original array: ", integerArray)
print("Duplicated array: ", array2)

# copying an array to another array - method 2
array3 = list(integerArray)
print("Original array: ", integerArray)
print("Duplicated array: ", array3)

# concatening array - method 1 - using operator
concatArray = array2 + array3
print("Array 2: ", array2)
print("Array 3: ", array3)
print("Concat array: ", concatArray)

# concatening array - method 2 - using extend method
concatArray.extend(array3)
print("Array 2: ", array2)
print("Array 3: ", array3)
print("Concat array: ", concatArray)

