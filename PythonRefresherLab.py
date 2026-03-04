#Python Refresher Lab exercise 1: Write a program which computes the doubling time of an asset (or debt) for a
#given (compound) interest rate. Do this using a while and if statement rather than
#with a closed solution such as the 'rule of 72.'

#Initalizing interest rate as a float data type and getting input from user. Iniitalizing rate as 
#defined interest rate divided by 1oo 
interest_rate = float(input("Enter annual interest rate:  "))
rate = interest_rate / 100

#Setting the inital and target amounts; initial amount is set to 1$ and target amount is 
#set to double the initial amount (goal is see how many years it would take to reach twice the money).
initial_amount = 1.0 
target_amount = initial_amount * 2
current_amount = initial_amount 
years = 0 

#While loop runs if current amount is less than the target 2x original. 
while current_amount < target_amount:
    #adding interest to the current amount; goves total earnings per year, which is then added
    # to current amount 
    current_amount += current_amount * rate 
    #increment years
    years +=1 
#print result
print (f"\n At an annual interest rate of {interest_rate}%, it will take {years} years to double your svaings. ") 
