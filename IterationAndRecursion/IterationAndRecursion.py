def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *=i
    return result

def factorial_recursive(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
    
numbers = [0, 5, 10, 25, 50, 100]

print("Iterative Factorials:")
for num in numbers:
    print("{} = {}".format(num, factorial_iterative(num)))

print("\nRecursive Factorials:")
for num in numbers:
    print("{} = {}".format(num, factorial_recursive(num)))
