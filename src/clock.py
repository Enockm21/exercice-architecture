import datetime

from clockgrammar import ClockGrammar

class Clock: 
    """
    - Check the periode of the day using system Time

    @author : Ahmed Bouzidia
    @author : ahmed.bouzidia@ecoles-epsi.net
    @version : 21-03-2024
    """
    
    def get_day_period(self):
        # Recuperate local system time
        current_hour = datetime.datetime.now().hour

        # Get day period
        if current_hour < 12:
            return ClockGrammar.MORNING
        elif current_hour < 18:
            return ClockGrammar.AFTERNOON
        else:
            return ClockGrammar.EVENING 
