from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import requests
import json
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

# To ignore Warnings
from warnings import simplefilter
simplefilter('ignore', category=FutureWarning)


class ActionGetData(Action):
    def name(self):
        return 'action_getData'

    def getCountryDetails(location, newdata):
        response = ''
        loc_index = newdata.index(location)
        for i in range(loc_index, loc_index + 6):
            response += newdata[i] + '\n'
        return response

    def run(self, dispatcher, tracker, domain):
        try:
            data = ''
            location = str(tracker.get_slot('country')).upper()

            # request = {"location": location}
            # header = {'content-type':'application/json'}
            # jsonrequest =json.dumps(request)

            # reply = requests.post(
            #     url='http://127.0.0.1:8000/getData/',
            #     data=jsonrequest,
            #     headers=header,
            #     timeout=10
            # )
            # jsonresponse = reply.json()
            # response = jsonresponse['reply']

            if location == 'AMERICA':
                location = 'USA'

            if location == 'ENGLAND':
                location = 'UK'

            html_doc = requests.get('https://www.worldometers.info/coronavirus/', timeout=30)
            soupDoc = BeautifulSoup(html_doc.text, 'html.parser')

            for tr in soupDoc.find_all('table', {'id': 'main_table_countries_today'}):
                data += tr.get_text()
            newdata = (data.split('All', 1)[1])[3:].split('\n')

            for i in range(len(newdata)):
                newdata[i] = newdata[i].upper().strip()

            if location in newdata:
                response = ActionGetData.getCountryDetails(location, newdata).split('\n')

                for i in range(len(response)):
                    if not response[i]:
                        response[i] = 0
                    if i == 2 or i == 4:
                        if response[i] != 0:
                            response[i] = response[i].split('+')[1]

                response = f'{response[0].capitalize()} has a total of {response[1]} confirmed cases from which ' \
                    f'there has been {response[3]} deaths till now and {response[5]} have ' \
                    f'successfully recovered. As of this moment, {response[2]} new cases have been ' \
                    f'identified today and {response[4]} people have passed away.'

            else:
                response = 'Oops! Seems like this is not a country. Please enter a valid country name.'

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

    def getLatLong(location):
        geolocator = Nominatim(user_agent="covbot2020")
        location = geolocator.geocode(location)
        lat, long = location.latitude, location.longitude
        return lat, long

    def run(self, dispatcher, tracker, domain):
        try:
            location = str(tracker.get_slot('location')).capitalize()

            # request = {"location": location}
            # header = {"content-type": "application/json"}
            # jsonrequest = json.dumps(request)

            lat, lng = ActionGetContainmentZone.getLatLong(location.capitalize())

            latlngs = [lat, lng]
            key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtYWlsSWRlbnRpdHkiOiJtc3VkaXB0bzI4QGdtYWlsLmNvbSJ9.' \
                  'If_z1b0Apd-1pZsz7YnuXcj6C-z1tG7-VscMmyLy7-g'
            externalapirequest = {"key": key,
                                  "latlngs": [
                                      latlngs
                                  ]
                                  }
            headers = {'content-type': 'application/json'}
            jsondata = json.dumps(externalapirequest)
            response = requests.post('https://data.geoiq.io/dataapis/v1.0/covid/locationcheck',
                                     data=jsondata, headers=headers, timeout=30)

            jsonresponse = response.json()
            data = json.dumps(jsonresponse['data'])
            zone = (data.split('districtZoneType', 1)[1])[4:].split('inContainmentZone', 1)[0].split('"')[0]
            response = f'As per the latest updates, {location.capitalize()} is in {zone} now.'

            # reply = requests.post(
            #     url='http://127.0.0.1:8000/getContainmentZone/',
            #     data=jsonrequest,
            #     headers=header,
            #     timeout=10
            # )
            # jsonresponse = reply.json()
            # response = jsonresponse['reply']

            dispatcher.utter_message(response)
            return SlotSet('location', location)

        except AttributeError:
            location = tracker.get_slot('location')
            response = 'I am afraid I could not find details about this location at the moment.'
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
            titleurl = []
            newsbody = ''

            category = str(tracker.get_slot('category')).lower()
            # request = {"category": category}
            # header = {"content-type": "application/json"}
            # jsonrequest = json.dumps(request)

            url = (f'http://newsapi.org/v2/top-headlines?country=in&category={category}&'
                   f'apiKey=312fa5cd53b64950a907fbc65b7d30a0')

            response = requests.get(url, timeout=30)
            jsonresponse = response.json()

            articles = jsonresponse['articles']

            if jsonresponse['totalResults'] == 0:
                raise AttributeError

            else:
                replyheader = 'The top headlines are: '

                for i in range(len(articles)):
                    title.append(articles[i]['title'])
                    titleurl.append(articles[i]['url'])

                    newsbody += '\n' + str(i) + '.' + ' ' + title[i] + '\n' + titleurl[i]

                response = replyheader + '\n' + newsbody

                # newsdata = requests.post(
                #     url='http://127.0.0.1:8000/getLatestNews/',
                #     data=jsonrequest,
                #     headers=header,
                #     timeout=20
                # )
                # jsonresponse = newsdata.json()
                #
                # if isinstance(jsonresponse, dict):
                #     dispatcher.utter_message(jsonresponse['reply'])
                #     return SlotSet('category', category)
                #
                # else:
                #     replyheader = 'The top headlines are: '
                #
                #     for i in range(len(jsonresponse)):
                #         title.append(jsonresponse[i]['title'])
                #         url.append(jsonresponse[i]['url'])
                #
                #         newsbody += '\n' + str(i) + '.' + ' ' + title[i] + '\n' + url[i]
                #
                #     response = replyheader + '\n' + newsbody

                dispatcher.utter_message(response)
                return SlotSet('category', category)

        except AttributeError:
            category = tracker.get_slot('category')
            response = 'I am afraid details regarding this category is not available at the moment.'
            dispatcher.utter_message(response)
            return SlotSet('category', category)

        except Exception:
            category = tracker.get_slot('category')
            response = 'Sorry! An error has been encountered. Please try after sometime.'
            dispatcher.utter_message(response)
            return SlotSet('category', category)
