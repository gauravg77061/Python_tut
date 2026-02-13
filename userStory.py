#user story 1 

# kettle_boiled=True

# if kettle_boiled == True:
#     print("kettle done ! timme to make chai")

# user story 2

# snack=input("Enter your preferred snack: ").lower()

# if snack == "cookies" or  snack == "samosa":
#     print(f"Great choice will serve you {snack} soon!")
# else:
#     print("sorry we only offer samosa and cookies")

#user story - 3 

# cup_size=input("enter the size of cup").lower()

# if cup_size=="small":
#     print(f"the price of small cup is 10")
# elif cup_size =="medium":
#     print("the price of medium cup is 15Rs")
# else:
#     print("The price of large cup is 20")

# staff=[("Amit",16),("Raj",15),("Gaurav",13),("Jyoti",15)]

# for name,age in staff:
#     if age >= 18 :
#         print(f"{name} is eligible")
#         break
#     else:
#         print(f"No one is eligble")

# print("you are outside of this loop")

# user story dictionary in place of match

# users=[
#     {"id":1, "total": 150 , "coupon": "p20"},
#     {"id":2, "total": 100 , "coupon": "F10"},
#     {"id":3, "total":200 , "coupon": "P50"},
    
# ]

# discounts ={
#     "p20":(0.2,0),
#     "F10":(0.5,0),
#     "P50":(0,10),
# }

# for user in users:
#     percent,fixed=discounts.get(user["coupon"],(0,0))
#     discount = user["total"]*percent+fixed
#     print(f"{user["id"]} paid {user["total"]} and will get discout{discount} on next shopping")

#     function user storty

# def print_order(name,chai_type):
#     print(f"{name} ordered {chai_type} chai!")


# print_order("Aman","masala")
# print_order("Hitesh","Ginger")

# #user story - splitting code into function

# def fetchingSales_Data():
#     print("fetching sales data")

# def filteringSales_Data():
#     print("filtering sales data")

# def summarizing_Data():
#     print("summarizing sales data")

# def generate_report():
#     fetchingSales_Data()
#     filteringSales_Data()
#     summarizing_Data()

# generate_report()

#hiding implementtation 

# def get_input():
#     print("Getting user inpunt")

# def validate_input():
#     print("validating user input")

# def save_to__db():
#     print("Saving to the data base")

# # yaha par implementain ek function mein wrap kar 
# #leneg simply ek print se dikha rahe ki ho gya 

# def register__user():
#     get_input()
#     validate_input()
#     save_to__db()

# register__user()

# Readibility

# def calculate_bill(cups,price_per_cup):
#     return cups*price_per_cup

# my_bill=calculate_bill(3,8)
# print(my_bill)

# improving tracibiity

# def add_val(price,vat_rate):
#     return price*(100+vat_rate)/100

# orders=[100,150,200]

# for price in orders:
#     final_amount=add_val(price,10)
#     print(f"original price is {price} ,with vat {final_amount}")

# local scope

# def serve_chai():
#     chai_type="Masala chai"
#     print(f"Inside the function {chai_type}")

# chai_type="Lemon Tea"
# print(f"Outside the function {chai_type}")
# serve_chai()

# enclosing scope

# def chai_counter():
#     chai_order="lemon"
#     def print_order():
#         chai_order="Ginger"
#         print("inner" ,chai_order)
#     print_order()
#     print('outer',chai_order)

# chai_order='tulsi'
# chai_counter()
# print("Global", chai_order)

# #Non scope

# def update_order():
#     chai_type='elaichi'
#     def kitchen():
#         nonlocal chai_type
#         chai_type='kesar'
#     kitchen()
#     print("After kitchen update", chai_type)

# update_order()

# global

# chai_type='plain'

# def front_desk():
#     def kitchen():
#         global chai_type
#         chai_type='Irani'
#     kitchen()

# front_desk()
# print("Final global chai:" ,chai_type)

# def special_chai(*ingre,**extras):
#     print("Inggre",ingre)
#     print("Extras",extras)

# special_chai("cinnaman","cardmon",sweetner="honey",foam="yes")

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

# chai_order()
# chai_order()

# def make_chai():
#   #  return "Here is your masala chai"
#      print("Here isyour masala tea")
# return_value=make_chai()
# print(return_value)

#return none 

# def idle_chai_wala():
#     pass

# print(idle_chai_wala())

#returning one value 

# def sold_cup():
#     return 120
# ans=sold_cup()
# print(ans)

# def chai_status(cups_left):
#     if cups_left == 0 :
#         return  "sorry,chai over"
#     return "chai is ready"

# print(chai_status(8))
# print(chai_status(0))

# def chai_reports():
#     return 20,100
# sold,remaining =chai_reports()
# print(sold)
# print(remaining)


