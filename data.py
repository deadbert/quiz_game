import requests

parameters = {
    'amount': '10',
    'type': 'boolean'
}
results = requests.get(url='https://opentdb.com/api.php', params=parameters)
results.raise_for_status()

question_data = results.json()['results']
