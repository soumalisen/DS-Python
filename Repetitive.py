# Write a function that takes a string as a parameter and returns a string 
#with every successive repetitive character replaced with a star(*). 


def replace_repetitivechars(input_string):
    result = ""
    for i in range(len(input_string)):
        if i > 0 and input_string[i] == input_string[i-1]:
            result += "*"
        else:
            result += input_string[i]
    return result

input_string = "balloon"
print(replace_repetitivechars(input_string))
