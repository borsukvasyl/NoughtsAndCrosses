def main():
    def make_question(question, true, false):
        while True:
            answer = input("{}".format(question)).lower()
            if answer in true:
                return True
            elif answer in false:
                return False
            print("Incorrect answer!")

    import random
    from noughts_and_crosses import NoughtsAndCrosses
    from user import User

    hard_bot_names = ["SuperBot", "Destroyer", "Dominator"]
    easy_bot_names = ["Bobo", "Noob", "HandsFromWrongPlace"]

    if make_question("Choose difficulty: ", ["hard", "h"], ["easy", "e"]):
        if make_question("Are you Oles Dobosevych or Andriy Romaniuk: ", ["yes", "y"], ["no", "n"]):
            from hard_bot_tree import HardBot
        else:
            from hard_bot import HardBot
        bot = HardBot(random.choice(hard_bot_names))
    else:
        from easy_bot import EasyBot
        bot = EasyBot(random.choice(easy_bot_names))
    game = NoughtsAndCrosses([User(input("Enter your name: ")), bot])
    game.run()


if __name__ == "__main__":
    main()
