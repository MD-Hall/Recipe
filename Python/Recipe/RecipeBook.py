# Recipe Book
# Max Hall
# 12 December 2021

from os.path import exists, basename
from os import listdir, remove
from sys import exit


'''Prints out the options that can be chose and returns a user given input''' 
def options():
    print()
    print("\tWould you like to:")
    print("\t(1) Use an existing recipe")
    print("\t(2) Add a new recipe")
    print("\t(3) Edit an existing recipe")
    print("\t(4) Delete an existing recipe")
    print("\t(5) Quit")  
    return input("\t: ")


'''Shows the names of the recipes which are saved''' 
def showRecipes(recipes):
    print("\n\tYour saved recipes are:\n")
    for i in recipes:
        print("\t"+addBackSpaces(i[:-4]))


'''This takes in the choice as well as a list of file names of the saved recipes
and executes whichever task is chosen'''
def followUp(choice):
    global recipes 
    recipes = getSavedRecipes()    
    if choice == '1':
        if len(recipes) > 0: 
            makeRecipe(recipes)
        else:
            print("\n\tThere are no saved recipes to be accessed")
        
    elif choice == '2':
        addRecipe(recipes)
    
    elif choice == '3':
        editRecipe(recipes)
        
    elif choice == '4':
        delRecipe(recipes)    
    
    elif choice == '5':
        print("\tThank you for using 'Your Recipe Book' created by Max Hall")
        exit()
    
    else:
        print("\n\tThis is not a valid choice!")
        followUp(options())
        


'''This shows a recipe which has been pre-saved you pass a list of file names of the saved recipes'''
def makeRecipe(recipesList):
    showRecipes(recipesList)
    recipeName = removeSpaces(input("\n\tWhat would you like to make?\n\t")) + ".txt"
    if recipeName in recipesList:
        print("\n\tThe Recipe for " + addBackSpaces(recipeName)[:-4] + " is:\n")
        try:
            myFile = open(recipeName, 'r')
            for line in myFile:
                print("\t" + line,end = '')
            
        finally:
            print()
            myFile.close()
            input("\tPress enter when you're finished with the recipe")
    else:
        print("\n\tThis is not a saved recipe")

    followUp(options())


'''This writes user input into the file'''
def writingToFile(filename):
    try:
        myFile = open(filename, 'w')
        userInput = ""
        print("\n\tType the recipe line by line and enter DONE when you are finished")
        while userInput != "DONE":
            userInput = input("\t")
            if userInput != "DONE":
                print(userInput, file = myFile)
    finally:
        myFile.close()        


'''This overwrites a saved recipe file'''
def editRecipe(recipesList):
    showRecipes(recipesList)
    recipeName = removeSpaces(input("\n\tWhat's the name of the recipe you wish to overwrite?\n\t")) + ".txt"
    if recipeName in recipesList:
        writingToFile(recipeName)
    else:
        print("\n\tThis is not a saved recipe")

    followUp(options())


'''This adds a saved recipe file'''
def addRecipe(recipesList):
    recipeName = removeSpaces(input("\n\tWhat's the name of the new recipe?\n\t")) + ".txt"
    if recipeName in recipesList:
        choice = input("\n\tThis recipe already exists, do you wish to override it? (Y/N)\n\t")
        while choice != 'Y' and choice != 'N':
            choice = input("\tPlease choose Y or N\n\t")
        if choice == "Y":
            writingToFile(recipeName) 
        else:
            pass
    else:
        writingToFile(recipeName)

    followUp(options())
 
  
'''This deletes a saved recipe file'''  
def delRecipe(recipesList):
    showRecipes(recipesList)
    recipeName = removeSpaces(input("\n\tWhat recipe do you want to delete:\n\t")) + ".txt"
    if recipeName in recipesList:
        choice = input("\n\tAre you sure you want to delete "+ addBackSpaces(recipeName)[:-4] + "? (Y/N)\n\t")
        while choice != 'Y' and choice != 'N':
            choice = input("\tPlease choose Y or N\n\t")
        if choice == "Y":
            remove(recipeName)
            print("\n\tRecipe removed successfully")
        else:
            print("\n\tNo Recipe Removed")
    else:
        print("\n\tThis is not a saved recipe")

    followUp(options())        


'''This replaces any whitespace in a string with a underscore'''
def removeSpaces(String):
    newString = String.replace(" ","_")
    return newString


'''This replaces any underscore in a string with whitespace'''
def addBackSpaces(String):
    newString = String.replace("_"," ")
    return newString


'''This replaces any underscore in a string with whitespace'''
def getSavedRecipes():
    recipes = listdir()
    if ".DS_Store" in recipes:
        recipes.remove(".DS_Store")
    recipes.remove(basename(__file__))
    return recipes


def main():
    print("\n\tWelcome to your Recipe Book")
    print("\t"+"-"*27)
    
    followUp(options())


if __name__ == '__main__':
    main()
