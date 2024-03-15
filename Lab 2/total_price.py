def total_price(n):
    price = 24.95
    discount = 0.4
    first_shipping = 3
    followup_shipping = 0.75
    total = round(n*price*(1-discount)+first_shipping+followup_shipping*(n-1),2)
    if n>0:
        return total
    elif n==0:
        return 0
    elif n<0:
        return "Negative Number Supplied"
