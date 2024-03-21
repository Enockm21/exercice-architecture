import datetime

from clockgrammar import ClockGrammar

 
    #Ahmed  Service 
class Clock:  #rennomer en Clock
    """
    Check the periode of the day using system Time
    @author : Ahmed Bouzidia
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 20-03-2024
    """
    
    def get_day_period(self):
        # Récupérer l'heure actuelle du système
        current_hour = datetime.datetime.now().hour

        # Déterminer la période de la journée en fonction de l'heure
        if current_hour < 12:
            return ClockGrammar.MORNING
        elif current_hour < 18:
            return ClockGrammar.AFTERNOON
        else:
            return ClockGrammar.EVENING 
