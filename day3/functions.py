def greet():
    print("Hello from a function")
    
    
greet()
greet()
greet()
greet()


# parameter and argument

def greet(name):
    print(f"Hello, {name}")

greet('Sheikh')
greet("Rijve")

#default and keyword argument
def power(base,exponenet=2):
    return base ** exponenet

print(power(5))
print(power(5,2))
print(power(exponenet=3,base=22))


# # limit function 
def sum_of_evens(limit):
    total =0
    for i in range(1,limit+1):
        if i % 2 ==1:
            continue
        total +=i
    return total

print(sum_of_evens(10))
