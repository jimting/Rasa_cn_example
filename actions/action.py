from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


class ActionAskWeather(Action):
    def name(self):
        return 'action_ask_weather'

    def run(self, dispatcher, tracker, domain):
        city = next(tracker.get_latest_entity_values('city'), None)
		searching_city = "none"
		if city is not None:
			searching_city = city
		date = next(tracker.get_latest_entity_values('date'), None)
		searching_date = "none"
		if date is not None:
			searching_date = date
		data = {
			"intent" : "action_ask_weather",
			"city" : searching_city,
			"date" : searching_date
		}
		dispatcher.utter_message(format(data))
		return []
