with open("README.md", "a") as file:
  if file:
    newText = input("Changes?\nR: ")
    if newText:
      file.write(newText)
  

with open("README.md", "r") as file:
  print(file.read())