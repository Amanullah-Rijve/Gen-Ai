# task 1
def is_even(n):
    if n % 2 ==0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(5))
print(is_even(6))

# task 2
def sum_skip(limit,skip):
    total = 0
    for i in range(1,limit+1):
        if i % skip ==0:
            continue
        total +=i
    return total

print(sum_skip(10,5))

#  task 3
def count_multiplies(limit,k):
    total = 0
    for i in range(1,limit+1):
        if i % k ==0:
            total+=1
    return total


print(count_multiplies(20,5))

