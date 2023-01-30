def convert(liters):
  cubic = liters / 1000
  return cubic
  
liters = float(input("Enter liters: "))
print(convert(liters))