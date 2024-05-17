#!/usr/bin/python3
""" solves the game to see who is the winner between 2 players """


def is_prime(num):
    """ checks if parsed number is prime number or not"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes(n):
    """
    for ervery prime number thats
    returned from is_prime gets stored here
    """
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    checks who is the winner between two players as they insert their numbers
    one by one and we need to find out which player has inserted all of his
    numbers before any other player does so.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = get_primes(n)
        total_moves = len(primes)

        if total_moves % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
