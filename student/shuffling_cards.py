# def create_numbered_deck(n):
#     """
#     Helper function to create a deck of cards numbered from 0 to n-1.

#     Args:
#     - n (int): Number of cards in the deck.

#     Returns:
#     - list: List of integers representing the numbered deck.
#     """
#     return [i for i in range(n)]

# def cut(deck, n):
#     """
#     Helper function to perform a cut operation on the deck.

#     Args:
#     - deck (list): List representing the deck of cards.
#     - n (int): Number of cards to cut from the top to the bottom.

#     Returns:
#     - list: List representing the deck after performing the cut operation.
#     """
#     # new_deck = []

#     # # Add the elements from position n to the end
#     # for i in range(n, len(deck)):
#     #     new_deck.append(deck[i])

#     # # Add the elements from the start to position n-1
#     # for i in range(n):
#     #     new_deck.append(deck[i])
    
#     # return new_deck
#     return deck[n:] + deck[:n]

# def deal(deck):
#     """
#     Helper function to deal the deck to a new pile, reversing the order of cards.

#     Args:
#     - deck (list): List representing the deck of cards.

#     Returns:
#     - list: List representing the deck after performing the deal operation.
#     """
#     new_deck = []

#     # Add elements in reverse order (end of deck, to zero, step of -1)
#     for i in range(len(deck) - 1, 0, -1):
#         new_deck.append(deck[i])

#     return new_deck

# def faro_shuffle(deck):
#     """
#     Helper function to perform a Faro out-shuffle on the deck

#     A faro out-shuffle (also known as a perfect, or weave, out-shuffle)
#     involves splitting the deck into two equal halves and then interleaving them
#     perfectly, starting with the top card of the original deck. 

#     Args:
#     - deck (list): List representing the deck of cards.

#     Returns:
#     - list: List representing the deck after performing the Faro shuffle.
#     """
#     size = len(deck)
#     new_deck = [None] * size
#     position = 0

#     for i in range(size):
#         # Find the next available position
#         while new_deck[position] is not None:
#             position = (position + 1) % size
        
#         new_deck[position] = deck[i]
#         position = (position + 2) % size  # Move to the next interleaved position

#     return new_deck

# def find_card_position(deck_size, instructions, card):
#     """
#     Find the position of a specific card in a deck after applying a series of instructions.

#     Args:
#     - deck_size (int): Number of cards in the deck.
#     - instructions (list of str): List of instructions to apply to the deck.
#     - card (int): The card to find the position of.

#     Returns:
#     - int: Position of the card in the deck after applying all instructions.
#     """
#     deck = create_numbered_deck(deck_size)

#     for instruction in instructions:
#         if instruction.startswith("cut"):
#             n = int(instruction.split()[-1])
#             deck = cut(deck, n)
#         elif instruction.startswith("deal"):
#             deck = deal(deck)
#         elif instruction.startswith("shuffle"):
#             deck = faro_shuffle(deck)

#     for position, _card in enumerate(deck):
#         if _card == card:
#             return position



import numpy as np
from numba import jit

def create_numbered_deck(n):
    """
    Helper function to create a deck of cards numbered from 0 to n-1.

    Args:
    - n (int): Number of cards in the deck.

    Returns:
    - np.ndarray: Array of integers representing the numbered deck.
    """
    return np.arange(n)

def cut(deck, n):
    """
    Helper function to perform a cut operation on the deck.

    Args:
    - deck (np.ndarray): Array representing the deck of cards.
    - n (int): Number of cards to cut from the top to the bottom.

    Returns:
    - np.ndarray: Array representing the deck after performing the cut operation.
    """
    return np.concatenate((deck[n:], deck[:n]))

def deal(deck):
    """
    Helper function to deal the deck to a new pile, reversing the order of cards.

    Args:
    - deck (np.ndarray): Array representing the deck of cards.

    Returns:
    - np.ndarray: Array representing the deck after performing the deal operation.
    """
    return deck[::-1]

def faro_shuffle(deck):
    """
    Helper function to perform a Faro out-shuffle on the deck

    A faro out-shuffle (also known as a perfect, or weave, out-shuffle)
    involves splitting the deck into two equal halves and then interleaving them
    perfectly, starting with the top card of the original deck. 

    Args:
    - deck (np.ndarray): Array representing the deck of cards.

    Returns:
    - np.ndarray: Array representing the deck after performing the Faro shuffle.
    """
    size = len(deck)
    half_size = size // 2
    first_half = deck[:half_size]
    second_half = deck[half_size:]
    
    new_deck = np.empty(size, dtype=deck.dtype)
    new_deck[::2] = first_half
    new_deck[1::2] = second_half

    return new_deck

def find_card_position(deck_size, instructions, card):
    """
    Find the position of a specific card in a deck after applying a series of instructions.

    Args:
    - deck_size (int): Number of cards in the deck.
    - instructions (list of str): List of instructions to apply to the deck.
    - card (int): The card to find the position of.

    Returns:
    - int: Position of the card in the deck after applying all instructions.
    """
    deck = create_numbered_deck(deck_size)

    for instruction in instructions:
        if instruction.startswith("cut"):
            n = int(instruction.split()[-1])
            deck = cut(deck, n)
        elif instruction.startswith("deal"):
            deck = deal(deck)
        elif instruction.startswith("shuffle"):
            deck = faro_shuffle(deck)

    try:
        return np.where(deck == card)[0][0]
    except IndexError:
        return -1
