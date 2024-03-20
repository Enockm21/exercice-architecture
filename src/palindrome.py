class Palindrome:
    def __init__(self, inputText):
        self.inputText = inputText
        self.palindrome = ""
        self.result = False

    def get_palindrome(self):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_text = ''.join(char.lower() for char in self.inputText if char.isalnum())
        
        # Check if the cleaned text is a palindrome
        if cleaned_text == cleaned_text[::-1]:
            self.palindrome = cleaned_text
            self.result = True
        else:
            self.result = False
    
    def setText(self,text):
        self.inputText = text
        self.get_palindrome()
        
    def is_palindrome(self):
        return self.result