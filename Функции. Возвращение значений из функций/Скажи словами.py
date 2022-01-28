def number_in_english(n):
    ls = {1: 'one', 2: 'two', 3: 'three',
          4: 'four', 5: 'five', 6: 'six',
          7: 'seven', 8: 'eight', 9: 'nine',
          10: 'ten', 11: 'eleven', 12: 'twelve',
          13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
          16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
          19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
          50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
          90: 'ninety', 0: 'zero'}
    if n <= 20:
        return ls.get(n)
    elif n % 100 == 0:
        return ls.get(int(str(n)[0])) + ' hundred'
    elif len(str(n)) == 2 and n % 10 == 0:
        return ls.get(n)
    elif len(str(n)) < 3:
        if n % 10 == 0:
            return ls.get(str(n)[0] + "0")
        else:
            return f'{ls.get(int(str(n)[0] + "0"))} {ls.get(int(str(n)[1]))}'
    else:
        if n % 10 == 0:
            return ls.get(int(str(n)[0])) + ' hundred and ' + ls.get(int(str(n)[1] + "0"))
        else:
            if ls.get(int(str(n)[1:])):
                return f'{ls.get(int(str(n)[0]))} hundred and {ls.get(int(str(n)[1:]))}'
            else:
                return f'{ls.get(int(str(n)[0]))} hundred and {ls.get(int(str(n)[1] + "0"))} {ls.get(int(str(n)[2]))}'
