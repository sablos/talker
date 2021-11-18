import time, random

def talk(statement):
  time.sleep(1)
  print()
  print("< ~ " + statement)

def listen():
  print()
  return input(">>> ")

greetings = ["Hello", "Hi", "Good day", "What's up"]

# program intro
print("This program says hello to the person of your choice")
print()
again = True
while again:
  talk("Who should I say hello to?: ")
  name = listen()
  talk("How many times should I say hello? ")
  times = listen()
  # check if times is a valid number with isdigit()
  if times.isdigit():
    times = int(times)
    for i in range(times):
      talk(f"{random.choice(greetings)}, {name}!")
  else:
    talk("You didn't enter a number so I'll say hello once")
    talk(f"{random.choice(greetings)}, {name}!")
  print()
  talk("Say hello to someone else? (y/n) ")
  choice = listen()
  if choice != "y":
    again = False