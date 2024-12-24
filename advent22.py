dat = [int(x) for x in open('input22.txt').read().splitlines()]

# part 1
def update_secret(secret, cache):
    if secret in cache.keys():
        return cache[secret], cache
    multiplyers = [64, (1/32), 2048]
    init_secret = secret + 0
    for N in range(3):
        old_secret = secret + 0
        # first multiply/divide
        secret = int(old_secret*multiplyers[N])
        # then mix
        secret = old_secret ^ secret
        # then prune
        secret = secret % 16777216
    cache[init_secret] = secret
    return secret, cache

cache = {}
numbers = []
buyers = {}
for b, secret in enumerate(dat):
    buyers[b] = []
    for _ in range(2000):
        secret, cache = update_secret(secret, cache)
        buyers[b].append(secret % 10)
    numbers.append(secret)
ans = sum(numbers)

# part 2


