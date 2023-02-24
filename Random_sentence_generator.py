import random
count = 0


def random_picker(words):
    return random.choice(words)


names = ["Danny", "Alex", "Silviya", "Nicole", "Peter", "George", "Ivan"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas", "Busmantsi", "North Pole"]
nouns = ["stones", "a cake", "bikes", "balls", "an apple", "a friend", "paintings", "money"]
adverbs = ["slowly", "quickly", "cheerfully", "sadly", "rapidly", "steadily", "ambitiously"]
details = ["at home", "at the park", "near the river", "when shopping", "while sleeping"]
verbs = ["eats", "hits", "holds", "hugs", "kisses", "plays with", "runs from", "dreams of"]

input("Hello and welcome to the random sentence generator by Danny!"
      "\nPress [Any button] to initiate the generator!")
while True:
    count += 1
    random_name = random_picker(names)
    random_place = random_picker(places)
    random_noun = random_picker(nouns)
    random_adverb = random_picker(adverbs)
    random_detail = random_picker(details)
    random_verb = random_picker(verbs)

    print(f"{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}.")
    input("Press [Any button] to continue.")

    #quit option after 10 attempts
    if count >= 10:
        print(f"You have already generated 10 unique sentences!\n"
              f"Would you like to proceed? [y]es or [n]o")
        while True:
            action = input()
            if action in ['y', 'Y', 'yes', 'Yes']:
                count = 0
                break
            elif action in ['n', 'N', 'no', 'No']:
                print("Goodbye!")
                exit()
            else:
                print("Unrecognised option!\n"
                      f"Would you like to proceed?\n"
                      f"Please type [y]es or [n]o")
