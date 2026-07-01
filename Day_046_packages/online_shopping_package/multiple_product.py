def mul_product(*prod):
    total = 0
    for i in prod:
         total = total + i
    return total

def cust_profile(**profile):

    for k, v in profile.items():
        print(k, ":", v)