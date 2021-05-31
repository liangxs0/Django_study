# from django.test import TestCase
# #
#
# from django.contrib.auth.hashers import make_password, check_password
# # # Create your tests here.
# x = make_password("123", 'abc', 'pbkdf2_sha256')
# y = make_password("123", 'abc', 'pbkdf2_sha256')
# print(x)
# print(y)

def a(nums):
    nums = [str(n) for n in nums]
    n_nums = []
    for n in nums:
        for nn in n:
            n_nums.append(nn)

    print(n_nums)

    n_nums.sort(reverse=True)
    print(n_nums)
    res = ''
    for n in n_nums:
        res+=n
    return res

c = "".join([3,30,34,5,9])
print(c)