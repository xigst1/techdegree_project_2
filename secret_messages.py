"""
TechDegree: Python Web Developer
Project 2: Secret Messages
choices of cipher: 
    1) Atbash
    2) Affline
    3) Keyword
Date: Sep 2018
"""

from ciphers import Cipher 


# help function(s)
def get_inverse_a(a, m = 26):
    """
    a help function to compute parameter inverse a for affline cipher
    """
    inverse_a = 1
    # a and inverse_a are so-called  modular multiplicative inverse of a modulo m. 
    while (inverse_a*a)%m != 1:
        # update inverse_a until it satisfies a*inverse_a mod m = 1
        inverse_a += 1
        
    return inverse_a


# 3 classes of ciphers
class Atbash(Cipher):
    """
    The Atbash cipher is a particular type of monoalphabetic cipher formed 
    by taking the alphabet and mapping it to its reverse, so that the first letter 
    becomes the last letter, the second letter becomes the second to last letter, 
    and so on. (see: https://en.wikipedia.org/wiki/Atbash)
    """

    def __init__(self, letters = 'abcdefghijklmnopqrstuvwxyz'):
        """
        initiate 2 dictionaries to map original letter to encrypted one and vice versa
        """  
        self.forward = {letters[x]: letters[::-1][x] for x in range(len(letters))}
        self.reverse = {letters[::-1][x]: letters[x] for x in range(len(letters))}
    
    
    def encrypt(self, text):
        """
        a method to encry an input text string
        """
        # initiate an empty list
        output = []
        
        # iterate through each letter using index
        for a_chr in text.lower():
            
            if a_chr == ' ':  # if it is a space character
                output.append(' ')
            else:  # add encrypted letter to the output string
                output.append(self.forward[a_chr])
        
        return ''.join(output)
    
    
    def decrypt(self, text):
        """
        a method to encry an input text string
        """
        # initiate an empty string
        output = []
        # iterate through each character
        for a_chr in text.lower():
            if a_chr == ' ':  # if it is a space character
                output.append(' ')
            else:  # add decrypted letter to the output string
                output.append(self.reverse[a_chr])
        
        return ''.join(output)


class Affline(Cipher):
    """
    Affline cipher maps an alphabet to its numeric equivalent, encrypted using a simple mathematical function, 
    and converted back to a letter (see: https://en.wikipedia.org/wiki/Affine_cipher)
    """
       
    def __init__(self, a, b, m = 26, letters = 'abcdefghijklmnopqrstuvwxyz'):
        """
        initiate the parameters as referred by https://en.wikipedia.org/wiki/Affine_cipher
        """
        self.a = a
        self.b = b
        self.m = m
        self.a_rev = get_inverse_a(self.a, self.m)
        self.letters = letters
        
    def encrypt(self, text):
        """
        a method to encry an input text string
        """
        # initiate an empty list
        output = []
        
        # iterate through each letter using index
        for a_chr in text.lower():
            
            if a_chr == ' ':  # if it is a space character
                output.append(' ')
            else:
                new_key = (self.letters.index(a_chr) * self.a + self.b) % self.m
                output.append(self.letters[new_key])
            
        return ''.join(output)
    
    def decrypt(self, text):
        """
        a method to decrypt back to its original string
        """
        # initiate an empty list
        output = []
        
        # iterate through each letter using index
        for a_chr in text.lower():
            
            if a_chr == ' ':  # if it is a space character
                output.append(' ')
            else:
                new_key = (self.a_rev *(self.letters.index(a_chr) - self.b)) % self.m
                output.append(self.letters[new_key])
        
        return ''.join(output)


