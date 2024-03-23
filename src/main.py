from palindrome import Palindrome
from hostbuilder import HostBuilder
from console import Console


def main():
    """"
      - Main class : lauch the console
      @version : 23-03-2024
      @author : ahmedbouzidia81@gmail.com
    """
    host_builder = HostBuilder()
    my_host = host_builder.build()
    palindrome = Palindrome()
    console = Console(palindrome, my_host)
    console.launchConsole()


if __name__ == "__main__":
    main()
