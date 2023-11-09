def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return ("not is_prime")
    return ("is_prime")
n=int(input("enter the value:"))
print(is_prime(n))
