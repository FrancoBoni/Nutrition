print("Hi! welcome to \"Cheff Malony!\" - The first chat bot that suggests meals based on your calories to burn. "
      "like a nutrition doctor.\nPlease, answer the following 4 questions in order to know your calories to burn.\n\n ")
men_calories_to_burn = 0
women_calories_to_burn = 0
calories_to_burn = 0


#validate Gender
while True:
    gender = input("Please enter your gender (\"M\" for Male \"F\" for Female) > ").upper()
    if gender == "M":
        print('Gender: Male')
        break
    if gender == "F":
        print("Gender: Female")
        break
    else:
        print("Didn't hear of that gender yet.")


#validate age
def validAge(age):
    try:
        age = int(age)
        return 1 <= age <= 115
    except ValueError:
        return False

while True:
    Age = input("Please enter your age > ")
    if validAge(Age) is True:
        print("Age", int(Age))
        break
    else:
        print("That can't be right, can it?")


#validate height
def validHeight(cm):
    try:
        cm = int(cm)
        return 40 <= cm <= 250
    except ValueError:
        return False

while True:
    Height = input("Please enter your height in centimetres(e.g.:172) > ")
    if validHeight(Height) is True:
        print("Height", int(Height))
        break
    else:
        print("Are you that tall? come on...")


#validate weight
def validWeight(Weight):
    try:
        Weight = int(Weight)
        return 1 <= Weight <= 300
    except ValueError:
        return False

while True:
    Weight = input("Please enter your weight in kilograms as a whole number (e.g.:78) > ")
    if validWeight(Weight) is True:
        print("Weight", int(Weight))
        break
    else:
        print("I don't know if i am nor wearing my glasses today but that doesn't seem like your weight, am i right?")


#calorie count
WeightForCalorie = int(Weight)
AgeForCalorie = int(Age)
HeightForCalorie = int(Height)

def men_calories_calculator(weight,height,age):
    men = 10*weight + 6.25*height - 5*age + 5
    return men

def woman_calories_calculator(weight,height,age):
    woman = 10*weight + 6.25*height - 5*age - 161
    return woman

if gender == "M":
    men_calories_to_burn = men_calories_calculator(WeightForCalorie,HeightForCalorie,AgeForCalorie)
    print("Your burning calorie per day is of", round(men_calories_to_burn))
elif gender == "F":
    women_calories_to_burn = woman_calories_calculator(WeightForCalorie, HeightForCalorie, AgeForCalorie)
    print("Your burning calorie per day is of", round(women_calories_to_burn))
else: pass


#startin with your breackfast
print("\n\nSo, let's get started. We will be segguesting different meals for your day ingest.\n ")

#Creating a class for food in order to store more than 1 value.
# Source: https://whatscookingamerica.net/NutritionalChart.htm
if men_calories_to_burn != 0:
    calories_to_burn = men_calories_to_burn
if women_calories_to_burn != 0:
    calories_to_burn = women_calories_to_burn

calories_left = round(calories_to_burn)


class Food:
    def __init__(self, name, calorie, serving_size, healthiness):
        self.name = name
        self.calorie = calorie
        self.serving_size = serving_size
        self.healthiness = healthiness

tea = Food("tea", 45, "1 ounce", "good")
bread = Food("bread", 90, "1 ounce", "good")
yogourt = Food("yogourt", 80, "1 ounce", "good")
breakfast_class = [yogourt, bread, tea]
breakfast_list = ["bread, yogourt, tea"]

print("Breakfast Menu:")
for food in breakfast_class:
    print(food.name,"("+food.serving_size+"):", food.calorie, "calories")


#for each food in your food list check if the food.name is equal to the input string

breakfast_of_the_day = ""

while True:
    #breakfastime!
    bf_choice = input("What are you having for breakfast? (if you want to go to the next meal type 'next meal'> ").lower()
    if bf_choice == "next meal":
        # if breakfast_of_the_day == None:
        #     breakfast_of_the_day = "nothing"
        print("Your current day ingestion:", breakfast_of_the_day)
        satisfied = input("Are you satisfied with your current day food?(say 'no' if you want to do over)").lower()
        if satisfied == "no":
            breakfast_of_the_day = ""
            calories_left = round(calories_to_burn)
        elif satisfied != "no":
            break
    else:
        for food in breakfast_class:
            if food.name == bf_choice:
                calories_left = calories_left - food.calorie
                breakfast_of_the_day =  breakfast_of_the_day + " - " + bf_choice
                print("You have", calories_left, "left to burn. Do you want to have anything else or just:"+ breakfast_of_the_day,"?")
        if any(bf_choice in f for f in breakfast_list):
            pass
        else: print("Not a valid breakfast choice")
