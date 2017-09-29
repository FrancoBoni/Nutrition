from NutritionTheory import *

print("Hi! welcome to \033[1m\"Cheff Malony!\"\033[0;0m"" - "
      "The first chat bot that suggests meals based on your calories to burn "
      "like a nutrition doctor.\nPlease, answer the following 4 questions in order to know your calories to burn.\n\n")
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
while True:
    Age = input("Please enter your age > ")
    if validAge(Age) is True:
        print("Age", int(Age))
        break
    else:
        print("That can't be right, can it?")

#validate height
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
    print("\nYour burning calorie per day is of", round(men_calories_to_burn),".")
elif gender == "F":
    women_calories_to_burn = woman_calories_calculator(WeightForCalorie, HeightForCalorie, AgeForCalorie)
    print("\nYour burning calorie per day is of", round(women_calories_to_burn),".")
else: pass


#startin with your breackfast
print("\n\nSo, let's get started. We will be segguesting different meals for your day ingest.\n"
        "Each option is based on a basic serving size but you can order it twice if you love it!"
        "Just type the name of the meal you want to have for us to process your order.\n ")


if men_calories_to_burn != 0:
    calories_to_burn = men_calories_to_burn
if women_calories_to_burn != 0:
    calories_to_burn = women_calories_to_burn

calories_left = round(calories_to_burn)
stop = False

breakfast_foods = []
open_a_menu_csv('foodfb.csv',breakfast_foods)
breakfast_of_the_day = ""

print("\033[4mBreakfast Menu (all fruits have fresh values):\033[0m")
for food in breakfast_foods:
    print(food.name,"("+food.serving_size+"):", food.calorie, "calories")

#for each food in your food list check if the food.name is equal to the input string

#breakfastime!

while True:
    calorie_limit(calories_left)
    if stop is True:
        print("\nYour final meal of the day is:", breakfast_of_the_day)
        break
    else:
        bf_choice = input("\nWhat are you having for breakfast?"
                          "(if you want to go to the next meal type 'next meal'> ").lower()
        if bf_choice == "next meal":
            no_breakfast = False
            if breakfast_of_the_day == "":
                breakfast_of_the_day = "Nothing"
                no_breakfast = True
            print("Your current breakfast ingestion:", breakfast_of_the_day)
            satisfied = input("Are you satisfied with your current breakfast(say 'no' to do over and "
                              "'yes' to go the the next meal)>").lower()
            if satisfied == "no":
                breakfast_of_the_day = ""
                calories_left = round(calories_to_burn)
            if satisfied == "yes":
                break
            elif satisfied != "no" or "yes":
                print("not a valid input")
        else:
            found = False
            for food in breakfast_foods:
                if food.name == bf_choice:
                    calories_left = calories_left - food.calorie
                    breakfast_of_the_day =  breakfast_of_the_day + " - " + bf_choice
                    print("You have", calories_left, "left to burn. Do you want to have anything else or just:"
                          + breakfast_of_the_day,"?>")
                    found = True
            if not found:
                print("Not a valid breakfast choice")

calories_to_burn = calories_left


# lunchtime!
lunch_foods = []
open_a_menu_csv('foodfl.csv',lunch_foods)
lunch_of_the_day = ""

print("\033[4m\nStarting to get hungry no? These are the food categories for your lunch meal:\033[0m")
for food in segments:
    print(food)

while True:
    calorie_limit(calories_left)
    if stop is True:
        print("\nYour final meal of the day is:", "\nBreakfast:",breakfast_of_the_day, "\nLunch:", lunch_of_the_day)
        break
    else:
        segm_choice = input("\nWhat are you having for lunch? you will find options for foods within each category"
                           "(if you want to go to the next meal type 'next meal')> ")
        if segm_choice == "next meal":
            no_lunch = False
            if lunch_of_the_day == "":
                lunch_of_the_day = "Nothing"
                no_lunch = True
            print("Your current lunch ingestion:", lunch_of_the_day)
            satisfied = input("Are you satisfied with your current lunch(say 'no' to do over and "
                              "'yes' to go the the next meal").lower()
            if satisfied == "no":
                lunch_of_the_day = ""
                calories_left = round(calories_to_burn)
            if satisfied == "yes":
                break
            elif satisfied != "no" or "yes":
                print("not a valid input")
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
                lunch_choice = input("\nWhat food are you having for lunch?>")
                for food in lunch_foods:
                    if food.name == lunch_choice:
                        calories_left = calories_left - food.calorie
                        lunch_of_the_day = lunch_of_the_day + " - " + lunch_choice
                        print("You have", calories_left,
                              "left to burn. Do you want to have anything else or just:" + lunch_of_the_day, "?>")
                        found = True
            if not found:
                print("not a valid input")

