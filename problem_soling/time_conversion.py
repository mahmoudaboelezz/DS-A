


def timeConversion(s):
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]
        else:
            return s[:-2]
    else:
        if s[:2] == '12':
            return s[:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]

    
    

s = '12:45:54AM'
print(timeConversion(s))


def timeConversion(s):
    # Write your code here
    if s[-2:] == 'AM':
        if s[:2] == '12':
            return '00' + s[2:-2]
        result = s[:-2]
    if s[-2:] =='PM':
        if int(s[:2]) == 12:
            result = s[:-2]
        else:
            a = int(s[:2]) +12
            result = f'{a}{s[2:-2]}'
    return result
s = '12:01:45PM'

print(timeConversion(s))