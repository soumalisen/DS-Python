#Program to create a dictionary with the frequency of vowels in an inputted string

s=input("Enter a string")
v="aieouAEIOU"
c={i:s.count(i)for i in v if i in s}
print(c)