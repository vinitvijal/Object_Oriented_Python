class ABC():
    class_var = 0
    def intel(self, var = 0):
        ABC.class_var += 1
        self.var = var
        print("Object Variable is : ",var)
        print("Class Variable is : ",ABC.class_var)
ob = ABC()
a = 5
while a == 5:
    xyz = int(5)
    ob.intel(xyz)
    
