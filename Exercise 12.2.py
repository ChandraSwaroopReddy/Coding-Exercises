def con(password):
  
  x = {}
  
  if (len(password)>7):
    x["length"] = True
  else:
    x["length"] = False
  
  x["uppercase"] = False
  for i in password:
    if i.isupper():
      x["uppercase"] = True
  
  x["digit"] = False    
  for i in password:
    if i.isdigit():
      x["digit"] = True
      
  if all(x.values()):
    return "Strong Password"
  else:
    return 'Weak Password'
  return y


password = input("Enter new password: ")
print(con(password))