class Keyword(Cipher):
    """
    keyword cipher see: https://en.wikipedia.org/wiki/Keyword_cipher
    """

      
    def __init__(self, key = 'kryptos', letters = 'abcdefghijklmnopqrstuvwxyz'):
        self.key_1 = key
        self.key_2 = ''.join([x for x in letters if x not in self.key_1])
        self.key = self.key_1 + self.key_2
        self.encrypts = {letters[x]: self.key[x] for x in range(len(letters))}
        self.decrypts = {val: key for key, val in self.encrypts.items()}
        
    def encrypt(self, text):
        """
        a method to encry an input text string
        """
        # initiate an empty list
        output = []
        
        # iterate through each letter using index
        for a_chr in text.lower():
            
            if a_chr == ' ':  # if it is a space character
                output.append(' ')
            else:  # add encrypted letter to the output string
                output.append(self.encrypts[a_chr])
        
        return ''.join(output)
    
    
    def decrypt(self, text):
        """
        a method to encry an input text string
        """
        # initiate an empty string
        output = []
        # iterate through each character
        for a_chr in text.lower():
            if a_chr == ' ':  # if it is a space character
                output.append(' ')
            else:  # add decrypted letter to the output string
                output.append(self.decrypts[a_chr])
        
        return ''.join(output)



if __name__ == '__main__':

    # main loop to keep the game continuing or exitting
    while True:
        # choice of encryption or decryption
        print('\nWhat are you going to do? \n\nEnter "E" for encrypt \nEnter "D" for decrypt \n ')
        to_do = input('please choose what to do: ')

        if to_do.lower() == 'e':
            print('\nA piece of cake, here is the list of available ciphers:')
            
            while True:
                # choice of 1 out of 3 ciphers
                print('Enter "A" to choose Atbash cipher \nEnter "B" to choose Affline cipher \nEnter "C" to choose Keyword cipher \n')
                choice = input('Please choose a cipher: ').lower()

                if choice == 'a':
                    my_cipher = Atbash()
                    print('\nExcellent! You chose Atbash ciper\n')
                    break

                elif choice == 'b':
                    print('\nExcellent! You chose Affline ciper\n')
                    choice_a = input('pick a non-zero integer (not 1,2,13,26 as it needs to be coprime with 26) for parameter "a": ')
                    choice_b = input('pick a non-zero integer for parameter "b": ')
                    my_cipher = Affline(int(choice_a), int(choice_b))
                    break

                elif choice == 'c':
                    print('\nExcellent! You chose Keyword ciper\n')
                    a_key = input('Please enter your choice of key (e.g. "kryptos"): ')
                    my_cipher = Keyword(key = a_key)
                    break

                else:
                    print('Invalid input, please choose again\n')
                    continue

            

            # enter text
            text = input('Please enter the text you want to encrypt: ')
            print('Here is your encrpyted message: {}\n'.format(my_cipher.encrypt(text)))

            # choice of playing again or making an exit
            next_choice = input('Do you want to try more (Y/N)?')

            if next_choice.lower() == 'y':
                continue
            else: 
                print('\nGood-bye\n')
                break

        elif to_do.lower() == 'd':
            print('\nA piece of cake, here is the list of available ciphers:')
            
            while True:
                # choice of cipher
                print('Enter "A" to choose Atbash cipher \nEnter "B" to choose Affline cipher \nEnter "C" to choose Keyword cipher \n')
                choice = input('Please choose a cipher: ').lower()

                if choice == 'a':
                    print('\nExcellent! You chose Atbash ciper\n')
                    my_cipher = Atbash()
                    break

                elif choice == 'b':
                    print('\nExcellent! You chose Affline ciper\n')
                    choice_a = input('pick a non-zero integer (not 1,2,13,26 as it needs to be coprime with 26) for parameter "a": ')
                    choice_b = input('pick a non-zero integer for parameter "b": ')
                    my_cipher = Affline(int(choice_a), int(choice_b))
                    break

                elif choice == 'c':
                    print('\nExcellent! You chose Keyword ciper\n')
                    a_key = input('Please enter your choice of key (e.g. "kryptos"): ')
                    my_cipher = Keyword(key = a_key)
                    break

                else:
                    print('Invalid input, please choose again\n')
                    continue

            # enter text to be decrypted
            text = input('Please enter the text you want to decrypt: ')
            print('Here is your encrpyted message: {}\n'.format(my_cipher.decrypt(text)))

            # choice of staying in the game or exitting
            next_choice = input('Do you want to try more (Y/N)?')

            if next_choice.lower() == 'y':
                continue
            else: 
                print('\nGood-bye\n')
                break

        else:
            print('invalid input, please choose again')

            continue
