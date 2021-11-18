# program intro
print("This program says hello to the person of your choice")
print()
again = True
while again:
  print(" ~ Who should I say hello to?: ")
  name = input(">>> ")
  print(" ~ How many times should I say hello? ")
  times = input(">>> ")
  # check if times is a valid number with isdigit()
  if times.isdigit():
    times = int(times)
    for i in range(times):
      print(f" ~ Hello {name}!")
  else:
    print(" ~ You didn't enter a number so I'll say hello once")
    print(f" ~ Hello {name}!")
  print()
  print(" ~ Say hello to someone else? (y/n) ")
  choice = input(">>> ")
  if choice != "y":
    again = False