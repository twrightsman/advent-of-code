from hashlib import md5

door_id = input("Door ID: ")
int_index = 0
unsolved = True
password = ['']*8

while(unsolved):
    m = md5()
    m.update((door_id + str(int_index)).encode('utf-8'))
    digest = m.hexdigest()
    if (digest[:5] == '00000'):
        if (digest[5].isdigit()) and (int(digest[5]) <= 7):
            if password[int(digest[5])] == '':
                password[int(digest[5])] = digest[6]
                if not '' in password:
                    unsolved = False

    int_index += 1

print(''.join(password))
