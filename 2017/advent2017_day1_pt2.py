captcha = input("Captcha: ")

sum = 0
last_index = len(captcha) - 1
captcha_len = len(captcha)
check_dist = captcha_len // 2
for index, digit in enumerate(captcha):
  if index + check_dist > last_index:
    check_index = check_dist - (last_index - index) - 1
  else:
    check_index = index + check_dist

  check_digit = captcha[check_index]

  if digit == check_digit:
    sum += int(digit)

print(sum)
