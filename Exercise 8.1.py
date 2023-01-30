y = 0
z = 0
p = 0

while True:
  x = input("Throw the coin and enter head or tail here: ")

  if (x == "head"):
    y = y + 1
    z = z+1
    print(z/y * 100)
    
  else:
    y = y+1
    p = p+1
    print(p/y * 100)