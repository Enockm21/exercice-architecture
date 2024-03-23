
        
class Palindrome:
    """
    This class define  palindrome detecter 
    @author: Ahmed Bouzidia
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """

    def __init__(self):
        self.palindrome = ""
        self.result = False

    def validate_palindrome(self,inputText):
        # Remove non-alphanumeric characters and convert to lowercase
        cleaned_text = ''.join(char.lower() for char in inputText if char.isalnum())
        
        # Check if the cleaned text is a palindrome
        if cleaned_text == cleaned_text[::-1]:
            self.palindrome = cleaned_text
            self.result = True
        
   
    def is_palindrome(self,inputText):
        self.validate_palindrome(inputText)
        return self.result