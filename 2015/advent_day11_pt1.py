import sys

def increment_character(character):
    if character == 'z':
        return 'a'
    else:
        return chr(ord(character) + 1)

def increment_password(password):
    character_array = list(password)

    for index in range(1, len(character_array) + 1):
        if index == len(character_array) and character_array[-index] == 'z':
            raise OverflowError("Password cannot be incremented past '{}'.".format(password))

        character_array[-index] = increment_character(character_array[-index])

        if not character_array[-index] == 'a':
            break

    return ''.join(character_array)


def includes_three_straight(password):
    for index in range(0, len(password)):
        try:
            char3 = ord(password[index + 2])
            char2 = ord(password[index + 1])
            char1 = ord(password[index])

            if (char3 == (char2 + 1)) and (char2 == (char1 + 1)):
                return True

        except IndexError:
            return False

def includes_iol(password):
    if 'i' in password:
        return True
    elif 'o' in password:
        return True
    elif 'l' in password:
        return True
    else:
        return False

def includes_diff_nonoverlap_pairs(password):
    one_pair_present = False

    index = 0
    while index < len(password):
        try:
            if password[index] == password[index + 1]:
                if one_pair_present:
                    return True
                else:
                    one_pair_present = True
                    index += 2
            else:
                index += 1
        except IndexError:
            return False

def valid_passwords(seed):
    password = seed

    try:
        while True:
            password = increment_password(password)

            if includes_three_straight(password) and (not includes_iol(password)) and includes_diff_nonoverlap_pairs(password):
                yield password

    except OverflowError:
        pass

puzzle_input = sys.stdin.read().rstrip()

ValidSantaPasswords = valid_passwords(puzzle_input)

print(next(ValidSantaPasswords))