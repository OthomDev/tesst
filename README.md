# Coding-Challenges-1-PO-week-2
Largest Gap (Java)

Given an array of integers, return the largest gap between the sorted elements of the array.

For example, consider the array:


[9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]


... in which, after sorting, the array becomes:


[0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]


... so that we now see that the largest gap in the array is between 9 and 20 which is 11.

Examples


largestGap([9, 4, 26, 26, 0, 0, 5, 20, 6, 25, 5]) ➞ 11

// After sorting: [0, 0, 4, 5, 5, 6, 9, 20, 25, 26, 26]

// Largest gap between 9 and 20 is 11

 

largestGap([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]) ➞ 4

// After sorting: [1, 3, 4, 5, 7, 7, 7, 7, 11, 12, 12, 13, 14]

// Largest gap between 7 and 11 is 4

 

largestGap([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]) ➞ 2

// After sorting: [1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]

// Largest gap between 6 and 8 is 2

# =====================================
Disarium Number (Python)

A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not.

Examples


is_disarium(75) ➞ False

# 7^1 + 5^2 = 7 + 25 = 32

 

is_disarium(135) ➞ True

# 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135

 

is_disarium(544) ➞ False

 

is_disarium(518) ➞ True

 

is_disarium(466) ➞ False

 

is_disarium(8) ➞ True


Notes


	
Position of the digit is 1-indexed.
