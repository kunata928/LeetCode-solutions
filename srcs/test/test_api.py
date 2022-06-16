import requests

# api_uri = 'http://numbersapi.com/999/math?json=true'
# res = requests.get(api_uri)

nums = [
962,
931,
932,
997,
966,
967,
904,
905,
972,
973,
974,
945,
983,
988,
959,
]

for num in nums:
    api_uri = 'http://numbersapi.com/' + str(num) + '/math?json=true'
    if requests.get(api_uri).json()['found']:
        print('Interesting')
    else:
        print('Boring')