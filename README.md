# -DSA-TEST1--B20811-



###    QUESTION 1
 a) The data structure being used in the code is a list. It is suitable for this task because a list allows a user to store a collection of numbers in a specific order.

b) Initializing maxSum with the first element of the list ensures that we have a starting point for calculating the maximum subarray sum. This initialization sets the initial value of maxSum to the first element, so if all the elements in the list are negative, the maximum subarray sum will be the first element itself.

c) The for loop iterates through the list by using the range function and the length of the list. The sumz variable keeps track of the current sum of the subarray. It is updated within the loop by adding the current element of the list to the sumz variable.

d) The code identifies the maximum subarray sum by comparing the current sum (sumz) with the maximum sum (maxSum). If the current sum becomes negative, it means that including the previous elements in the subarray would decrease the sum, so we reset the sumz to 0. If the current sum is greater than the maximum sum, we update the maximum sum to the current sum.

e) The time complexity of this code for finding the maximum subarray sum is O(n), where n is the number of elements in the list. The choice of using a list and the algorithm used contribute to its efficiency because it only requires a single pass through the list to find the maximum subarray sum.



or 
a) The code is using a list data structure to store the numbers. A list is a suitable data structure for this task because it allows for efficient access and modification of its elements. Lists are ordered sequences of elements, and each element can be accessed using its index. This makes it easy to iterate through the list and perform operations on each element. Additionally, lists can be easily extended or shortened, making them suitable for storing dynamic data sets.

b) Initializing maxSum with the first element of the list is important because it ensures that the algorithm will always find a maximum subarray sum, even if all the elements in the list are negative. If maxSum were initialized to a value less than the first element, the algorithm might not find the correct maximum subarray sum.

c) The for loop iterates through the list from the first element to the last element. The purpose of the sumz variable is to store the sum of the subarray that is currently being considered. The sumz variable is updated within the loop by adding the current element of the list to the previous sum.

d) The code identifies the maximum subarray sum by comparing the current sumz to the maxSum variable. If the current sumz is greater than maxSum, then the maxSum variable is updated to the current sumz. This ensures that the maxSum variable always stores the maximum subarray sum that has been found so far.

e) The time complexity of this code for finding the maximum subarray sum is O(n), where n is the number of elements in the list. This is because the algorithm iterates through the list once, and each iteration takes constant time. The choice of a list data structure and the use of a simple for loop contribute to the efficiency and performance of the algorithm.




```markdown
# Uganda Martyrs Python Script

This Python script manages two lists of Catholic and Anglican martyrs, identifies and removes duplicate names, and provides functions to determine the group of a martyr based on their name and to check if a given name matches any of the Uganda Martyrs.

## Instructions

### 1. Create Lists of Catholic and Anglican Martyrs

Two separate lists have been created:

```python
catholic_martyrs = ["Achileo Kiwanuka", "Adolphus Ludigo Mukasa", ...]  # List of Catholic martyrs
anglican_martyrs = ["Aaron Lubega", "Apollo Kivebulaya", ...]  # List of Anglican martyrs
```

### 2. Remove Duplicate Names

Duplicate names have been identified and removed from both lists to ensure accuracy.

### 3. Determine the Group of a Martyr

The script provides a function named `martyr_count()` that takes a martyr's name as input and returns the group (Catholic or Anglican) to which the martyr belongs.

### 4. Determine the Group of a Specific Martyr

You can use the `martyr_count()` function to determine the group of a specific martyr. For example, to find the group of the martyr named "Kizito," you can call the function like this:

```python
group = martyr_count()
if group != "Unknown":
    print(f"The martyr named Kizito belongs to the {group} group.")
else:
    print("The name Kizito is not found in either list of Uganda Martyrs.")
```

### 5. Check if a Name Matches Uganda Martyrs

A function named `matches_uganda_martyrs(name)` is provided. It returns `True` if the input name matches any of the Uganda Martyrs in both lists and `False` otherwise.

You can use this function to check if a given name matches any of the Uganda Martyrs. For example, you can input a name and see if it matches:

```python
name_to_check = input("Enter a name to check if it matches Uganda Martyrs: ")
result = matches_uganda_martyrs(name_to_check)
if result:
    print(f"{name_to_check} matches a name in either the Catholic or Anglican martyrs list.")
else:
    print(f"{name_to_check} does not match any of the Uganda Martyrs' names.")
```

