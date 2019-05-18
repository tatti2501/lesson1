def get_summ(one, two, delimiter='&'):
    one=str(one)
    two=str(two)
    thr=one+delimiter+two
    return thr.upper()
summ=get_summ("one","two")
print(summ)
summ=get_summ("Learn", "python")
print(summ)
def format_price(price):
    price=int(price)
    

