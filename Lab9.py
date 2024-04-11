print('Heyy!!')

#decoder created by Lucas
def decoder(string):
    decoded_message = ''
    for i in range(len(string)):
        number = int(string[i])
        number -= 3
        #accounts for numbers larger than 6 that return double digit numbers
        if number < 0:
            number += 10
        number = str(number)
        decoded_message += number
    return decoded_message

print(decoder('90123'))
