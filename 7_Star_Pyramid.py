row = int(input("Enter a number: "))
if row >= 1:
    maxx = row * 2 - 1  # Maximum width of the pyramid
    for i in range(1, row + 1):
        stars = "*" * (2 * i - 1)  # Number of stars in the current row
        print(f'{stars:^{maxx}}')  # Center the stars within the max width
