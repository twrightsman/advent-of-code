from collections import defaultdict

with open('day4_input.txt') as room_file:
    sector_id_sum = 0
    for room in room_file:
        encrypted_name, given_checksum = room.rstrip().split('[')
        given_checksum = given_checksum.rstrip(']')
        encrypted_name = encrypted_name.split('-')
        sector_id = int(encrypted_name.pop())
        encrypted_name = ''.join(encrypted_name)

        char_freq = defaultdict(lambda: 0)
        for char in encrypted_name:
            char_freq[char] += 1

        alpha_sorted_keys = sorted(list(char_freq.keys()))
        checksum = ''.join(sorted(alpha_sorted_keys, key=lambda x: char_freq[x], reverse=True)[:5])

        if checksum == given_checksum:
            sector_id_sum += sector_id

print(sector_id_sum)
