from enum import Enum
from helpers import *


class Actions(Enum):
    PRINT = 0
    ADD = 1
    DELETE = 2
    SEARCH = 3
    UPDATE = 4
    EXIT = 5

def display_menu():
    """
    Display the menu for user
    """
    for action in Actions: print_green(f"{action.value} - {action.name}")
    return Actions(int(input("your selection : ")))

def add_car():
    """
    Add new element in cars array, and _green the added car
    """
    cars.append({"model":input("Insert the model : "), 
                 "type":input("Insert the type : "), 
                 "color":input("Insert the color : "), 
                 "year":input("Insert the year : "), })
    print_green(f"car added: {cars[-1]}")

def search_car():
    """
    search_cars search all car models present in cars array
    seacrh method is not case-sensitive
    Returns: 
     list : indexes of found items in 'cars' list
     list : found items in 'cars' list 

    """
    found = False
    found_cars_index = []
    found_cars = []
    count = 0

    if cars == []:
        print_green("repository cars is empty")
        return
    search = input("give me model to search: ")
    for index,car in enumerate(cars):
        if car['model'].lower() == search.lower():
            count +=1
            print_green(f"{str(count)} - model is present : {car}")
            found_cars_index.append(index)
            found_cars.append(car)
            found = True
    if not found :
        print_green(f"model not found")
    return  found_cars_index,found_cars

def delete_car():
    """
    Delete a car from the list using search_car function
    """
    found_cars_index, found_cars  = search_car()
    if (len(found_cars) == 0): return
    id = choice(found_cars_index, found_cars)
    confirm = input(f"Are you sure to delete : {found_cars[id]} : Y / N : ")
    if confirm.lower() == 'y': 
        print_green(f"delete {found_cars[id]}")
        cars.remove(found_cars[id])
    else:
        print_green("Operation canceled. Return to menu")

def choice(found_cars_index, found_cars):
    """
    Inner function that return index of car to select, in order to update or delete it
    """
    if (len(found_cars)>1):
        user_choice = input(f"Select car between : 1 to {len(found_cars_index)}")
        id = int(user_choice) - 1
    if (len(found_cars) == 1): id = 0
    return id

def update_car():
    """
    Update details of selected car
    """
    found_cars_index, found_cars  = search_car()
    if (len(found_cars) == 0): return
    id = choice(found_cars_index, found_cars) 
    confirm = input(f"Are you sure to update : {found_cars[id]} : Y / N : ")
    if confirm.lower() == 'y': 
        for key, value in cars[id].items():
            new_value = input(f"Current {key} is : {value}\nUpdate the new {key} : ")
            if new_value:
                cars[id][key] = new_value
            else:
                print_green(f"{key} : {value} remains unchanged")
       

def display_cars():
    """
    Display car properties
    """

    for id, car in enumerate(cars):
        print_green(f"{str(id+1)} - {car['model']} | {car['type']} | {car['color']} | {car['year']}" )
    


def menu():
    while (True):
        user_selection = display_menu()
        if user_selection == Actions.PRINT: display_cars()
        if user_selection == Actions.ADD: add_car()
        if user_selection == Actions.DELETE: delete_car()
        if user_selection == Actions.SEARCH: search_car()
        if user_selection == Actions.UPDATE: update_car()
        print_dotted_line()
        if user_selection == Actions.EXIT: return



if __name__ == '__main__':
    cars = read_csv_to_list_of_dicts("cars.csv")
    menu()
    print_green("thank you for using car managment program")
    save_list_of_dicts_to_csv(cars, "cars.csv")