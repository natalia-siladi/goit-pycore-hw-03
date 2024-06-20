import random

def get_numbers_ticket(min, max, quantity):
  
# checking validity of the entered parameters
  if not(1 <= min <= max <= 1000):
    return []
  if not(1 <= quantity < (max - min)):
    return []
  
#generating a set of unique numbers
  random_numbers = random.sample(range(min, max), quantity)

# sorting the list of numbers
  random_numbers.sort()

  return random_numbers

lottery_numbers = get_numbers_ticket(5, 49, 4)
print("Ваші лотерейні числа:", lottery_numbers)





