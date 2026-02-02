
# base__liquid=['water','milk']
# extra_flavour=['ginger']

# full_liquid=base__liquid+extra_flavour
# print((f"this is method overloading, {full_liquid}"))

# strong_brew=["black tea",'water']*3
# print(f"operator operloading {strong_brew}")

# raw_spice_data=bytearray(b"cinnamon")
# print(f"elements is byter array {raw_spice_data}")


essential_spices={"cardamon","ginger","cinnamon"}
optional__spices={"cloves","ginger","black pepper"}

all_spices=essential_spices | optional__spices

print(f"All spices{all_spices}")

common_spices=essential_spices & optional__spices

print(f"common spices ,{common_spices}")

only_in_essentials=essential_spices-optional__spices

print(f"only in essentials {only_in_essentials}")

print(f"Is clove present in optional spices? {'cloves' in optional__spices}")
