from typing import Any, Text, Dict, List

from rasa_sdk import Tracker, Action
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from service.action import get_text_weather_date
from service.normalization import text_to_date
from service.weather_api import get_weather_api


# class WeatherForm(FormAction):
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         """A list of required slots that the form has to fill"""
#
#         return ["address", "date-time"]
#
#     def name(self) -> Text:
#         return "action_report_weather"
#
#     def submit(self,
#                dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         address = tracker.get_slot('address')
#         date_time = tracker.get_slot('date-time')
#
#         date_time_number = text_date_to_number_date(date_time)
#
#         if isinstance(date_time_number, str):  # parse date_time failed
#             msg = "暂不支持查询 {} 的天气".format([address, date_time_number])
#             return [SlotSet("matches", msg)]
#             # print(msg)
#             # dispatcher.utter_message(msg)
#         else:
#             weather_data = get_text_weather_date(address, date_time,
#                                                  date_time_number)
#             return [SlotSet("matches", "{}".format(weather_data))]
#             # print(weather_data)
#             # dispatcher.utter_message(weather_data)
#
#         # utter submit template
#         # dispatcher.utter_template('utter_submit', tracker)
#         # return []

class ActionWeather(Action):

	def name(self):
		return "action_weather"

	def run(self, dispatcher, tracker, domain):
		date = next(tracker.get_latest_entity_values('date'), None)
		searching_date = "none"
		if date is not None:
			searching_date = date
		location = next(tracker.get_latest_entity_values('location'), None)
		searching_location = "none"
		if location is not None:
			searching_location = location
		data = {
			"intent" : "action_weather",
			"date" : searching_date,
			"location" : searching_location
		}
		dispatcher.utter_message(format(data))
		return []
		
class ActionReportWeather(Action):
    def name(self):
		return "action_report_weather"

    def run(self, dispatcher, tracker, domain):
		date = next(tracker.get_latest_entity_values('date'), None)
		searching_date = "none"
		if date is not None:
			searching_date = date
		location = next(tracker.get_latest_entity_values('location'), None)
		searching_location = "none"
		if location is not None:
			searching_location = location
		data = {
			"intent" : "action_weather",
			"date" : searching_date,
			"location" : searching_location
		}
		dispatcher.utter_message(format(data))
		return []