# def pure_chai(cups):
#     return cups*10

# total_chai=0

# def impure_chai(cups):
#     global total_chai
#     total_chai+=cups

# def pour_chai(n):
#     print(n)
#     if n==0 :
#         return "All cups poured"
#     return pour_chai(n-1)
   
# ans=pour_chai(3)
# print(ans)

# arr=["Gaurav","Aman","Rachit","Gaurav"]

# arr2=list(filter(lambda a: a!="Gaurav",arr))
# print(arr2)

#comprehension

# menu=['apple','mango','apple','amla','grapes']
# apple=[fruit for fruit in menu if "app" in fruit]
# print(apple)

# favourites_chai=[
#     'Masala chai','Green tea','Masala chai','Green tea'
#     ,'Elaichi chai','Lemon tea'
# ]

# unique_chai={chai for chai in favourites_chai if len(chai)>8}

# print(unique_chai)

# recipes={
#     "Masal chai":["ginger","cardmom","clove"],
#     "Elaichi chai":["ginger","milk","clove"],
#     "spicy chai":["ginger","black pepper","clove"]
# }

# unique_spices={spice  for ingredients in recipes.values() for
#                 spice in 
#                ingredients}
# print(unique_spices)

#dict

# tea__prices={
#     "Masala chai":40,
#     "Green tea":50,
#     "Lemon tea":200
# }

# new_tea_prices={tea:price/80 for tea,price in tea__prices.items()}
# print(new_tea_prices)

#genertors

# def serve_chai():
#     yield "cup 1: masala chai"
#     yield "cup 2: ginger chai"

# stall=serve_chai()

# print(stall)

# print(next(stall))

# print(next(stall))

# for cup in stall:
#     print(cup)

# #infinite generators

# def infinite_chai():
#     cnt=1
#     while True:
#         yield f"Refil {cnt}"
#         cnt+=1

# refil=infinite_chai()

# for _ in range(6):
#     print(next(refil))

# # send alue to generator 

# def chai_customer():
#     print("Welcome ! what chai would you like !")

#     order =yield
#     while True:
#         print(f"preparing: {order}")
#         order=yield

# stall=chai_customer()
# print(stall)
# next(stall)

# stall.send("Masal chai")

# yield fromand close the generators

# def local_chai():
#     yield "Masal chai"
#     yield "ginger chai"

# def imported_chai():
#     yield "Matcha"
#     yield "Oolong"

# def full_menu():
#     yield from local_chai()
#     yield from imported_chai()

# for chai in full_menu():
#     print(chai)


# def chai_stall():
#     try:
#         while True:
#             order = yield "Waiting chai order"
#     except:
#         print("Stall closed,No more chai")

# stall =chai_stall()
# print(next(stall))
# stall.close()

# decorator 

# def my_decorator(fun):
#     def wrapper():
#         print("Befor function run")
#         fun()
#         print("After function runs")

#     return wrapper

# @my_decorator
# def greet():
#     print("Hello from decorator")

# greet()
# print(greet.__name__)

# from functools import wraps

# def log_activity(func):
#     @wraps(func)
#     def wraper(*args,**kwargs):
#         print("Before execution")
#         result=func(*args,**kwargs)
#         print("after result")
#         return result
         
#     return wraper

# @log_activity
# def brew_chai(type,milk="no"):
#     print(f"Brewing {type} chai and status of milk{milk}")

# brew_chai("Masala chai")

# from functools import wraps
# def require_admin(func):

#     @wraps(func)
#     def wrapper(user_role):
        
#         if user_role != 'admin':
#             print("Access denied: admin only")
#         else:
     
#             return func(user_role)
#     return wrapper #return fro outer function 
# @require_admin
# def access_tea_inventory(role):
#     print("Access granted to tea inventory")

# access_tea_inventory("user")
# access_tea_inventory("admin")

# class chai:
#     pass

# class chaiTime:
#     pass

# print(type(chai))
# ginger_tea=chai()

# print(type(ginger_tea))
# print(type(ginger_tea) is chai)
# print(type(ginger_tea) is chaiTime)

# class chai():
#     origin='India'

# chai.is_hot=True

# print(chai.origin)
# print(chai.is_hot)

# # creating object fromclass
# masala = chai()
# print(f" masala{masala.origin}")
# print(f"masala{masala.is_hot}")

# masala.is_hot=False
# print(f"masala{masala.is_hot}")
# print(f"coming from class {chai.is_hot}")

# variable = attribut when go inside the obect

# class chai:
#     temperature = 'hot'
#     strength = 'strong'

# cutting =chai()
# print(cutting.temperature)
# cutting.temperature='mild'
# print("After changing",cutting.temperature)
# print("Direct look in the cllass",chai.temperature)

