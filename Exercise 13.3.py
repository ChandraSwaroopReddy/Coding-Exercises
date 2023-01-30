def year(year_of_birth, current_year=2022):
  age = current_year - year_of_birth 
  return age

year_of_birth = int(input("What is your year of birth? "))
result = year(year_of_birth)
print(result)

if result > 120:
  print("Wow")
else:
  print("Healthy")
