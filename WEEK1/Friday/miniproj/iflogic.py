#!/usr/bin/python3
"""Veronica Pichay | TLG Learning
      Zodiac sign checker"""

def main():
    """runtime"""


# User's birth date
date = int(input("What date is your birthday? "))

# User's birth month
month = input("What month is your birthday? ")
month = month.lower()

if month == 'december':
    zodiac_sign = 'Sagittarius' if (date < 22) else 'capricorn'
    #if date < 22:
    #    zodiac_sign = 'Sagittarius'
    #else:
    #    zodiac_sign = 'capricorn'
elif month == 'january':
    zodiac_sign = 'Capricorn' if (date < 20) else 'aquarius'
elif month == 'february':
    zodiac_sign = 'Aquarius' if (date < 19) else 'pisces'
elif month == 'march':
    zodiac_sign = 'Pisces' if (date < 21) else 'aries'
elif month == 'april':
    zodiac_sign = 'Aries' if (date < 20) else 'taurus'
elif month == 'may':
    zodiac_sign = 'Taurus' if (date < 21) else 'gemini'
elif month == 'june':
    zodiac_sign = 'Gemini' if (date < 21) else 'cancer'
elif month == 'july':
    zodiac_sign = 'Cancer' if (date < 23) else 'leo'
elif month == 'august':
    zodiac_sign = 'Leo' if (date < 23) else 'virgo'
elif month == 'september':
    zodiac_sign = 'Virgo' if (date < 23) else 'libra'
elif month == 'october':
    zodiac_sign = 'Libra' if (date < 23) else 'scorpio'
elif month == 'november':
    zodiac_sign = 'scorpio' if (date < 22) else 'sagittarius'
print("Your Astrological sign is :", zodiac_sign)
