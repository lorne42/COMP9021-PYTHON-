from math import sqrt

def sieve_of_primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve

def primes_in_window(size, lower_bound, upper_bound):
    if size > upper_bound - lower_bound + 1:
        print('Window size is too large for these bounds.')
        return
    
    sieve = sieve_of_primes_up_to(upper_bound)
    
    max_prime_count = 0
    best_windows = []
    
    # Scan for windows of the given size
    for i in range(lower_bound, upper_bound - size + 2):
        prime_count = sum(1 for j in range(i, i + size) if sieve[j])
        
        if prime_count > max_prime_count:
            max_prime_count = prime_count
            best_windows = [(i, i + size - 1)]
        elif prime_count == max_prime_count:
            best_windows.append((i, i + size - 1))
    
    if max_prime_count == 0:
        print(f'There is no prime in a window of size {size}.')
    else:
        if size != 1:
            print(f'There are at most {max_prime_count} primes in a window of size {size}.')
        else:
            print('There is at most one prime in a window of size 1.')

        for start, end in best_windows:
            primes_in_window = [p for p in range(start, start + size) if sieve[p]]
            if primes_in_window:
                print(f'In some window, the smallest prime is {primes_in_window[0]} and the largest one is {primes_in_window[-1]}.')
