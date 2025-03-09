# Write a function thant takes a list of integers as a parameters andd 
# returns third smallest number from the list.

def third_smallest(numbers):
    if len(numbers) < 3:
        print("List must contain atleast 3 elements")
        return
    
    unique_numbers = sorted(set(numbers))  
    if len(unique_numbers) < 3:
        print("List must have at least three unique elements")
        return

    return unique_numbers[2] 


numbers = [4, 1, 5, 7, 2, 8, 1, 6, 3]
print(third_smallest(numbers)) 