from palindrome import Palindrome
from host import Host

        
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

    def get_palindrome_result(self):
        return self.palindrome.get_result()

    def say_goodbye(self):
        return self.receptionist.say_goodbye()

    def tell_user_is_palindrome(self):
        return self.receptionist.congratulate()

    def tell_user_not_palindrome(self):
        return self.receptionist.blame()

    def launchConsole(self):
        # Greet the user
        greeting = self.greet_user()
        print(greeting)

        # Ask for input
        input_text = input("Enter a text: ")
        
        # Set palindrome and get result
        
        
        if self.palindrome.is_palindrome(input_text):
            print (self.tell_user_is_palindrome())
        else:
            print(self.tell_user_not_palindrome())
            
        
        
        # Say goodbye
        goodbye_message = self.say_goodbye()
    
        print(goodbye_message)