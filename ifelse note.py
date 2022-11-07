amount=int(input("enter amount no"))
if amount>=2000:
    print(amount//2000)
if amount>=500:
    print((amount%2000)//500)
if amount>=200:
    print((amount%500)//200)
if amount>=100:
    print((amount%200)//100)
if amount>=50:
    print((amount%100)//50)

