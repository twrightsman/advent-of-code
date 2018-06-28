import hashlib

solved = False
key = "iwrupvqb"
current_int = 0

while not solved:
    current_int += 1
    m = hashlib.md5()

    key_and_int = key + str(current_int)
    m.update(key_and_int.encode('utf-8'))

    if m.hexdigest()[0:5] == '00000':
        solved = True

    if current_int % 10000 == 0:
        print('Finished {}'.format(current_int))

print(current_int)