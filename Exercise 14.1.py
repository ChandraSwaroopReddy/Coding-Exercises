def temp(temperature):
  if temperature <= 0:
    return "Solid"
  elif temperature > 0 and temperature < 100:
    return "Liquid"
  else:
    return "Gas"


temperature = int(input("Enter water temperature: "))
print(temp(temperature))