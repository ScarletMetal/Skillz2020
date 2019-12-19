"""
This is an example for a bot.
"""
from penguin_game import *


BotState = Enum("BotState", "survival", "expansion")

state = BotState.survival


def penguins_to_capture(my_icebergs, iceberg):
    max_turns = 0
    for my_iceberg in my_icebergs:
        if my_iceberg.penguin_amount > iceberg.penguin_amount + iceberg.penguins_per_turn*my_iceberg.get_turns_till_arrival(iceberg):
            return iceberg.penguin_amount + iceberg.penguins_per_turn*my_iceberg.get_turns_till_arrival(iceberg)
        max_turns = max_turns if max_turns>my_iceberg.get_turns_till_arrival(iceberg) else my_iceberg.get_turns_till_arrival(iceberg)
    return iceberg.penguin_amount + iceberg.penguins_per_turn*max_turns

def do_turn(game):
    """
    Makes the bot run a single turn.

    :param game: the current game state.
    :type game: Game
    """
    # Go over all of my icebergs.
    for my_iceberg in game.get_my_icebergs():
        # The amount of penguins in my iceberg.
        my_penguin_amount = my_iceberg.penguin_amount  # type: int

        # If there are any neutral icebergs.
        if game.get_neutral_icebergs():
            # Target a neutral iceberg.
            destination = game.get_neutral_icebergs()[0]  # type: Iceberg
        else:
            # Target an enemy iceberg.
            destination = game.get_enemy_icebergs()[0]  # type: Iceberg

        # The amount of penguins the target has.
        destination_penguin_amount = destination.penguin_amount  # type: int

        # If my iceberg has more penguins than the target iceberg.
        if my_penguin_amount > destination_penguin_amount:
            # Send penguins to the target.
            print my_iceberg, "sends", (destination_penguin_amount + 1), "penguins to", destination
            my_iceberg.send_penguins(destination, destination_penguin_amount + 1)