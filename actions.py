from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import json

# To ignore Warnings
from warnings import simplefilter
simplefilter('ignore', category=FutureWarning)


class ActionGetData(Action):
    def name(self):
        return 'action_getData'

    def run(self, dispatcher, tracker, domain):
        try:
            location = tracker.get_slot('country')
            request = {"location": location}
            header = {'content-type':'application/json'}
            jsonrequest =json.dumps(request)

            reply = requests.post(
                url='http://127.0.0.1:8000/getData/',
                data=jsonrequest,
                headers=header,
                timeout=10
            )
            jsonresponse = reply.json()
            response = jsonresponse['reply']

            dispatcher.utter_message(response)
            return [SlotSet('country', location)]

        except Exception:
            location = tracker.get_slot('country')
            response = 'Sorry! An error has been encountered. Please try after sometime.'
            dispatcher.utter_message(response)
            return [SlotSet('country', location)]


class ActionGetContainmentZone(Action):
    def name(self):
        return 'action_GetContainment'

    def run(self, dispatcher, tracker, domain):
        try:
            location = tracker.get_slot('location')
            request = {"location": location}
            header = {"content-type": "application/json"}
            jsonrequest = json.dumps(request)

            reply = requests.post(
                url='http://127.0.0.1:8000/getContainmentZone/',
                data=jsonrequest,
                headers=header,
                timeout=10
            )
            jsonresponse = reply.json()
            response = jsonresponse['reply']

            dispatcher.utter_message(response)
            return SlotSet('location', location)

        except Exception:
            location = tracker.get_slot('location')
            response = 'Sorry! An error has been encountered. Please try after sometime.'
            dispatcher.utter_message(response)
            return SlotSet('location', location)


class ActionGetLatestNews(Action):
    def name(self):
        return 'action_getLatestnews'

    def run(self, dispatcher, tracker, domain):
        try:
            title = []
            url = []
            newsbody = ''

            category = tracker.get_slot('category')
            request = {"category": category}
            header = {"content-type": "application/json"}
            jsonrequest = json.dumps(request)

            newsdata = requests.post(
                url='http://127.0.0.1:8000/getLatestNews/',
                data=jsonrequest,
                headers=header,
                timeout=20
            )
            jsonresponse = newsdata.json()

            if isinstance(jsonresponse, dict):
                dispatcher.utter_message(jsonresponse['reply'])
                return SlotSet('category', category)

            else:
                replyheader = 'The top headlines are: '

                for i in range(len(jsonresponse)):
                    title.append(jsonresponse[i]['title'])
                    url.append(jsonresponse[i]['url'])

                    newsbody += '\n' + str(i) + '.' + ' ' + title[i] + '\n' + url[i]

                response = replyheader + '\n' + newsbody

                dispatcher.utter_message(response)
                return SlotSet('category', category)

        except Exception:
            category = tracker.get_slot('category')
            response = 'Sorry! An error has been encountered. Please try after sometime.'
            dispatcher.utter_message(response)
            return SlotSet('category', category)
