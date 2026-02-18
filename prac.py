# class Tea:
#     def __init__(self,age):
#         self.age=age
    
#     def chai_type(self,type_):
#         self.type_=type_

# tea=Tea(2)
# tea.chai_type('masala')
# print(tea.type_)

# yaha par agar mujhe chai_type ke andar 
# ke attributes ko access krna ho toh mein
# tea.attribute name se kr sakta hu


#case 2
# class Tea:
#     def chai_type(self):
#         return ("Printing")
    
#     def age(self,age_):
#         self.age_=age_
#         return self.age_

# tea=Tea()
# tea.age(2)
# print(tea.chai_type())
# # yaha par meine oject ki value return kri h 

# print(tea.age(3))
# # yaha par directlty value access kari
# print(tea.age_)

class Tea:
    def __init__(self,sugar):
        self.sugar_=sugar
     
    @property
    def sugar(self):
       return  self.sugar_+1

    @sugar.setter
    def sugar(self,value):
        if 1<=value <=5:
            self.sugar_=value
        else:
            raise ValueError("Invalid sugar ")
        
tea=Tea(1)
tea.sugar=10
print(tea.sugar)




        




