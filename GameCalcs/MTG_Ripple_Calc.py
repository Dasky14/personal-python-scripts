import random
import time
from prettytable import PrettyTable
from os import system, name
from dataclasses import dataclass
from multiprocessing import Pool


def clear():
    _ = system("cls") if name == "nt" else system("clear")


def space():
    print("")


# --- Variables --------------------------------------------------------------------

decksToSimulate = 10000
cardsPerDeck = 100
cardsDrawnAtStart = 15
correctCardsPerDeckMin = 25
correctCardsPerDeckMax = 50

# ----------------------------------------------------------------------------------


@dataclass
class Result:
    """
    Contains the result for the simulation of a single deck
    """

    hitsInDeck: int
    totalCasts: int
    totalDecks: int
    runouts: int

    def averageCasts(self) -> float:
        return self.totalCasts / self.totalDecks


# --- Main logic -------------------------------------------------------------------


def main():
    timer = time.perf_counter()
    start = timer

    results = []
    amounts = range(correctCardsPerDeckMin, correctCardsPerDeckMax + 1)

    # Create a multiprocessing pool to simulate the decks
    with Pool() as pool:
        # Run the simulations with the pool
        results = pool.map(simulate_deck, amounts)

        # Create a pretty table to display the results
        table = PrettyTable()
        table.field_names = [
            "Cards in deck",
            "Average casts",
            "Chance to cast everything",
        ]

        # Set left alignment for all fields
        for field_name in table.field_names:
            table.align[field_name] = "l"

        # Add the results to the table
        for result in results:
            table.add_row(
                [
                    f"{result.hitsInDeck}",
                    f"{round(result.averageCasts(), 2)}",
                    f"{round((result.runouts / result.totalDecks) * 100, 2)}%",
                ]
            )

    # Clear the console and print the simulation statistics
    clear()
    print(f"{"Simulation time":<30}: {round(time.perf_counter() - start, 2)} seconds")
    print(f"{"Total decks":<30}: {decksToSimulate}")
    print(f"{"Deck size":<30}: {cardsPerDeck}")
    print(f"{"Cards drawn at start":<30}: {cardsDrawnAtStart}")
    print(f"{"Hits in deck start":<30}: {correctCardsPerDeckMin}")
    print(f"{"Hits in deck end":<30}: {correctCardsPerDeckMax}")
    space()

    # Print the results table
    print(table)


# ----------------------------------------------------------------------------------


def simulate_deck(hitsInDeck: int) -> Result:
    """
    Simulates a deck with a given number of hits in it, and returns the result of the simulation.

    Args:
            hitsInDeck (int): The number of hits in the deck
    Returns:
            Result: The result of the simulation
    """
    totalCasts = 0
    runouts = 0
    for _ in range(decksToSimulate):
        pool = []
        pool.extend([True] * hitsInDeck)
        pool.extend([False] * (cardsPerDeck - hitsInDeck))
        random.shuffle(pool)
        drawnCount = 0
        for _ in range(cardsDrawnAtStart):
            if pool.pop(0) == True:
                drawnCount += 1

        stackCount = 1
        thisDeckCasts = 0
        while stackCount > 0:
            hits = 0
            # Reveal top 4, count hits, remove from pool
            for i in range(4):
                drawnCard = pool.pop(0)
                if drawnCard == True:
                    hits += 1
                    totalCasts += 1
                    thisDeckCasts += 1
            stackCount += hits

            # Put the misses back in the deck
            if hits < 4:
                pool.extend([False] * (4 - hits))

            stackCount -= 1

            # If we've cast everything in the deck, empty stack
            if thisDeckCasts >= (hitsInDeck - drawnCount) - 1:
                stackCount = 0
                runouts += 1

    # Return the result of the simulation
    return Result(hitsInDeck, totalCasts, decksToSimulate, runouts)


if __name__ == "__main__":
    main()