calories_to_burn = calories_left
print("\nBreakfast:",breakfast_of_the_day, "\nLunch:", lunch_of_the_day)

tea_foods = []
open_a_menu_csv('foodfb.csv',tea_foods)
tea_of_the_day = ""

print("\033[4m\nAre you one of those people who grabs something to eat at tea-time? here are some options:\033[0m")


#Tea-Time!
while True:
    calorie_limit(calories_left)
    if stop is True:
        print("\nYour final meal of the day is:", "\nBreakfast:",breakfast_of_the_day, "\nLunch:", lunch_of_the_day,
              "\nTea-time:",tea_of_the_day)
        break
    else:
        tt_choice = input("\nWhat are you having for tea-time? "
                          "(if you want to go to the next meal type 'next meal'> ").lower()
        if tt_choice == "next meal":
            no_tea_time = False
            if tea_of_the_day == "":
                tea_of_the_day = "Nothing"
                no_tea_time = True
            print("Your current tea-time ingestion:", tea_of_the_day)
            satisfied = input("Are you satisfied with your current tea-time? (say 'no' to do over and "
                              "'yes' to go the the next meal)>").lower()
            if satisfied == "no":
                tea_of_the_day = ""
                calories_left = round(calories_to_burn)
            if satisfied == "yes":
                break
            elif satisfied != "no" or "yes":
                print("not a valid input")
        else:
            found = False
            for food in tea_foods:
                if food.name == tt_choice:
                    calories_left = calories_left - food.calorie
                    tea_of_the_day =  tea_of_the_day + " - " + tt_choice
                    print("You have", calories_left, "left to burn. "
                        "Do you want to have anything else or just:"+ tea_of_the_day,"?>")
                    found = True
            if not found:
                print("Not a valid tea-time choice")

calories_to_burn = calories_left
print("\nBreakfast:",breakfast_of_the_day,"\nLunch:",lunch_of_the_day,"\nTea-time:",tea_of_the_day)

# Dinner!
dinner_foods = []
open_a_menu_csv('foodfl.csv',dinner_foods)
dinner_of_the_day = ""

print("\033[4m\nLast meal of the day! These are the food categories for your lunch meal:\033[0m")
for food in segments:
    print(food)

while True:
    calorie_limit(calories_left)
    if stop is True:
        print("\nBreakfast:",breakfast_of_the_day,"\nLunch:",lunch_of_the_day,"\nTea-time:",tea_of_the_day,
              "Dinner:",dinner_of_the_day)
        break
    else:
        segm_choice = input("\nWhat are you having for dinner? you will find options for foods within each category"
                           "(if you want to go to finish type 'finished')> ")
        recommendation_warning(segm_choice, "chocolates")
        recommendation_warning(segm_choice,"meats")
        if segm_choice == "finished":
            no_dinner = False
            if dinner_of_the_day == "":
                dinner_of_the_day = "Nothing"
                no_dinner = True
            print("Your current dinner ingestion:", dinner_of_the_day)
            satisfied = input("Are you satisfied with your current dinner(say 'no' to do over and "
                              "'yes' to go the the next meal)>").lower()
            if satisfied == "no":
                dinner_of_the_day = ""
                calories_left = round(calories_to_burn)
            if satisfied == "yes":
                break
            elif satisfied != "no" or "yes":
                print("not a valid input")
        else:
            found = False
            for food in dinner_foods:
                if food.segment == segm_choice:
                    print(food.name,"("+food.serving_size+"):", food.calorie, "calories")
                    found = True
                    if not found:
                        print("Not a valid dinner choice")
            if found:
                found = False
                dinner_choice = input("\nWhat food are you having for dinner?>")
                for food in dinner_foods:
                    if food.name == dinner_choice:
                        calories_left = calories_left - food.calorie
                        dinner_of_the_day = dinner_of_the_day + " - " + dinner_choice
                        print("You have", calories_left,
                              "left to burn. Do you want to have anything else or just:" + dinner_of_the_day, "?")
                        found = True
            if not found:
                print("not a valid input")


print("\033[4m\nYour final menu of the day is:\033[0m"
      "\nBreakfast:",breakfast_of_the_day,"\nLunch:",lunch_of_the_day,"\nTea-time:",tea_of_the_day,
              "\nDinner:",dinner_of_the_day)
