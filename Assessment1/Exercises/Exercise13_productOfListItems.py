#Write a program that passes a list as an argument to a function. 
# The function should then calculate the product (values multiplied) of the list values 
# and return this value back to the main program.

#making a function where you need to type the name of the list inside the brackets when you call it
def multiply_list(listx):
    #can't write 0 because anything multiplied by 0 is 0 but the answer will be same if it's 1
    prod=1
    #using a for loop and making a variable for each element in list to be multiplied with prod
    #the prod variable will be multiplied with each element
    #so it will be like 1x6x2x9x4
    for element in listx:
        prod *= element
    #after the for loop ends and the prod variable is multiplied by all the elements
    #returning the prod variable to the user
    return prod

#making my own list
my_list=[6,2,9,4]
#printing the answer by calling function
print(multiply_list(my_list))