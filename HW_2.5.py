import json
import requests

# case 1
response = requests.get("https://gist.githubusercontent.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37/raw/4b1d72e0ac353b36c58b7a3a9e90fa163d57919f/some.json")
# print(response.text[1:-1])
# print(len(response.text))
json_text = json.loads(response.text[1:-1])
print(json_text['messages'][1]['message'])


# case 2
json_text1 = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text1)
print(obj['messages'][1]['message'])


# case 3
response = requests.get("https://gist.githubusercontent.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37/raw/4b1d72e0ac353b36c58b7a3a9e90fa163d57919f/some.json")
j_t = response.text
j_t_dict = json.loads(j_t[1:-1])
print(j_t_dict['messages'][1]['message'])
