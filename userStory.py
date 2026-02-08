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

def serve_chai():
    yield "cup 1: masala chai"
    yield "cup 2: ginger chai"

stall=serve_chai()

print(stall)

print(next(stall))

print(next(stall))

# for cup in stall:
#     print(cup)




       



