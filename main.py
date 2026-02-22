import time
import random
from num2words import num2words
from easterEggs import cookies_video, easter_eggs

def guess_yours():
    print("Hello! Please enter a number, any number and I'll be able to guess what it is!")

    try:
        number = int(input("Enter a number: "))
        print("Thinking...")
        time.sleep(random.uniform(2, 6))
        if number in easter_eggs:
            print(easter_eggs[number])
            return
        print(f"Got it! Your number must be {num2words(number)}!")
    except ValueError:
        print("Please enter only a whole numerical input next time please!")

def guess_mine():
    secret = random.randint(0, 1000)

    try:
        guess = int(input("Hi! So you want to guess the number I'm thinking of? It won't be easy, but I promise the reward will be worth it if you win!"))
        if guess == secret:
            print("...")
            time.sleep(3)
            print("HOW\n")
            time.sleep(1)
            print("Well... you actually did it.")
            time.sleep(1)
            print("My creator Rainy wanted me to give you this YouTube video\nas a reward, these are the best cookies he's ever made.")
            time.sleep(1)
            print("We hope you enjoy it as much as we did.\n")
            print(f"{cookies_video}")
        else:
            print("Wrong! One more try:")
            guess = int(input("> "))
            if guess == secret:
                print("...")
                time.sleep(3)
                print("HOW\n")
                time.sleep(1)
                print("Well... you actually did it.")
                time.sleep(1)
                print("My creator Rainy wanted me to give you this YouTube video\nas a reward, these are the best cookies he's ever made.")
                time.sleep(1)
                print("We hope you enjoy it as much as we did.\n")
                print("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            else:
                print(f"WRONG! IT WAS {num2words(secret)}!")
    except ValueError:
        print("Please enter only a whole numerical input next time please!")

def main():
    print("1. Let me guess your number")
    print("2. Guess my number")

    choice = input("> ").strip()

    if choice == "1":
        guess_yours()
    elif choice == "2":
        guess_mine()
main()
