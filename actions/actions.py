from rasa_core_sdk import Action

class ActionAskWeather(Action):
    def name(self):
        return 'action_ask_weather'

    def run(self, dispatcher, tracker, domain):
        searching_city = next(tracker.get_latest_entity_values('city'), None)
        dispatcher.utter_message(searching_city + "的天氣很好哦！")
        return []
