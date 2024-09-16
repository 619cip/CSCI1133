hours = int(input('Enter time in hours: '))
print(f'{hours // (24*7)} weeks, {hours % (24*7) // 24} days, and {hours % 24} hours')