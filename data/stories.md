## story_001
* greet
  - utter_greet
* inform_stats{"country":"India"}
  - action_getData
  - slot{"country":"India"}
* goodbye
  - utter_goodbye

## story_002
* greet
  - utter_greet
* inform_stats
  - utter_ask_country
* inform_stats{"country":"Italy"}
  - action_getData
  - slot{"country":"Italy"}
* goodbye
  - utter_goodbye

## story_003
* greet
  - utter_greet
* inform_zone{"location":"Bhubaneswar"}
  - action_GetContainment
  - slot{"location":"Bhubaneswar"}
* goodbye
  - utter_goodbye

## story_004
* greet
  - utter_greet
* inform_zone
  - utter_ask_location
* inform_zone{"location":"Raipur"}
  - action_GetContainment
  - slot{"location":"Raipur"}
* goodbye
  - utter_goodbye

## story_005
* greet
  - utter_greet
* inform_news{"category":"health"}
  - action_getLatestnews
  - slot{"category":"health"}
* goodbye
  - utter_goodbye

## story_006
* greet
  - utter_greet
* inform_news
  - utter_ask_category
* inform_news{"category":"technology"}
  - action_getLatestnews
  - slot{"category":"technology"}
* goodbye
  - utter_goodbye

## story_007
* greet
  -utter_greet
* inform_self
  - utter_self
* goodbye
  - utter_goodbye

## story_008
* greet
  -utter_greet
* inform_stats{"country":"Afghanistan"}
  - action_getData
  - slot{"country":"Afghanistan"}
* inform_zone
   - utter_ask_location
* inform_zone{"location":"Bhubaneswar"}
  - action_GetContainment
  - slot{"location":"Bhubaneswar"}
* inform_news{"category":"health"}
  - action_getLatestnews
  - slot{"category":"health"}
* bot_challenge
  - utter_iamabot
* goodbye
  - utter_goodbye

## story_009
* inform_zone{"location":"Bhubaneswar"}
  - action_GetContainment
  - slot{"location":"Bhubaneswar"}
* inform_stats{"country":"Belgium"}
  - action_getData
  - slot{"country":"Belgium"}
* inform_news
  - utter_ask_category
* inform_news{"category":"health"}
  - action_getLatestnews
  - slot{"category":"health"}
* inform_self
  - utter_self
* goodbye
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## interactive_story_1
* greet
    - utter_greet
* inform_stats
    - utter_ask_country
* inform_country{"country": "China"}
    - slot{"country": "China"}
    - action_getData
    - slot{"country": "China"}
* inform_zone{"location": "bhubaneswar"}
    - slot{"location": "bhubaneswar"}
    - action_GetContainment
* inform_news
    - utter_ask_category
* inform_category{"category": "health"}
    - slot{"category": "health"}
    - action_getLatestnews
* inform_news{"category": "technology"}
    - slot{"category": "technology"}
    - action_getLatestnews
* goodbye
    - utter_goodbye

## interactive_story_1
* bot_challenge
    - utter_iamabot
* inform_self
    - utter_self
* inform_stats
    - utter_ask_country
* inform_stats{"country": "bangladesh"}
    - slot{"country": "bangladesh"}
    - action_getData
    - slot{"country": "bangladesh"}
* inform_zone
    - utter_ask_location
* inform_location{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_GetContainment
* goodbye
    - utter_goodbye

## interactive_story_1
* out_of_scope
    - utter_default
* out_of_scope
    - utter_default

## interactive_story_1
* greet
    - utter_greet
* inform_news
    - utter_ask_category
* inform_category{"category": "technology"}
    - slot{"category": "technology"}
    - action_getLatestnews
* inform_news
    - utter_ask_category
* inform_category{"category": "general"}
    - slot{"category": "general"}
    - action_getLatestnews
* inform_stats{"country": "Bangladesh"}
    - slot{"country": "Bangladesh"}
    - action_getData
    - slot{"country": "Bangladesh"}
* inform_self
    - utter_self
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
* affirm
    - utter_happy
* inform_zone
    - utter_ask_location
* inform_location{"location": "Immadihalli"}
    - slot{"location": "Immadihalli"}
    - action_GetContainment

## interactive_story_1
* greet
    - utter_greet
* inform_news{"category": "science"}
    - slot{"category": "science"}
    - action_getLatestnews
* inform_stats{"country": "Germany"}
    - slot{"country": "Germany"}
    - action_getData
    - slot{"country": "Germany"}
* goodbye
    - utter_goodbye
    - action_restart

## New Story

* greet
    - utter_greet
* bot_challenge
    - utter_iamabot
* inform_self
    - utter_self
* inform_stats
    - utter_ask_country
* inform_country{"country":"India"}
    - action_getData
* inform_stats{"country":"China"}
    - action_getData
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* inform_stats
    - utter_ask_country
* inform_stats{"country": "ireland"}
    - slot{"country": "ireland"}
    - action_getData
    - slot{"country": "IRELAND"}
* inform_country{"country": "canada"}
    - slot{"country": "canada"}
    - action_getData
    - slot{"country": "CANADA"}
* inform_stats{"country": "england"}
    - slot{"country": "england"}
    - action_getData
    - slot{"country": "UK"}
* inform_zone
    - utter_ask_location
* inform_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_GetContainment
* inform_zone{"location": "Indore"}
    - slot{"location": "Indore"}
    - action_GetContainment
* inform_news
    - utter_ask_category
* inform_news{"category": "entertainment"}
    - slot{"category": "entertainment"}
    - action_getLatestnews
* inform_category{"category": "science"}
    - slot{"category": "science"}
    - action_getLatestnews
* mood_unhappy
    - utter_cheer_up
    - utter_did_that_help
* goodbye
    - utter_goodbye
