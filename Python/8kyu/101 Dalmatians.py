# https://www.codewars.com/kata/101-dalmatians-squash-the-bugs-not-the-dogs/train/python
def how_many_dalmatians(number):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    return dogs[0] if number <= 10 else (dogs[1] if number <= 50 else (dogs[2]  if number < 101 else dogs[3]))

print(how_many_dalmatians(101))