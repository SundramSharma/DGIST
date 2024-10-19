pas = input("Make a pasword minimum 8 chars with one uppercase letter, one lowercase, one digt, one special char: ")
if len(pas) >= 8 and any(char.isupper() for char in pas):
                            if any(char.islower() for char in pas):
                              if any(char.isdigit() for char in pas):
                               if any(char in "!@#$%^&*()_+-=" for char in pas):
                                print("True")
else:
        print("False")