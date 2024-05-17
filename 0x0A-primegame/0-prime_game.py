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
    for every prime number that's
    returned from is_prime gets stored here
    """
    sieve = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    primes = [p for p in range(2, n+1) if sieve[p]]
    return primes


def isWinner(x, nums):
    """
    checks who is the winner between two players as they insert their numbers
    one by one and we need to find out which player has inserted all of his
    numbers before any other player does so.
    """
    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)
    primes = get_primes(max_num)

    for n in nums:
        total_moves = len([p for p in primes if p <= n])

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
