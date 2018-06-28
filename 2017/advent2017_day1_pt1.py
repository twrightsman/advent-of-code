captcha = input("Captcha: ")

sum = 0
last_index = len(captcha) - 1
for index, digit in enumerate(captcha):
  if index == last_index:
    next_digit = captcha[0]
  else:
    next_digit = captcha[index + 1]
  
  if digit == next_digit:
    sum += int(digit)

print(sum)