# del cutting.temperature
# print("after deletion whats the value",cutting.temperature)

# cutting.cup='small'
# print("after adding property",cutting.cup)
# del cutting.cup
# print("after deletion cup property",cutting.cup)

#methods
# class chaicup:
#     size=150 #ml

#     def describe(self):
#         return f"A{self.size} ml cup chai"
# cup=chaicup()
# print(cup.describe())
# print(chaicup.describe(cup))

#constructor init 

# class cha_order:
#     temparature="hot"
#     def __init__(self,type_,size):
#         self.type=type_
#         self.size=size

#     def summary(self):
#         return f"{self.size}ml {self.type} chai"
    
# order=cha_order("Masala",200)
# print(order.summary())
# print(order.temparature)
# print(order.type)
# print(order.size)

#inheritance 

# class BaseChai:
#     def __init__(self,type_):
#         self.type=type_

#     def prepare(self):
#         print(f"preparing {self.type} chai...")

# class Masala_chai(BaseChai):
#     def add_spices(self):
#         print("Adding cardamon,ginger and cloves")

# class chaiShope:
#     chai_cls=BaseChai

#     def __init__(self):
#         self.chai=self.chai_cls("Regular")

#     def serve(self):
#         print(f"serving {self.chai.type} chai in the shop")

# obj =chaiShope()
# print(obj.serve())

#Accessing Base class 

#

# class chai:
#     def __init__(self,type_,strength):
#         self.type=type_
#         self.strength=strength

# # class GingerChai:
# #     def __init__(self,type_,strength,spice_level):
# #         self.type=type_
# #         self.strength=strength
# #         self.spice_level=spice_level ->there is lot of code duplication

# #2nd way
# # class GingerChai(chai):
# #     def __init__(self, type_, strength,spice_level):
# #         chai.__init__(self,type_, strength)
# #         self.spice_level=spice_level

# class Ginger(chai):
#     def __init__(self, type_, strength,spice_level):
#         super().__init__(type_, strength)
#         self.spice_level=spice_level


# class A:
#     label="A: Base class"

# class B(A):
#     label="B:Masala blend"

# class C(A):
#     label="C: Herbal"

# class D(B,C):
#     pass

# cup = D()
# print(cup.label)

# class chaiUtils:
#     @staticmethod
#     def clean_ingredients(text):
#         return [item.strip() for item in text.split(",")]

# raw='water , milk , ginger , honey'

# # obj=chaiUtils()
# # cleaned=obj.clean_ingredients(raw)
# # print(cleaned)

# # by static method

# cleaned_static=chaiUtils.clean_ingredients(raw)
# # print(cleaned)
# print(cleaned_static)

# class chai_order:

#     def __init__(self,tea_type,sweetness,size):
#         self.tea_type=tea_type
#         self.sweetness=sweetness
#         self.size=size
    
#     @classmethod
#     def from_dict(cls,order_data):
#         return cls(
#             order_data["tea_type"],
#             order_data["sweetness"],
#             order_data['size'],
#         )
    
#     @classmethod
#     def from_string(cls,order_string):
#         tea_type,sweetness,size=order_string.split("-")
#         return cls(tea_type,sweetness,size)
    
# order1=chai_order.from_dict({
#     "tea_type":'masala',
#     "sweetness":"medium",
#     "size":"small"
# })

# obj=chai_order("masala","medium",'30')
# obj.tea_type='masala'
# print(obj.__dict__)


# print(order1.__dict__)

# order2=chai_order.from_string("Ginger-low-small")
# print(order2.__dict__)

# class TeaLeaf:
#     def __init__(self,age):
#         self._age=age

#     @property
#     def age(self):
#         return self._age + 2
    
#     @age.setter
#     def age(self,age):
#         if 1<=age <=5:
#             self.__age =age
#         else:
#             raise ValueError("Tea age below 5 years must b/w 1 and 5")

# leaf = TeaLeaf(2)
# leaf.age = 1
# print(leaf.age) 

# chai_menu={"masala" :30,"ginger":40}

# try:
#     chai_menu["elaichi"]
# except KeyError:
#     print("key you are trying toexcess is not exist")
        
# print("Hello world ")

# def serve(flavour):
#     try:
#         print(f"Preparing {flavour} chai ...")
#         if flavour == 'unknown':
#             raise ValueError("We dont know that flavur")
#     except ValueError as e:
#         print("Error:", e)
#     else:
#         print(f"{flavour}")
#     finally:
#          print("Next customer")

# serve('unknown')
# serve('masala')

def process_order(item,quantity):
    try:
        price={"masala":20}[item]
        cost=price*quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("sorry that chai is not avaiable")
    except TypeError:
        print("quanity must be in number ")

process_order("ginger",2)
process_order("masala","two")
process_order("masala",2)





       



