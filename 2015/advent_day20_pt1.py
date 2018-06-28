def factors(n):
    '''Credit:
    http://stackoverflow.com/questions/6800193/what-is-the-most-efficient-way-of-finding-all-the-factors-of-a-number-in-python
    '''
    return set(x for tup in ([i, n//i] 
                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)

target_presents = 34000000
target_factor_sum = target_presents / 10

house = 0
solved = False
while not solved:
    house += 1
    if sum(factors(house)) >= target_factor_sum:
        solved = True

print(house)