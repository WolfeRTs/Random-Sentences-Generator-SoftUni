import random


def random_sentence(light, neutral, dark, meetings, fights, meet_actions, fight_actions):
    main_character = random.choice(light)
    side_character = random.choice(neutral)
    villain_character = random.choice(dark)
    meet_place = random.choice(meetings)
    fight_place = random.choice(fights)
    meet_action = random.choice(meet_actions)
    fight_action = random.choice(fight_actions)

    if fight_place == 'Death Star':
        return f"{main_character} and {side_character} met on {meet_action}, but were caught by {villain_character} and taken prisoners on the Death Star!"
    elif fight_place == 'Sarlacc Pit':
        return f"Poor {main_character} and {side_character} fell into a Sarlacc Pit! {villain_character} is definitely having a laugh."
    else:
        return f"{main_character} and {side_character} meet on {meet_place} to {meet_action} and then {fight_action} {villain_character} on {fight_place}"


light_characters = ['Chewbacca', 'Han Solo', 'Leia', 'Luke Skywalker', 'Anakin Skywalker', 'Jar Jar Binks', 'Mace Windu', 'Obi-Wan Kenobi', 'Padme Amidala', 'Yoda']
neutral_characters = ['Boba Fett', 'C-3PO', 'Jabba the Hutt', 'R2-D2', 'Ahsoka Tano', 'Fennec Shand']
dark_characters = ['Darth Vader', 'Darth Sidious', 'Darth Maul', 'Count Dooku', 'General Grievous', 'Asajj Ventress']
meeting_places = ['Coruscant', 'Mos Espa', 'Naboo', 'Kamino', 'Jedi Temple', 'Hoth', 'Endor']
fighting_places = ['Death Star', 'Mustafar', 'Sarlacc Pit', 'Kashyyk', 'Geonosis', 'Dathomir']
meeting_actions = ['scheme a plan', 'have a few drinks', 'play a game of holochess', 'discuss politics', 'attend a droid programming course', 'watch a match of droid boxing']
fighting_actions = ['defeat', 'ally with', 'ambush', 'spar with', 'podrace with', 'negotiate with']

# Example result - {Chewbacca} and {Boba Fett} meet on {Coruscant} to {scheme a plan} and then {defeat} {Darth Vader} on {Mustafar}

while True:
    print(random_sentence(light_characters, neutral_characters, dark_characters, meeting_places, fighting_places, meeting_actions, fighting_actions))
    print()
    user_input = input("Press [Enter] to generate a new one or write 'Finish' to exit the program: ")
    print()
    if user_input.lower() == 'finish':
        print('May the Force be with you!')
        break
