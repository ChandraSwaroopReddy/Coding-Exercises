year_of_birth = int(input("What is your year of birth? "))

def year(year_of_birth, current_year=2022):
  age = current_year - year_of_birth
  return age


print(year(year_of_birth))