from collections import defaultdict

with open('day4_input.txt') as room_file:
    sector_id_sum = 0
    for room in room_file:
        encrypted_name, given_checksum = room.rstrip().split('[')
        given_checksum = given_checksum.rstrip(']')
        encrypted_name = encrypted_name.split('-')
        sector_id = int(encrypted_name.pop())
        merged_encrypted_name = ''.join(encrypted_name)

        char_freq = defaultdict(lambda: 0)
        for char in merged_encrypted_name:
            char_freq[char] += 1

        alpha_sorted_keys = sorted(list(char_freq.keys()))
        checksum = ''.join(sorted(alpha_sorted_keys, key=lambda x: char_freq[x], reverse=True)[:5])

        if checksum == given_checksum:
            # valid room!
            actual_shift = sector_id % 26
            decrypted_name = []
            for index, word in enumerate(encrypted_name):
                decrypted_name.append([])
                for char in word:
                    if (ord(char) + actual_shift) > ord('z'):
                        remaining_shift = actual_shift - (ord('z') - ord(char) + 1)
                        new_char = chr(ord('a') + remaining_shift)
                    else:
                        new_char = chr(ord(char) + actual_shift)
                    decrypted_name[index].append(new_char)
                decrypted_name[index] = ''.join(decrypted_name[index])
            if 'northpole' in decrypted_name:
                print(sector_id)
                break

