from datetime import datetime

def get_days_from_today(date):

# create today date
  date_today = datetime.today().date()
 
# create input date, exeptions
  try:
    input_date = datetime.strptime(date, "%Y.%m.%d").date()

  except ValueError: 
    print("Wrong date forrmat. Try to use 'YYYY.MM.DD'")
  
# count difference
  delta =  date_today - input_date

# return the result
  return delta.days
  

print(get_days_from_today("2012.10.11"))
  


# why I can't see in terminal if I put return, only print



    