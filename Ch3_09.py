# (Financial application: payroll) Write a program that reads the following information
# and prints a payroll statement:
# Employee's name (e.g., Smith)
# Number of hours worked in a week (e.g., 10)
# Hourly pay rate (e.g., 9.75)
# Federal tax withholding rate (e.g., 20%)
# State tax withholding rate (e.g., 9%)
# Sample Run:
# Enter employee's name: Smith
# Enter number of hours worked in a week: 10
# Enter hourly pay rate: 9.75
# Enter federal tax withholding rate: 0.20
# Enter state tax withholding rate: 0.09
# Employee Name: Smith
# Hours Worked: 10.0
# Pay Rate: $9.75
# Gross Pay: $97.5
# Deductions:
#     Federal Withholding (20.0%): $19.5
#     State Withholding (9.0%): $8.77
#     Total Deduction: $28.27
# Net Pay: $69.22

employeeName = input("Enter employee name: ")

noHoursWorkedperWeek = eval(input("Enter number of hours worked per week: "))

hourlyPayRate = eval(input("Enter the hourly pay rate:"))

strHourlyPayRate = '$' + str(hourlyPayRate)

federalTaxWithholdingRate = eval(input("Enter the Federal Tax withholding rate (in percentage): "))

stateTaxWithholdingRate = eval(input("Enter the State Tax withholding rate (in percentage): "))

grossPayPerWeek = noHoursWorkedperWeek * hourlyPayRate

strGrossPayPerWeek = '$' + str(grossPayPerWeek)

federalWithholding = (federalTaxWithholdingRate) * grossPayPerWeek

stateWithholding = (stateTaxWithholdingRate) * grossPayPerWeek

totalDeduction = federalWithholding + stateWithholding

netPayPerWeek = grossPayPerWeek - totalDeduction

print("********************Payroll Application************************")

print("Employee Name:", employeeName)

print("Hours Worked:", noHoursWorkedperWeek)

print("Hourly Pay Rate: ", strHourlyPayRate)

print("Gross Pay: ", strGrossPayPerWeek)

print("Deductions:")

print("\tFederal Withholding (", federalTaxWithholdingRate * 100, "% ): ", ('$' + format(federalWithholding, "<10.2f")))

print("\tState Withholding (", stateTaxWithholdingRate * 100, "% ): ", ('$' + str(format(stateWithholding,"<10.2f"))))

print("\tTotal Deduction: ", ('$' + str(format(totalDeduction, "<10.2f"))))

print("Net Pay: ", ('$' + str(format(netPayPerWeek, "<10.2f"))))

