print("Hi! welcome to \"Cheff Malony!\" - The first chat bot that suggests meals based on your calories to burn. "
      "like a nutrition doctor.\nPlease, answer the following 4 questions in order to know your calories to burn.\n\n ")


#validate Gender
while True:
    Gender = input("Please enter your gender (\"M\" for Male \"F\" for Female): ").upper()
    if Gender == "M":
        print('Gender: Male')
        break
    if Gender == "F":
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
    Age = input("Please enter your age: ")
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
    Height = input("Please enter your height in centimetres(e.g.:172): ")
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
    Weight = input("Please enter your weight in kilograms as a whole number (e.g.:78): ")
    if validWeight(Weight) is True:
        print("Weight", int(Weight))
        break
    else:
        print("I don't know if i am nor wearing my glasses today but that doesn't seem like your weight, am i right?")


#calorie count
WeightForCalorie = int(Weight)
AgeForCalorie = int(Age)
HeightForCalorie = int(Height)

def mencalories(weight,height,age):
    men = 10*weight + 6.25*height - 5*age + 5
    return men

def womancalories(weight,height,age):
    woman = 10*weight + 6.25*height - 5*age - 161
    return woman

if Gender == "M":
    MenCaloriesToBurn = mencalories(WeightForCalorie,HeightForCalorie,AgeForCalorie)
    print("Your burning calorie per day is of", round(MenCaloriesToBurn))
elif Gender == "F":
    WomenCaloriesToBurn = womancalories(WeightForCalorie, HeightForCalorie, AgeForCalorie)
    print("Your burning calorie per day is of", round(WomenCaloriesToBurn))
else: pass


#startin with your breackfast
print("\n\nSo, let's get started. We will be segguesting different meals for your meals. "
      "\nStart telling us what would you like to have for breakfast\n\n ")

Creating a class for food in order to store more than 1 value.
# Source: https://whatscookingamerica.net/NutritionalChart.htm



class Food:
    def __init__(self, name, calorie, size, unit, healthiness):
        self.name = name
        self.calorie = calorie
        self.size = size
        self.unit = unit
        self.healthiness = healthiness

bread = Food("Bread", 90, 1, "ounce", "good")
yogourt = Food("Yogourt", 80, 1, "ounce", "good")

Breakfast_list = ("Yogourt","Bread")
calorie = 2000

def getfoodpercalorie
    
    

while True:
    bf_choice = input("What are you having for breakfast? ")
    if bf_choice.title() in Breakfast_list:
        
        calorie_left = calorie - calorie(bf_choice)
        print(calorie_left)
        print("Would you have anything else? ")
    elif bf_choice == "nothing else":
        break
    else:continue
