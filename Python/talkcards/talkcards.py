import math
import pandas as pd
import random

CARD_LENGTH = 40
WORDS_LENGTH = 30
SIDE_PADDING = int((CARD_LENGTH - WORDS_LENGTH) / 2)
TOP_BOTTOM_PADDING = "||" + (" " * (CARD_LENGTH - 4)) + "||"
LEFT_BORDER = "||" + (" " * (SIDE_PADDING - 2))
RIGHT_BORDER = (" " * (SIDE_PADDING - 2)) + "||"
TOP_BOTTOM_BORDER = "=" * (CARD_LENGTH)

def print_card(test_string):
    card_array = [TOP_BOTTOM_BORDER]
    card_array.extend(TOP_BOTTOM_PADDING for i in range(2))

    for i in range(math.ceil(len(test_string) / WORDS_LENGTH)):
        card_string = test_string[(WORDS_LENGTH * i):(WORDS_LENGTH * (i + 1))]
        if len(card_string) < WORDS_LENGTH:
            remainder_length = (CARD_LENGTH - len(card_string) - 4)
            last_left_border = "||" + (" " * int(remainder_length / 2))
            last_right_border = (" " * int(remainder_length / 2)) + "||"
            edited_string = last_left_border + str(card_string) + last_right_border
            if len(edited_string) < CARD_LENGTH:
                edited_string = last_left_border + str(card_string) + " " + last_right_border
            card_array.append(edited_string)
        else:
            card_array.append(LEFT_BORDER + str(card_string) + RIGHT_BORDER)
        
    card_array.extend(TOP_BOTTOM_PADDING for i in range(2))
    card_array.append(TOP_BOTTOM_BORDER)
    final_card = "\n".join(card_array)
    return final_card

csv_selection = True
while csv_selection:
    end_round = input("\nKey in the path to your game file (.csv format): \n")
    try:
        all_cards = pd.read_csv(end_round).dropna()
        card_categories = list(all_cards.columns.values)
        game_choice = {i + 1:card_categories[i] for i in range(len(card_categories))}
        csv_selection = False
    except:
        print("\nInvalid input; please try again.")

ongoing_game = True
while ongoing_game:
    while ongoing_game:
        print("\nGame categories: ")
        for key, val in game_choice.items():
            print(str(key) + ": " + str(val))
        user_input = input("\nSelect a category by entering the corresponding number or type 'q' to quit: \n")
        if user_input == 'q':
            print("\nHope you had a meaningful time connecting!")
            ongoing_game = False
        else:
            try:
                selected_category = game_choice[int(user_input)]
                print("\nCategory [" + str(game_choice[int(user_input)]) + "] selected. \n")
                category_cards = list(all_cards[selected_category])
                random_card = random.choice(category_cards)
                print(print_card(random_card))
                ongoing_round = True
                while ongoing_round:
                    end_round = input("\nPress 'n' to move on to the next round.\n")
                    if end_round == 'n':
                        ongoing_round = False
            except:
                print("Invalid input; please try again.")