"""
This is an example for a bot.
"""
from penguin_game import *

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

    def calculate_ideality (capture_rate, threat_level):
        return threat_level-capture_rate

    def expansion_phase(enemy_icebergs):
        ideal_for_expansion = list(enemy_icebergs.keys())[0]
        for enemy_iceberg in enemy_icebergs:
            max_value = calculate_ideality(enemy_icebergs.get(ideal_for_expansion)[0],
                                           enemy_icebergs.get(ideal_for_expansion)[1])
            if calculate_ideality(enemy_icebergs.get(enemy_iceberg)[0], enemy_icebergs.get(enemy_iceberg)[1]) >\
                    max_value:
                ideal_for_expansion = enemy_iceberg

        return ideal_for_expansion


