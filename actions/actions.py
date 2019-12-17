from rasa_core_sdk import Action

class ActionAskWeather(Action):
    def name(self):
        return 'action_ask_weather'

    def run(self, dispatcher, tracker, domain):
        searching_city = next(tracker.get_latest_entity_values('city'), None)
        searching_date = next(tracker.get_latest_entity_values('date'), None)
        data = {
            "intent" : "action_ask_weather",
            "city" : searching_city,
            "date" : searching_date
        }
        dispatcher.utter_message(format(data))
        return []
