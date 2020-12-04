from string import hexdigits, digits


def day4_part1(passport_batch: str) -> str:
    valid_passports = 0
    for passport in passport_batch.split("\n\n"):
        if passport:
            keyvalue_pairs = " ".join(passport.split("\n")).split(" ")
            passport_dict = {key: value for key, value in [p.split(':') for p in keyvalue_pairs if p]}
            if len(passport_dict.keys() - {'cid'}) == 7:
                valid_passports += 1
    return str(valid_passports)


def is_valid_height(height: str) -> bool:
    try:
        value = int(height[:-2])
        unit = height[-2:]
        if unit == 'cm':
            if (value >= 150) and (value <= 193):
                return True
        elif unit == 'in':
            if (value >= 59) and (value <= 76):
                return True
    except:
        return False
    return False


def is_valid_hair_color(hair_color: str) -> bool:
    if hair_color.startswith('#'):
        return all([c in hexdigits for c in hair_color[1:]])
    return False


VALID_EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def is_valid_eye_color(eye_color: str) -> bool:
    return eye_color in VALID_EYE_COLORS


def is_valid_passport_id(passport_id: str) -> bool:
    return (len(passport_id) == 9) and all([c in digits for c in passport_id])


def is_day2_valid_passport(passport: str) -> str:
    if passport:
        keyvalue_pairs = " ".join(passport.split("\n")).split(" ")
        passport_dict = {key: value for key, value in [p.split(':') for p in keyvalue_pairs if p]}
        if len(passport_dict.keys() - {'cid'}) == 7:
            if all([
                int(passport_dict['byr']) >= 1920,
                int(passport_dict['byr']) <= 2002,
                int(passport_dict['iyr']) >= 2010,
                int(passport_dict['iyr']) <= 2020,
                int(passport_dict['eyr']) >= 2020,
                int(passport_dict['eyr']) <= 2030,
                is_valid_height(passport_dict['hgt']),
                is_valid_hair_color(passport_dict['hcl']),
                is_valid_eye_color(passport_dict['ecl']),
                is_valid_passport_id(passport_dict['pid'])
            ]):
                return True
    return False


def day4_part2(passport_batch: str) -> str:
    valid_passports = 0
    for passport in passport_batch.split("\n\n"):
        valid_passports += int(is_day2_valid_passport(passport))
    return str(valid_passports)

