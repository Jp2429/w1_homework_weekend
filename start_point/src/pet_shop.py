# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    shop_name=pet_shop['name']
    return shop_name

def get_total_cash(pet_shop):
    total_cash=pet_shop['admin']['total_cash']
    return total_cash

def add_or_remove_cash(pet_shop,change):
    pet_shop['admin']['total_cash']+=change
    

def get_pets_sold(pet_shop):
    total_pets=pet_shop['admin']['pets_sold']
    return total_pets

def increase_pets_sold(pet_shop,change):
    pet_shop['admin']['pets_sold']+=change

def get_stock_count(pet_shop):
    count=len(pet_shop['pets'])
    return count

def get_pets_by_breed(pet_shop, breed_type):
    pets=[]
    count=0
    for breed in pet_shop:
        if breed_type==pet_shop['pets'][count]['breed']:
            pets.append(pet_shop['pets'])
        else:
            return pets
        count+=1
    return pets

def find_pet_by_name(pet_shop, pet_name):
    for pets in pet_shop['pets']:
        if pets['name']==pet_name:
            pet_name=pets
            return pet_name

def remove_pet_by_name(pet_shop, p_name):
    count=0
    for pet in pet_shop['pets']:
        if p_name==pet['name']:
            pet_shop['pets'].pop(count)
        count+=1

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append(new_pet)

def get_customer_cash(customer):
    cust_cash=customer['cash']
    return cust_cash

def remove_customer_cash(customer, change):
    customer['cash']-=change

def get_customer_pet_count(customer):
    count=len(customer['pets'])
    return count

def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)

