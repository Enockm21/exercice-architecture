from palindrome import Palindrome
from receptionist import Receptionist

            #Ahmed : Objet valeur
class Console:
    """
    This class represents a console that will be launched on the terminal
    It represents the interface wich interact with the user
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024

    """
    
    def __init__(self, palindrome, receptionist):
        self.palindrome = palindrome
        self.receptionist = receptionist

    def greet_user(self,):
        return self.receptionist.greet()

    def set_palindromeText(self, input_text):
        self.palindrome.setText(input_text)
        self.palindrome.get_palindrome()

    def get_palindrome_result(self):
        return self.palindrome.get_result()

    def say_goodbye(self):
        return self.receptionist.say_goodbye()

    def tell_user_is_palindrome(self):
        return self.receptionist.feliciter()    

    def tell_user_not_palindrome(self):
        return self.receptionist.blam()

    def launchConsole(self):
        # Greet the user
        greeting = self.greet_user()
        print(greeting)

        # Ask for input
        input_text = input("Enter a text: ")
        
        # Set palindrome and get result
        self.palindrome.setText(input_text)
        
        if self.palindrome.is_palindrome():
            print (self.tell_user_is_palindrome())
        else:
            print(self.tell_user_not_palindrome())
            
        
        
        # Say goodbye
        goodbye_message = self.say_goodbye()
    
        print(goodbye_message)