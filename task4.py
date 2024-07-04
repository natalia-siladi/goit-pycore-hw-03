from datetime import datetime, timedelta

def get_upcoming_birthdays(users):

    # getting current date
    date_today = datetime.today().date()
    bithday_guys_list = []

    for user in users:
        # changing year to current one
        name = user["name"]
        
        #changing year of birth to current one
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        congr_birthday_date = birthday_date.replace(year = date_today.year)
        
        # changing year to next one
        if congr_birthday_date < date_today:
            congr_birthday_date = congr_birthday_date.replace(date_today.year + 1)
            

        days_delta = (congr_birthday_date - date_today).days
        week_delta = timedelta(days=7) 
        
        if 0 <= days_delta <= week_delta.days:
            
            #Checking if it's weekend and setting a new day of congratulation
            day_of_week = congr_birthday_date.weekday()

            if day_of_week >= 5:
                days_until_monday = 7 - day_of_week
                upcoming_birthdays_date = congr_birthday_date + timedelta(days = days_until_monday)
            else:
                upcoming_birthdays_date = congr_birthday_date    

            bithday_guys_list.append({"name":name, "congratulation_date": upcoming_birthdays_date.strftime("%Y.%m.%d")})

    return bithday_guys_list     

             
# example
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Anastasia Siladi", "birthday": "2006.07.22"},
    {"name": "Anisia Siladi", "birthday": "2006.07.05"},
    {"name": "Afanasii Siladi", "birthday": "2008.07.06"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)             
            
