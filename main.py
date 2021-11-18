again = True
while again:
  name = input("Who should I say hello to?: ")
  times = input("How many times should I say hello? ")
  # check if times is a valid number
  if times.isdigit():
    times = int(times)
    for i in range(times):
      print(f"Hello {name}!")
  else:
    print("You didn't enter a number so I'll say hello once")
    print(f"Hello {name}!")
  print()
  choice = input("Say hello to someone else? (y/n) ")
  if choice != "y":
    again = False