totalPrevious = 0
totalInterestExpenses = 0
# totalPrevious and totalInterestExpenses are set to 0 because later totalPrevious += previous and
# totalInterestExpenses += interestExpenses require variables that are declared in advance


year = int(input("Please enter the year that you want to calculate the personal interest rate for: "))
# The user enters an integer year of personal interest

expenditureNumber = int(input("Please enter the number of expenditure categories: "))
# The user enters the integer number of expenditure categories

for i in range(expenditureNumber):
    previous = float(input("Please enter expenses for previous year: "))
    interestExpenses = float(input("Please enter expenses for year of interest: "))
    # The user enters n times the number of expenditure categories and then the computer outputs n times the
    # questions "Please enter the amount spent in the previous year" and "Please enter the amount spent in the year
    # of personal interest"

    totalPrevious += previous
    # Total expenses for previous year

    totalInterestExpenses += interestExpenses
    # Total expenses for year of interest year

    final = (totalInterestExpenses - totalPrevious) / totalInterestExpenses
    # As the rate of inflation is equal to the difference between the total quantity spent in the year of interest
    # and the total quantity spent in the previous year divided by the total quantity spent in the year of interest
    # of the individual

    percentage = "{:.1%}".format(final)
# The percentage sign is added because the inflation rate is a percentage

print("Personal inflation rate for", year, "is", percentage)
# The computer output inflation rate for the year of interest is the difference between the total quantity spent in
# the year of interest entered by the user and the total quantity spent in the previous year divided by the total
# quantity spent in the year of interest


"""
Since the computer has output the inflation rate for the year of interest to the individual, it can identify the type of inflation.
There are four types of inflation, Low Inflation, Moderate, High Inflation, High Inflation and Hyper.
When the computer determines that the inflation rate is equal to the string type 0, the computer outputs Type of Inflation: Low Inflation
When the computer determines that the inflation rate is less than the string type 0.03, the computer outputs Type of Inflation: Low Inflation
When the computer determines that the inflation rate is less than the string type 0.05 and greater than 0.03, the computer outputs Type of Inflation: Moderate
When the computer determines that the inflation rate is less than the string type 0.1 and greater than 0.05, the computer outputs Type of Inflation: High Inflation
When the computer determines that the inflation rate is of a string type other than all of the above, the computer outputs Type of Inflation: Hyper
"""

if percentage == str(0):
    print("Type of Inflation: Low Inflation")
#

elif percentage < str(0.03):
    print("Type of Inflation: Low Inflation")
elif str(0.03) < percentage < str(0.05):
    print("Type of Inflation: Moderate")
elif str(0.05) < percentage < str(0.1):
    print("Type of Inflation: High Inflation")
else:
    print("Type of Inflation: Hyper")
