

def power_numbers(*args: int):
   return [i**2 for i in args if isinstance(i, int)]

def is_prime(a):
    k = 0
    for i in range(2, a // 2+1):
        if (a % i == 0):
            k = k+1
        if (k <= 0):
            return True
        else:
            return False


# filter types
ODD = "odd" #нечетный
EVEN = "even"  # четный
PRIME = "prime" # простое число

def filter_numbers(*args, check):
    print("args= ", args,"check = ", check)
    if check == "even":
        return list(filter(lambda x: x % 2 == 0, args))
    if check == "odd":
        return list(filter(lambda x: x % 2 !=0, args))
    if check == "prime":
        return list(filter(is_prime, args))
