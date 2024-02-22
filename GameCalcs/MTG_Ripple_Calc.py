import sys
import random
import time
from os import system, name

def clear():
	_ = system('cls') if name == 'nt' else system('clear')

def space():
	print("")

# --- Variables --------------------------------------------------------------------

decksToSimulate = 10000
cardsPerDeck = 100
cardsDrawnAtStart = 15
correctCardsPerDeckMin = 25
correctCardsPerDeckMax = 40

# ----------------------------------------------------------------------------------

class Result:
	def __init__(self, hitsInDeck: int, totalCasts: int, decksToSimulate: int, runouts: int):
		self.totalDecks = decksToSimulate
		self.hitsInDeck = hitsInDeck
		self.totalCasts = totalCasts
		self.runouts = runouts

	def averageCasts(self) -> float:
		return self.totalCasts / self.totalDecks

# --- Main logic -------------------------------------------------------------------

timer = time.perf_counter()
start = timer

results = []

for hitsInDeck in range(correctCardsPerDeckMin, correctCardsPerDeckMax + 1):
	totalCasts = 0
	runouts = 0

	for deckIndex in range(decksToSimulate):
		pool = []
		pool.extend([True] * hitsInDeck)
		pool.extend([False] * (cardsPerDeck - hitsInDeck))
		random.shuffle(pool)
		#for _ in range(cardsDrawnAtStart):
		#	pool.pop(0)

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
			if thisDeckCasts >= hitsInDeck - 1:
				stackCount = 0
				runouts += 1

			#print(f"Deck {deckIndex + 1}, hits in deck: {hitsInDeck}, hits in this deck: {thisDeckCasts}, stackCount {stackCount}, deck size: {len(pool)}")
			#time.sleep(0.1)
	
	results.append(Result(hitsInDeck, totalCasts, decksToSimulate, runouts))






clear()
print(f"Simulation time                : {round(time.perf_counter() - start, 2)} seconds")
print(f"Total decks                    : {decksToSimulate}")
print(f"Deck size                      : {cardsPerDeck}")
print(f"Cards drawn at start           : {cardsDrawnAtStart}")
print(f"Hits in deck start             : {correctCardsPerDeckMin}")
print(f"Hits in deck end               : {correctCardsPerDeckMax}")
space()

for result in results:
	print(f"--- {result.hitsInDeck} of same card in deck ---")
	print(f"Average casts              : {result.averageCasts()}")
	print(f"Chance to cast everything  : {(result.runouts / result.totalDecks) * 100}%")
	space()
