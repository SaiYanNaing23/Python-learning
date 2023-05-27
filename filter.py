nums = [1,2,3,4,5,6,7,8,9,10]

def even(num):
    return (num%2)==0

even_number=list(filter(even,nums))
print(even_number)

even_number = [num for num in nums if (num%2)==0]
print(even_number)

