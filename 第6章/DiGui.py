# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return  n*factorial(n-1)

# print(factorial(90))
# def power (x,n):
#     if n==0:
#         return 1
#     else:
#         return x*power(x,n-1)
# print(power(3,2))

#二分查找算法
def search(sequence,number,lower=0,upper=None):
    if upper is None:
        upper = len(sequence)-1
    if lower==upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower+upper)//2
        if number>sequence[middle]:
            return search(sequence,number,middle+1,upper)
        else:
            return search(sequence,number,upper,middle)