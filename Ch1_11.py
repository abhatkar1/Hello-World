'''
1.11 (Population projection) The US Census Bureau projects population based on the
    following assumptions:
        One birth every 7 seconds
        One death every 13 seconds
        One new immigrant every 45 seconds
    Write a program to display the population for each of the next five years. Assume the
    current population is 312032486 and one year has 365 days. Hint: in Python, you
    can use integer division operator // to perform division. The result is an integer. For
    example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
'''
Curr_pop = 312032486
Sec_in_year = 365*24*3600
Sec_per_death = 13
Sec_per_birth = 7
Sec_per_immi = 45


births_in_a_year = Sec_in_year // Sec_per_birth 
deaths_in_a_year = Sec_in_year // Sec_per_death 
immi_in_a_year = Sec_in_year // Sec_per_immi 

Pop_increase_per_year = immi_in_a_year + births_in_a_year - deaths_in_a_year 

for i in range(1, 6):
    print("Population after", i, "year: ", (Curr_pop + i*Pop_increase_per_year))
