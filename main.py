
def mutiple_tuple(nums):
    
    temp = list(nums)
    
    product = 1 
    
    for x in temp:
    
        product *= x
    

    return product

nums = (6, 3, 2, 2, -1, 18)


print ("Original Tuple: ")

print(nums)

print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums))


nums = (2, 4, 6, 8, 3, 2, 9)


print ("\nOriginal Tuple: ")


print(nums)

print("Product - multiplying all the numbers of the said tuple:", mutiple_tuple(nums)) 
