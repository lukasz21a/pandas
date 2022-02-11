import pandas as pd


# Read data from file
df = pd.read_csv("data.csv")

# How many of each race are represented in this dataset
race_count = df['race'].value_counts()

# The average age of men
average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

# The percentage of people who have a Bachelor's degree
percent_bachelors = round(df['education'].value_counts(normalize=True)
                          ['Bachelors'] * 100, 1)

# What percentage of people with advanced education 
# (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K
higher_edu = (df['education'] == 'Bachelors') \
             | (df['education'] == 'Masters') \
             | (df['education'] == 'Doctorate')
result = df[higher_edu]['salary'].value_counts(normalize=True)['>50K'] * 100
higher_education_rich = round(result, 1)

# What percentage of people without advanced education make more than 50K
lower_edu = (df['education'] != 'Bachelors') & (df['education'] != 'Masters') \
            & (df['education'] != 'Doctorate')
result2 = df[lower_edu]['salary'].value_counts(normalize=True)['>50K'] * 100
lower_education_rich = round(result2, 1)

# What is the minimum number of hours a person works per week
min_work_hours = df['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K
min_hours = df['hours-per-week'] == min_work_hours
rich_percentage = int(df[min_hours]['salary'].value_counts(normalize=True)['>50K'] * 100)

# What country has the highest percentage of people that earn >50K
country_list = df["native-country"].unique().tolist()
empty_list = [0.0 for _ in range(len(country_list))]
country_frame = pd.DataFrame(index=country_list)
country_frame.insert(0, "percentage", empty_list, True)

for country in country_list:
    native_c = df['native-country'] == country
    percentage = round(df[native_c]['salary'].value_counts(normalize=True)['>50K'] * 100, 1)
    country_frame.at[country, 'percentage'] = percentage

max_percentage = country_frame['percentage'] == country_frame['percentage'].max()
highest_earning_country = country_frame.index[max_percentage][0]
highest_earning_country_percentage = country_frame['percentage'].max()

# Identify the most popular occupation for those who earn >50K in India.
condi3 = (df['native-country'] == 'India') & (df['salary'] == '>50K')
top_IN_occupation = df[condi3].occupation.mode().loc[0]


print("Number of each race:\n", race_count.to_string())
print()
print("Average age of men:", average_age_men)
print(f"Percentage with Bachelors degrees: {percent_bachelors}%")
print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
print(f"Min work time: {min_work_hours} hours/week")
print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
print("Country with highest percentage of rich:", highest_earning_country)
print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
print("Top occupations in India:", top_IN_occupation)