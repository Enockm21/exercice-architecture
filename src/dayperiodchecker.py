import datetime

class DayPeriodChecker:
"""
Check the periode of the day using system Time
@author : Ahmed Bouzidia
"""
    def __init__(self):
        pass

    def get_day_period(self):
        # Récupérer l'heure actuelle du système
        current_hour = datetime.datetime.now().hour

        # Déterminer la période de la journée en fonction de l'heure
        if current_hour < 12:
            return DayPeriodGrammar.MORNING
        elif current_hour < 18:
            return DayPeriodGrammar.AFTERNOON
        else:
            return DayPeriodGrammar.EVENING 

# Exemple d'utilisation
if __name__ == "__main__":
    day_period_checker = DayPeriodChecker()
    current_period = day_period_checker.get_day_period()
    print("Période de la journée :", current_period)
