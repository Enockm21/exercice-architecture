from palindrome import Palindrome
from botgreeter import BotGreeter

class Dashboard:
    def __init__(self, palindrome, botGreeter):
        self.palindrome = palindrome
        self.botGreeter = botGreeter

    def greet_user(self,):
        return self.botGreeter.greet()

    def set_palindromeText(self, input_text):
        self.palindrome.setText(input_text)
        self.palindrome.get_palindrome()

    def get_palindrome_result(self):
        return self.palindrome.get_result()

    def say_goodbye(self):
        return self.botGreeter.say_goodbye()

    def tell_user_is_palindrome(self):
        return self.botGreeter.feliciter()    

    def tell_user_not_palindrome(self):
        return self.botGreeter.blam()

    def launchDashboard(self):
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