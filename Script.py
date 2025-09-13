import pandas as pd
import random

# Sample states & cities
states_cities = {
    "California": ["Los Angeles", "San Francisco", "San Diego"],
    "Texas": ["Dallas", "Houston", "Austin"],
    "New York": ["New York City", "Buffalo", "Rochester"],
    "Florida": ["Miami", "Orlando", "Tampa"],
    "Illinois": ["Chicago", "Springfield", "Naperville"]
}

years = list(range(2015, 2023))
data_prices = []
data_demo = []

property_id = 1000

for state, cities in states_cities.items():
    for city in cities:
        # demographics data (static per city)
        household_income = random.randint(40000, 90000)
        population_growth = round(random.uniform(0.5, 3.0), 2)
        data_demo.append([city, state, population_growth, household_income])
        
        # yearly housing data
        for year in years:
            property_id += 1
            median_price = random.randint(200000, 900000)
            mortgage_rate = round(random.uniform(3.0, 6.0), 2)
            data_prices.append([property_id, state, city, year, median_price, mortgage_rate])

# Convert to DataFrames
df_prices = pd.DataFrame(data_prices, columns=["Property_ID", "State", "City", "Year", "Median_House_Price", "Mortgage_Rate"])
df_demo = pd.DataFrame(data_demo, columns=["City", "State", "Population_Growth", "Household_Income"])

# Save CSV files
df_prices.to_csv("housing_prices.csv", index=False)
df_demo.to_csv("demographics.csv", index=False)

print("CSV files generated: housing_prices.csv, demographics.csv")
