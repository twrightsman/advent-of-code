def day2_part1(password_db: str) -> str:
    valid_passwords = 0
    for line in password_db.split("\n"):
        if line:
            policy, password = line.split(": ")
            char_range, char = policy.split(" ")
            lower_bound, upper_bound = [int(e) for e in char_range.split('-')]
            char_count = password.count(char)
            if (char_count >= lower_bound) and (char_count <= upper_bound):
                valid_passwords += 1
    return str(valid_passwords)

def day2_part2(password_db: str) -> str:
    valid_passwords = 0
    for line in password_db.split("\n"):
        if line:
            policy, password = line.split(": ")
            char_indices, char = policy.split(" ")
            index1, index2 = [int(e) for e in char_indices.split('-')]
            if (password[index1 - 1] == char) ^ (password[index2 - 1] == char):
                valid_passwords += 1
    return str(valid_passwords)

