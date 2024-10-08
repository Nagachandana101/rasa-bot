# from typing import Any, Text, Dict, List
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet

# class ActionScheduleInterview(Action):

#     def name(self) -> Text:
#         return "action_schedule_interview"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         interview_date = tracker.get_slot("interview_date")
        


#         dispatcher.utter_message(text=f"Your interview has been scheduled for  {interview_date}.")
#         return []
