from rasa_core_sdk import Action

class ActionAskWeather(Action):
    def name(self):
        return 'action_ask_weather'

    def run(self, dispatcher, tracker, domain):
        ent = tracker.latest_message['city']
        return [SlotSet('city', ent)]
