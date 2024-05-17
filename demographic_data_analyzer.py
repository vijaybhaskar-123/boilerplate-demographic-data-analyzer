import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df =pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.

    race_count = df.race.value_counts()

    # What is the average age of men?
    maleValues=df.query('sex in ["Male"]')
    age=maleValues['age'].mean()
    average_age_men = round(age,1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelorscount=df.query('education in ["Bachelors"]')
  

    percentage_bachelors=round((len(bachelorscount)/len(df))*100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higherEducation=df.query('education in ["Bachelors","Masters","Doctorate"]')
    higherThan50k=len(higherEducation.query('salary in [">50K"]'))
   
    paramaters=["Bachelors","Masters","Doctorate"]

    higher_education = len(df.query('education in ["Bachelors","Masters","Doctorate"]'))
    lower_education = df[~df.education.isin(paramaters)]
    lower_education50k=lower_education.query('salary in [">50K"]')

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    higher_education_rich = round((higherThan50k/higher_education)*100,1)
    lower_education_rich = round((len(lower_education50k)/len(lower_education))*100,1)
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    
    min_work_hours = df["hours-per-week"].min()
    min_work_hours_people=df[df["hours-per-week"]==min_work_hours]
    
    min_work_hours_people_earn50k=len(min_work_hours_people[min_work_hours_people["salary"]==">50K"])
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    

    num_min_workers = len(df[df["hours-per-week"]==min_work_hours])
    
    

    rich_percentage = round((min_work_hours_people_earn50k/len(min_work_hours_people))*100)

    # What country has the highest percentage of people that earn >50K?
    TotalCount=df['native-country'].value_counts()
    earningabove50k = df[df['salary']==">50K"]
    country_count = earningabove50k['native-country'].value_counts()
    percentage=round((country_count/TotalCount)*100,1)
   
    highest_earning_country_percentage = percentage.max()
    highest_earning_country=percentage.idxmax()


    # Identify the most popular occupation for those who earn >50K in India.
    earnabove50k=df[(df["salary"]==">50K")& (df["native-country"]=="India")]
   
    top_IN_occupation = earnabove50k["occupation"].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
