# Project: Life Expectancy Data Analysis
# Author : Joshua Ariyo
# Description: A Python Program That Helps The User Analyse A Dataset Of Life Expectancy.
# Date: 10/12/2025

data = []
# Open the file
with open("life-expectancy.csv") as life_expectancy_file:
    next(life_expectancy_file)  # Skip the header line
    for line in life_expectancy_file:
        parts = line.strip().split(",")

        entity = parts[0]
        entity_code = parts[1]
        year = int(parts[2])
        life_expectancy = float(parts[3])
        data.append((entity, entity_code, year, life_expectancy))

print("Welcome to the Life Expectancy Analyzer!")
print("Type 'stop' at any time to quit.\n")

# Initial variables for overall highest & lowest dataset
overall_max_life = -1
overall_max_country = ""
overall_max_year = 0
overall_min_life = 999
overall_min_country = ""
overall_min_year = 0

# Finds the highest and lowest values in the entire dataset
for entity, entity_code, year, life_expectancy in data:
    if life_expectancy > overall_max_life:
        overall_max_life = life_expectancy
        overall_max_country = entity
        overall_max_year = year

    if life_expectancy < overall_min_life:
        overall_min_life = life_expectancy
        overall_min_country = entity
        overall_min_year = year
# Loop the program until user types stop
while True:
    user_input = input("Enter the year of interest (or type 'stop' to exit): ")

    if user_input.lower() == "stop":
        print("Program Stopped. Goodbye!")
        break

    if not user_input.isdigit():
        print("Please enter a valid year or 'stop' to quit.\n")
        continue

    year_of_interest = int(user_input)

    # Initial variables for that specific year
    year_highest = -1
    year_lowest = 999
    year_total = 0
    year_count = 0
    year_highest_country = ""
    year_lowest_country = ""

    # Finds the Average, Highest, and Lowest values for that year
    for entity, entity_code, year, life_expectancy in data:
        if year == year_of_interest:
            year_total += life_expectancy
            year_count += 1

            if life_expectancy > year_highest:
                year_highest = life_expectancy
                year_highest_country = entity

            if life_expectancy < year_lowest:
                year_lowest = life_expectancy
                year_lowest_country = entity

    if year_count > 0:
        year_average = year_total / year_count
        print(f"\nFor the year {year_of_interest}:")
        print(f"  Average Life Expectancy: {year_average:.2f}")
        print(f"  Highest Life Expectancy: {year_highest:.2f} from {year_highest_country}")
        print(f"  Lowest Life Expectancy:  {year_lowest:.2f} from {year_lowest_country}\n")
    else:
        print(f"No data found for the year {year_of_interest}.\n")

# Print overall stats at the end
print()
print(f"The Overall Max Life Expectancy is: {overall_max_life:.2f} from {overall_max_country} in {overall_max_year}.")
print(f"The Overall Min Life Expectancy is: {overall_min_life:.2f} from {overall_min_country} in {overall_min_year}.")
