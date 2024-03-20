from consoleBuilder import ConsoleBuilder
from palindrome import Palindrome
from receptionistbuilder import ReceptionistBuilder
from console import Console


# 

def main():
    #console_builder = ConsoleBuilder()   on peut supp console  builder
    receptionistBuilder = ReceptionistBuilder()
    receptionist = receptionistBuilder.build()
    palindrome = Palindrome(" ")
    console = Console(palindrome, receptionist)
    
    #console = console_builder.build()
    
    console.launchConsole()

if __name__ == "__main__":
    main()
