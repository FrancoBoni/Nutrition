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

def calorie_limit(calorie_balance):
    if -200 <= calorie_balance <= 200:
        print("Is about to round things up because you have", calorie_balance, "calories balance.")
    if -400 < calorie_balance < -201:
        print("\nWe suggest you to close your mouth darling. Your current calorie count is:", calorie_balance,
              "\nOr you can do over your meal but definetely not having more to eat.")
        stop = True
    if calorie_balance < -401:
        print("Come on you're killing me. ")
    else:pass

def recommendation_warning(the_input,the_string):
    if the_input == the_string:
        print("We don't recommend eating",the_string,"at night but is your call...")

def healthy_warning(menu_of_the_day):
    for food in menu_of_the_day:
        if food.healthiness is "healthy" > food.healthiness is "not healthy":
            print("Watch out with what you are eating, ")


segments = ['alcohols','meats','breads','cheeses','chocolates','condiments','oils','fruits','seeds','lambs',
               'pastas','porks','chickens','fishes','vegetables']
