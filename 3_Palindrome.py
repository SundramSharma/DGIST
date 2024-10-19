pal = input("Enter a Palindrome: ")
nospacepal = ""
for char in pal:
  if char != " ":
    nospacepal = nospacepal + char.lower()
    
if nospacepal == nospacepal[::-1]:
  print("True")
else:
  print("False")