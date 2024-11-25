def sum_mul(*args):
    res = sum(args)
    mul = 1
    for i  in args:
        mul *= i
    return res ,mul

print("Addition and multiplication: ",sum_mul(4,7,8))
