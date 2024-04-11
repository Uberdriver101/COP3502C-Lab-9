

def encoder(string):
    encoded_message = ''
    for i in range(len(string)):
        char = string[i]
        if char.isdigit():
            number = int(char)
            number += 3
            if number > 9:
                number -= 10
            encoded_message += str(number)
        else:
            encoded_message += char
    return encoded_message


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


if __name__ == '__main__':
    encoded_password = ''
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        menu_selection = int(input('Please enter an option: '))


        if menu_selection == 3:
            break
        elif menu_selection == 1:
            password = input('Please enter your password to encode: ')
            encoded_password = encoder(password)
            print('Your password has been encoded and stored!')
        elif menu_selection == 2:
            decoded_password = decoder(encoded_password)

            print(f'The encoded passcode is {encoded_password}, and the original password is {decoded_password}')