def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, int(n ** 0.5)):
        if n % divisor == 0:
            return False
    return True


n = int(input())
print("YES" if is_prime(n) else "NO")
