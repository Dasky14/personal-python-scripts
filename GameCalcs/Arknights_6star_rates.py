from prettytable import PrettyTable
from random import random
from time import sleep


def main():
    # Arknights 6-star rates
    starting_chance = 0.02
    increment = 0.02
    increment_after = 50

    # Iteration variables
    iteration_max = 1000000

    six_star_count = 0
    pulls_since_last_six_star = 0
    for _ in range(iteration_max):
        current_chance = starting_chance + increment * (
            max(0, (pulls_since_last_six_star + 1) - increment_after)
        )

        if random() < current_chance:
            six_star_count += 1
            pulls_since_last_six_star = 0
        else:
            pulls_since_last_six_star += 1

    print_data(iteration_max, six_star_count)


def print_data(total_pulls, six_star_count):
    table = PrettyTable()
    table.field_names = [
        "Pulls",
        "6* units",
        "Average pulls per 6*",
    ]

    # Left align all fields
    for field_name in table.field_names:
        table.align[field_name] = "l"

    table.add_row(
        [
            str(total_pulls),
            str(six_star_count),
            str("{0:.2f}".format(total_pulls / six_star_count)),
        ]
    )

    print(table)


if __name__ == "__main__":
    main()
