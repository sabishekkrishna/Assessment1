def basic_pay(hours,rate):
    return hours*rate

def add_hra(basic, percent):
    return (basic+basic*percent*0.01)
if __name__=="__main__":
    ans = basic_pay(160,250)
    print(ans)