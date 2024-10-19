"""Prime Number Checker"""
num = int(input("Enter a number: "))
if num%num == 0 and num%1 == 0:
  if num != 2:
    if num%2 != 0:
      print("True")
    else:
      print("False")
  else:
    print("True")