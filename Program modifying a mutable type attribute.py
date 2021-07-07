class number():
    even = []
    odd = []
    def check(num):
        if num % 2 == 0:
            number.even.append(num)
        else:
            number.odd.append(num)
a = 0
while a == 0:
    asd = int(input("Enter Your Number : "))
    number.check(asd)
    print(" --> Even Numbers are : ",number.even)
    print(" --> Odd Numbers are : ",number.odd)


