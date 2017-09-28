from NutritionTheory import *

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


while True:
    Age = input("Please enter your age > ")
    if validAge(Age) is True:
        print("Age", int(Age))
        break
    else:
        print("That can't be right, can it?")


while True:
    Height = input("Please enter your height in centimetres(e.g.:172) > ")
    if validHeight(Height) is True:
        print("Height", int(Height))
        break
    else:
        print("Are you that tall? come on...")


while True:
    Weight = input("Please enter your weight in kilograms as a whole number (e.g.:78) > ")
    if validWeight(Weight) is True:
        print("Weight", int(Weight))
        break
    else:
        print("I don't know if i am nor wearing my glasses today but that doesn't seem like your weight, am i right?")


WeightForCalorie = int(Weight)
AgeForCalorie = int(Age)
HeightForCalorie = int(Height)

if gender == "M":
    men_calories_to_burn = men_calories_calculator(WeightForCalorie,HeightForCalorie,AgeForCalorie)
    print("Your burning calorie per day is of", round(men_calories_to_burn))
elif gender == "F":
    women_calories_to_burn = woman_calories_calculator(WeightForCalorie, HeightForCalorie, AgeForCalorie)
    print("Your burning calorie per day is of", round(women_calories_to_burn))
else: pass


#startin with your breackfast
print("\n\nSo, let's get started. We will be segguesting different meals for your day ingest."
        "Each option is based on a basic serving size but you can order it twice if you love it!\n ")

#Creating a class for food in order to store more than 1 value.
# Source: https://whatscookingamerica.net/NutritionalChart.htm
if men_calories_to_burn != 0:
    calories_to_burn = men_calories_to_burn
if women_calories_to_burn != 0:
    calories_to_burn = women_calories_to_burn

calories_left = round(calories_to_burn)


breakfast_foods = []
open_a_menu_csv('foodfb.csv',breakfast_foods)
breakfast_of_the_day = ""

print("Breakfast Menu:")
for food in breakfast_foods:
    print(food.name,"("+food.serving_size+"):", food.calorie, "calories")

#for each food in your food list check if the food.name is equal to the input string


while True:
    #breakfastime!
    bf_choice = input("Current Breakfast:What are you having for breakfast? (if you want to go to the next meal type 'next meal'> ").lower()
    if bf_choice == "next meal":
        no_breakfast = False
        if breakfast_of_the_day == "":
            breakfast_of_the_day = "Nothing"
            no_breakfast = True
        print("Your current breakfast ingestion:", breakfast_of_the_day)
        satisfied = input("Are you satisfied with your current breakfast(say 'no' if you want to do over)").lower()
        if satisfied == "no":
            breakfast_of_the_day = ""
            calories_left = round(calories_to_burn)
        elif satisfied != "no":
            break
    else:
        found = False
        for food in breakfast_foods:
            if food.name == bf_choice:
                calories_left = calories_left - food.calorie
                breakfast_of_the_day =  breakfast_of_the_day + " - " + bf_choice
                print("You have", calories_left, "left to burn. Do you want to have anything else or just:"+ breakfast_of_the_day,"?")
                found = True
        if not found:
            print("Not a valid breakfast choice")



lunch_foods = []
open_a_menu_csv('foodfl.csv',lunch_foods)
lunch_of_the_day = ""

print("\nSo! Starting to get hungry no? These are the food categories for your lunch meal:")

while True:
    #lunchtime!
    segm_choice = input("Choose a food category to fill you in with food options"
                           "(if you want to go to the next meal type 'next meal')> ")
    if segm_choice == "next meal":
        no_lunc = False
        if lunch_of_the_day == "":
            lunch_of_the_day = "Nothing"
            no_lunch = True
        print("Your current lunch ingestion:", lunch_of_the_day)
        satisfied = input("Are you satisfied with your current lunch(say 'no' if you want to do over)").lower()
        if satisfied == "no":
            lunch_of_the_day = ""
            calories_left = round(calories_to_burn)
        elif satisfied != "no":
            break
    else:
        found = False
        for food in lunch_foods:
            if food.segment == segm_choice:
                print(food.name,"("+food.serving_size+"):", food.calorie, "calories")
                found = True
                if not found:
                    print("Not a valid lunch choice")
        if found:
            found = False
            lunch_choice = input("What's your choice for lunch?")
            for food in lunch_foods:
                if food.name == lunch_choice:
                    calories_left = calories_left - food.calorie
                    lunch_of_the_day = lunch_of_the_day + " - " + lunch_choice
                    print("You have", calories_left,
                          "left to burn. Do you want to have anything else or just:" + lunch_of_the_day, "?")
                    found = True
        if not found:
            print("not a valid category")


menu_of_the_day = breakfast_of_the_day + lunch_of_the_day
print("These is your current menu of the day:", menu_of_the_day)
