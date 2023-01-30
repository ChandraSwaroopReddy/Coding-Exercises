def totalnames(names):
  names_list = names.split(',')
  no_names = len(names_list)
  return no_names


names = input("Enter names separated by commas (no spaces): ")
print(totalnames(names))
