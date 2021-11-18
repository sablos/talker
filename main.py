again = True
while again:
  name = input("Who should I say hello to?: ")
  times = int(input("How many times should I say hello? "))
  for i in range(times):
    print(f"Hello {name}!")
  print()
  choice = input("Say hello to someone else? (y/n) ")
  if choice != "y":
    again = False