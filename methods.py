# create a method to search
# display the content
# weather report
# speech option
def get_input(material):
    _input = material.get()
    print(_input)
    import requests
    import json
    url = f"https://newsapi.org/v2/everything?q={material}&from=2022-02-21&sortBy=popularity&apiKey=fb358baaf0a349cea5135ebf84961e87"
    print(url)
    # response_api = requests.get(url)
    # data = response_api.text
    # parse_json = json.loads(data)
    # print(parse_json)
    # print(response_api)