def basic_pay(hours,rate):
    return hours*rate

def add_hra(basic, percent):
    return (basic+basic*percent*0.01)

def deduct_tax(salary, percent):
    return (salary - salary*percent*0.01)
if __name__=="__main__":
    ans = basic_pay(160,250)
    print(ans)
    hra = add_hra(160,10 )
    print(hra)
    ded = deduct_tax(hra, 5)
    print(ded)