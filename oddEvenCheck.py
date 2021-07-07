class Number():
    def oddEven(self, num):
        if num % 2 == 0:
            print(num ,"is Even")
        else:
            print(num ,"is Odd")
maths = Number()
a = int(input("Enter Your Number : "))
maths.oddEven(a)