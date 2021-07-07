class prn():
    string = "Hi, Its my first OOP"
    def sum(self,a,b,d = 0):
        c = a + b + d
        return c


obj = prn()
print(obj.string)
abc = obj.sum(15, 16, 40)
print("Value of C is ",abc)
