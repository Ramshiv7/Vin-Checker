class Car:
    def __init__(self):
        print('Vin Checker')


    def tata(self):
        print(f'TATA car vin check : {chassis} and {len(chassis)}')

        tata_year = {"A" : "2010","B" : "2011",
        "C" : "2012",
        "D" : "2013",
        "E" : "2014",
        "F" : "2015",
        "G" : "2016",
        "H" : "2017",
        "J" : "2018",
        "K" : "2019",
        "L" : "2020",
        "M" : "2021",
        "N" : "2022",
        "P" : "2023",
        "R" : "2024",
        "S" : "2025",
        "T" : "2026",
        "V" : "2027",
        "W" : "2028",
        "X" : "2029",
        "Y" : "2030"}

        tata_month = {"A" : "JAN",
        "B" : "FEB",
        "C" : "MAR",
        "D" : "APR",
        "E" : "MAY",
        "F" : "JUN",
        "G" : "JUL",
        "H" : "AUG",
        "J" : "SEP",
        "K" : "OCT",
        "N" : "NOV",
        "P" : "DEC"}

        if len(chassis) != 17 and chassis[:3] != 'MAT':
            print('Invalid Chassis ')
        else:
            print('Valid Chassis')
            year_val = chassis[9]
            month_val = chassis[11]

            result = f'Car is Manufactured in the month of {tata_month[month_val]} of the Year {tata_year[year_val]}'
            print(result)


    def chevy(self):

        chevy_trailblaze_month = {
"A" : "JAN",
"B" : "FEB",
"C" : "MAR",
"D" : "APR",
"F" : "MAY",
"G" : "JUN",
"H" : "JUL",
"K" : "AUG",
"M" : "SEP",
"N" : "OCT",
"P" : "NOV",
"P" : "DEC"
        }

        chevy_month = {
"A" : "JAN",
"B" : "FEB",
"C" : "MAR",
"D" : "APR",
"E" : "MAY",
"F" : "JUN",
"G" : "JUL",
"H" : "AUG",
"J" : "SEP",
"K" : "OCT",
"L" : "NOV",
"M" : "DEC"}

        chevy_year = {
"A" : "2010",
"B" : "2011",
"C" : "2012",
"D" : "2013",
"E" : "2014",
"F" : "2015",
"G" : "2016",
"H" : "2017",
"J" : "2018",
"K" : "2019",
"L" : "2020",
"M" : "2021",
"N" : "2022",
"P" : "2023",
"R" : "2024",
"S" : "2025",
"T" : "2026",
"V" : "2027",
"W" : "2028",
"X" : "2029",
"Y" : "2030"}

        if len(chassis) !=17 and ( chassis[:3] != 'MA6' or chassis[:3] != 'MMM'):
            print("Invalid Chassis for Chevrolet")
        elif len(chassis) == 17 and chassis[:3] == "MA6":

            print("Valid Chassis/ Vin Number")
            year_val = chassis[8]
            month_val = chassis[10]

            result = f'Car is Manufactured in the month of {chevy_month[month_val]} of the Year {chevy_year[year_val]}'
            print(result)
        elif len(chassis) == 17 and chassis[:3] == "MMM":
            print('Look !, we got a Trailblazer !!!!')

            month_val = chassis[5]
            year_val = chassis[10]

            result = f'Car is Manufactured in the month of {chevy_trailblaze_month[month_val]} of the Year {chevy_year[year_val]}'
            print(result)
        


    def honda(self):
        pass
 

make = input('Enter your car make')

chassis = input('Enter the Chassis ').upper()

x = Car

if make.lower() == "tata":
    x.tata(chassis)
elif make.lower() == "chevrolet":
    x.chevy(chassis)
else:
    print('invlaid Make ')

