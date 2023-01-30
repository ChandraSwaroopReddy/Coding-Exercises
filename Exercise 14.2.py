Freezing_point = 0
Boiling_point = 100

def temp(temperature):
  if temperature <= Freezing_point:
    return "Solid"
  elif temperature > Freezing_point and temperature < Boiling_point:
    return "Liquid"
  else:
    return "Gas"


temperature = int(input("Enter water temperature: "))
print(temp(temperature))