class Dashboard:
    def __init__(self, palindrome, botGreeter):
        self.palindrome = palindrome
        self.botGreeter = botGreeter

    def greet_user(self, name):
        return self.botGreeter.greet(name)

    def set_palindrome(self, input_text):
        self.palindrome.inputText = input_text
        self.palindrome.get_palindrome()

    def get_palindrome_result(self):
        return self.palindrome.get_result()

    def say_goodbye(self, name):
        return self.botGreeter.say_goodbye(name)

    def launchDashboard(self, name):
        # Greet the user
        greeting = self.greet_user(name)
        print(greeting)

        # Ask for input
        input_text = input("Enter a text: ")
        
        # Set palindrome and get result
        self.set_palindrome(input_text)
        palindrome_result = self.get_palindrome_result()

        # Say goodbye
        goodbye_message = self.say_goodbye(name)
        
        # Return palindrome result and say goodbye
        print(palindrome_result)
        print(goodbye_message)