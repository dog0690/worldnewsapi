import worldnewsapi
from worldnewsapi.rest import ApiException
from pprint import pprint


configuration = worldnewsapi.Configuration(
    host = "https://api.worldnewsapi.com"
)
configuration.api_key['apiKey'] = "c1b669de7e8f43bb8b606ba5dd5706c9"
configuration.api_key['headerApiKey'] = "c1b669de7e8f43bb8b606ba5dd5706c9"

with worldnewsapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = worldnewsapi.NewsApi(api_client)
    url = 'https://www.bbc.com/news/world-us-canada-59340789' # str | The url of the news.
    analyze = True # bool | Whether to analyze the extracted news (extract entities, detect sentiment etc.) (optional)

    try:
        # Extract News
        api_response = api_instance.extract_news(url, analyze=analyze)
        print("The response of NewsApi->extract_news:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NewsApi->extract_news: %s\n" % e)