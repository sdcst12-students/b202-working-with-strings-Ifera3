#!python3

"""
Strings are iterable.  Use for loops to iterate through both strings to create a list to represent a deck of cards. Note: We can also use list comprehension as strings are still iterable!
"""

ranks = "A23456789TJQK"
suits = "CDHS"

def createDeck():
  Deck = []
  for s in suits:
    for r in ranks:
      Deck.append(f'{r}{s}')
      print(f'{r}{s}')
  return Deck

def main():
  deck = createDeck()
  print(deck)
  assert "AS" in deck
  assert "KC" in deck
  assert deck.count("TC") == 1

if __name__ == "__main__":
  main()
