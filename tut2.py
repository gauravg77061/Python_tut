
# # base__liquid=['water','milk']
# # extra_flavour=['ginger']

# # full_liquid=base__liquid+extra_flavour
# # print((f"this is method overloading, {full_liquid}"))

# # strong_brew=["black tea",'water']*3
# # print(f"operator operloading {strong_brew}")

# # raw_spice_data=bytearray(b"cinnamon")
# # print(f"elements is byter array {raw_spice_data}")


# essential_spices={"cardamon","ginger","cinnamon"}
# optional__spices={"cloves","ginger","black pepper"}

# all_spices=essential_spices | optional__spices

# print(f"All spices{all_spices}")

# common_spices=essential_spices & optional__spices

# print(f"common spices ,{common_spices}")

# only_in_essentials=essential_spices-optional__spices

# print(f"only in essentials {only_in_essentials}")

# print(f"Is clove present in optional spices? {'cloves' in optional__spices}")


# chai_order=dict(type="masala tea",size="large",sugar=2);
# print(f"chai order {chai_order}")

chai_recipe={}
chai_recipe["base"]="black tea"
chai_recipe["liquid"]="milk"
# del chai_recipe['liquid']
# print(f"printing base{chai_recipe['base']}")

# print(f"whether base is present in keys {'base' in chai_recipe.keys()}")
# print(f"whether the milk present in values {'milk' in chai_recipe.values()}")

new_chai_recipe=chai_recipe.popitem()
print(new_chai_recipe)




print(f"chai rescipe {chai_recipe}")