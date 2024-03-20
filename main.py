import datetime

class MirrorApp:
    def __init__(self, language='en'):
        self.language = language
        self.greetings = {
            'fr': {
                'morning': 'Bonjour',
                'afternoon': 'Bon après-midi',
                'evening': 'Bonsoir'
            },
            'en': {
                'morning': 'Good morning',
                'afternoon': 'Good afternoon',
                'evening': 'Good evening'
            }
        }
        self.farewells = {
            'fr': {
                'morning': 'Au revoir',
                'afternoon': 'Au revoir',
                'evening': 'Bonne nuit'
            },
            'en': {
                'morning': 'Goodbye',
                'afternoon': 'Goodbye',
                'evening': 'Good night'
            }
        }

    def get_time_of_day(self):
        hour = datetime.datetime.now().hour
        if 6 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 18:
            return 'afternoon'
        else:
            return 'evening'

    def greet(self):
        time_of_day = self.get_time_of_day()
        print(self.greetings[self.language][time_of_day])

    def farewell(self):
        time_of_day = self.get_time_of_day()
        print(self.farewells[self.language][time_of_day])

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    def run(self):
            self.greet()
            user_input = input("Écrivez quelque chose: ").strip()
            if self.is_palindrome(user_input.replace(" ", "").lower()):
                if self.language == 'fr':
                    print(user_input[::-1])
                    print("Bien dit !")
                else:
                    print(user_input[::-1])
                    print("Well said!")
            else:
                print(user_input[::-1])
            self.farewell()
if __name__ == "__main__":
    language = input("Choisissez votre langue (fr/en): ").lower()
    app = MirrorApp(language)
    app.run()








# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y

#     # Assure que le point est immuable en n'ayant pas de setters (setters non définis)

#     def get_x(self):
#         return self.__x

#     def get_y(self):
#         return self.__y

# def manhattan_distance(point_a, point_b):
#     return abs(point_a.get_x() - point_b.get_x()) + abs(point_a.get_y() - point_b.get_y())

# # Exemple d'utilisation
# point1 = Point(1, 2)
# point2 = Point(4, 6)
# print(manhattan_distance(point1, point2))