from hashlib import md5

door_id = input("Door ID: ")
int_index = 0
unsolved = True
password = ''

while(unsolved):
    m = md5()
    m.update((door_id + str(int_index)).encode('utf-8'))
    digest = m.hexdigest()
    if digest[:5] == '00000':
        password += digest[5]
        if len(password) == 8:
            unsolved = False

    int_index += 1

print(password)
