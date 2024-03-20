import datetime
import json
 
class MirrorApp:
    traductionfile= open('traduction.json')
    traduction = json.load(traductionfile)

    def __init__(self, language='en'):
        self.language = language

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
        print(self.traduction["greetings"][self.language][time_of_day])

    def farewell(self):
        time_of_day = self.get_time_of_day()
        print(self.traduction["farewells"][self.language][time_of_day])    
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]
    def congratulate(self,word):
        print(self.is_palindrome(word))
        print(self.traduction["expression"][self.language]["goodjob"])



    def run(self):
        self.greet()
        user_input = input(self.traduction["expression"][self.language]["writesomething"]).strip().replace(" ", "").lower()
        if self.is_palindrome(user_input):
            self.congratulate(user_input)
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