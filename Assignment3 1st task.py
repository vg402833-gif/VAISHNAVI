def fac_rec(num):
    if num==1:
        return 1
    else:
        factorial=num*fac_rec(num-1)
        return factorial
num=(int(input("Enter a number:")))
fac_rec(num)
print(f"Factorial of a {num} is:{fac_rec(num)}")