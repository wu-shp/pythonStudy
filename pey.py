def describe_pet(animal_type,pet_name):
    """显示宠物的信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")

describe_pet('hamster','harry')
describe_pet('dog','willie')
describe_pet(animal_type='cat',pet_name='yom')
describe_pet(pet_name='daee',animal_type='pig')