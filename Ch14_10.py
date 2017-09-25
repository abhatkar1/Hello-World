# (Guess the capitals) Rewrite Exercise 11.40 using a dictionary to store the pairs
# of states and capitals so that the questions are randomly displayed.

#11.40
# Guess the capitals) Write a program that repeatedly prompts the user to enter a
# capital for a state. Upon receiving the user input, the program reports whether
# the answer is correct. Assume that 50 states and their capitals are stored in a twodimensional
# list, as shown
# in Figure 11.13. The program prompts the user to
# answer
# all the states’ capitals and displays the total correct count. The user’s
# answer
# is not case sensitive.
# Implement the program using a list to represent the
# data
# in the following
# table.

import random

countryCapitals = {
"Afghanistan":"Kabul",
"Albania":"Tirana",
"Algeria":"Algiers",
"Andorra":"Andorra la Vella",
"Angola":"Luanda",
"Antigua and Barbuda":"Saint John's",
"Argentina":"Buenos Aires",
"Armenia":"Yerevan",
"Australia":"Canberra",
"Austria":"Vienna",
"Azerbaijan":"Baku",
"Bahamas":"Nassau",
"Bahrain":"Manama",
"Bangladesh":"Dhaka",
"Barbados":"Bridgetown",
"Belarus":"Minsk",
"Belgium":"Brussels",
"Belize":"Belmopan",
"Benin":"Porto-Novo",
"Bhutan":"Thimphu",
"Cabo Verde":"Praia",
"Cambodia":"Phnom Penh",
"Cameroon":"Yaounde",
"Canada":"Ottawa",
"Central African Republic":"Bangui",
"Chad":"N'Djamena",
"Chile":"Santiago",
"China":"Beijing",
"Colombia":"Bogotá",
"Comoros":"Moroni",
"Democratic Republic of theCongo":"Kinshasa",
"Republic of the Congo":"Brazzaville",
"Costa Rica":"San Jose",
"Cote d'Ivoire":"Yamoussoukro",
"Croatia":"Zagreb",
"Cuba":"Havana",
"Cyprus":"Nicosia",
"Czech Republic":"Prague",
"Iceland":"Reykjavik",
"India":"New Delhi",
"Indonesia":"Jakarta",
"Iran":"Tehran",
"Iraq":"Baghdad",
"Ireland":"Dublin",
"Israel":"Jerusalem",
"Italy":"Rome",
"Taiwan":"Taipei",
"Tajikistan":"Dushanbe",
"Tanzania":"Dodoma",
"Thailand":"Bangkok",
"Timor-Leste":"Dili",
"Togo":"Lomé",
"Tonga":"Nukuʻalofa",
"Trinidad and Tobago":"Port of Spain",
"Tunisia":"Tunis",
"Turkey":"Ankara",
"Turkmenistan":"Ashgabat",
"Tuvalu":"Funafuti"
}

print("*************Game: Guess the capital*************")

correctAnswers = 0
listOfCountries = list(countryCapitals.keys())
count = 0
alreadyAsked = []
while count < 10:
    randomNumber = random.randrange(0, len(listOfCountries))
    key = listOfCountries[randomNumber]
    if key not in alreadyAsked:
        alreadyAsked.append(key)
        answer = input(str(count + 1) + ". What is the capital of " + key + " ?")
        if answer.lower() == countryCapitals[key].lower():
            correctAnswers += 1
            print("Correct.")
        else:
            print("Wrong. Correct answer is", countryCapitals[key])
        count += 1
print()
print("Out of 10, you got", correctAnswers, "correct.")
