import csv

#validate age
def validAge(age):
    try:
        age = int(age)
        return 1 <= age <= 115
    except ValueError:
        return False

#validate height
def validHeight(cm):
    try:
        cm = int(cm)
        return 40 <= cm <= 250
    except ValueError:
        return False


#validate weight
def validWeight(Weight):
    try:
        Weight = int(Weight)
        return 1 <= Weight <= 300
    except ValueError:
        return False

#calorie count


def men_calories_calculator(weight,height,age):
    men = 10*weight + 6.25*height - 5*age + 5
    return men

def woman_calories_calculator(weight,height,age):
    woman = 10*weight + 6.25*height - 5*age - 161
    return woman


class Food:
    def __init__(self, name, calorie, serving_size, healthiness, segment):
        self.name = name
        self.calorie = calorie
        self.serving_size = serving_size
        self.healthiness = healthiness
        self.segment = segment


def open_a_menu_csv(file,menu_foods):
    with open(file) as foods:
        dict_reader = csv.DictReader(foods)
        for row in dict_reader:
            food = Food(row['name'], int(row['calorie']), row['serving_size'], row['healthiness'],row['segment'])
            menu_foods.append(food)

segm_choice = ['alcohols','meats','breads','cheeses','chocolates','condiments','oils','fruits','seeds','lambs',
               'pastas','porks','chickens','fishes','vegetables']
