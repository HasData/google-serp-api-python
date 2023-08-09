# Scrapeit Cloud Python SERP SDK

The Scrapeit Cloud Python SERP API SDK is a powerful tool that allows you to scrape Search Engine Result Pages (SERP) data from Google. With this SDK, you can easily access valuable data at scale in HTML format from any website without the need for a proxy. This SDK provides a convenient and straightforward interface to interact with the Scrape-it.cloud API and retrieve search results for specified keywords.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Usage](#usage)
5. [Supported Parameters](#supported-parameters)
6. [Response Format](#response-format)
7. [Examples and Use Cases](#examples-and-use-cases)
   - [Basic Search](#basic-search)
   - [Image Search](#image-search)
   - [News Search](#news-search)
   - [Video Search](#video-search)
   - [Shopping Search](#shopping-search)
8. [Advanced Features](#advanced-features)
9. [Best Practices](#best-practices)
10. [Troubleshooting](#troubleshooting)

## Installation

To use the Scrapeit Cloud Python SERP API SDK, you can install it via pip:

```bash
pip install google-serp-api
```

## Getting Started

Before you can use the SDK, you need to sign up for Scrapeit Cloud and obtain your API key. Visit [Scrapeit Cloud Sign-up](https://app.scrape-it.cloud/sign-up) to create an account and get your API key.

## Usage

To make API requests using the SDK, follow these steps:

1. Import the `ScrapeitCloudClient` class from the SDK:

```python
from google_serp_api import ScrapeitCloudClient
```

2. Replace `'INSERT_YOUR_API_KEY_HERE'` with your actual API key:

```python
api_key = 'YOUR_SCRAPEIT_CLOUD_API_KEY'
```

3. Create an instance of the `ScrapeitCloudClient` class with your API key:

```python
client = ScrapeitCloudClient(api_key=api_key)
```

4. Specify the search parameters in a dictionary:

```python
params = {
    "q": "pizza",
    "location": "Austin, Texas, United States",
    "num": 10,
    "domain": "google.com"
}
```

5. Make the API request using the `scrape` method and get the response:

```python
response = client.scrape(params=params)
```

6. Access the response data as text:

```python
print(response.text)
```

## Supported Parameters

The SDK supports various parameters that allow you to customize your search requests. Here are the supported parameters:

| Parameter    | Default Value | Description |
| ------------ | ------------- | ----------- |
| q            | -             | [Required] Specify the search term for which you want to scrape the SERP. |
| location     | "Austin, Texas, United States" | [Optional] Canonical location name. |
| domain       | "google.com"         | [Optional] The Google domain you want to use for the search. |
| gl           | "us"          | [Optional] The two-letter country code for the country you want to limit the search to. |
| hl           | "en"          | [Optional] The two-letter language code for the language you want to use for the search. |
| tbm          | -             | [Optional] Specify the type of search (Google SERP, Locals, Images, Videos, News or Shopping). |
| deviceType   | "desktop"     | [Optional] Specify the device type for the search. |
| start        | -             | [Optional] Result offset. |
| num          | 100           | [Optional] Number of results per page. Can be a value from 10 to 100 |

For more details on each parameter, refer to the [Scrapeit Cloud documentation](https://scrape-it.cloud/docs/google-scraping-api/serp).

## Response Format

The SDK returns the API response in JSON format. The JSON response object may include various properties depending on the specific search query. The response can contain the next data:

- `ads`: Contains information about advertisements related to the search query.
- `imagesResults`: Provides image search results related to the query.
- `onlineRelatedSearches`: Offers online related search suggestions for the query.
- `onlineVideos`: Returns online video search results related to the query.
- `knowledgeGraph`: Contains data from the Knowledge Graph for the search query.
- `localAds`: Provides local advertisements related to the search query.
- `localResults`: Contains local search results based on the query.
- `newsResults`: Offers news search results related to the query.
- `organicResults`: Contains organic web search results for the query.
- `pagination`: Provides information about pagination and navigation through search results.
- `relatedQuestions`: Contains related questions to the search query.
- `relatedSearches`: Provides related search queries to the original query.
- `searchInformation`: Contains general information about the search query.
- `topStories`: Offers top stories related to the search query.

Please note that not all properties will be present in every API response. The actual properties returned will vary based on the nature of the search and the availability of relevant data.

Here's an example of the JSON response:

```json

{
  "requestMetadata": {
    "id": "fa371203-7452-49a6-ae5d-e2937f6ad2e3",
    "googleUrl": "https://www.google.com/search?q=tea&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM%3D&gl=us&hl=en&filter=1&oq=tea&sourceid=chrome&num=10&ie=UTF-8",
    "googleHtmlFile": "https://storage.googleapis.com/scrapeit-cloud-screenshots/fa371203-7452-49a6-ae5d-e2937f6ad2e3.html",
    "status": "ok"
  },
  "searchInformation": {
    "totalResults": "5020000000",
    "timeTaken": 0.49
  },
  "organicResults": [
    {
      "position": 1,
      "title": "Texas Education Agency - Texas.gov",
      "link": "https://tea.texas.gov/",
      "displayedLink": "https://tea.texas.gov",
      "source": "Texas Education Agency (.gov)",
      "snippet": "The Latest TEA News · STAAR Redesign · Superintendents · Parent Resources · Educator Certification · Employment Opportunities · Military Families · Contact TEA.",
      "snippetHighlitedWords": [
        "TEA",
        "TEA"
      ],
      "sitelinks": {
        "expanded": [
          {
            "title": "Certificate Lookup",
            "link": "https://tea.texas.gov/texas-educators/certification/certificate-lookup",
            "snippet": "As of January 2011, TEA no longer mails paper certificates. The ..."
          },
          {
            "title": "Student Assessment",
            "link": "https://tea.texas.gov/student-assessment",
            "snippet": "STAAR Resources - Testing - The STAAR Report Card -"
          }
        ]
      }
    },
    {
      "position": 7,
      "title": "Art of Tea: Organic Loose Leaf Teas, Tea Bags & Tea Gift",
      "link": "https://www.artoftea.com/",
      "displayedLink": "https://www.artoftea.com",
      "source": "Art of Tea",
      "snippet": "Explore Art of Tea, an organic online tea shop with a wide variety of loose leaf, packaged teas, teaware, tea gifts & more. Shop custom-crafted teas today!",
      "snippetHighlitedWords": [
        "Tea",
        "tea",
        "teas",
        "tea",
        "teas"
      ]
    }
  ],
  "localResults": {
    "places": [
      {
        "position": 1,
        "title": "Sweetwaters Coffee & Tea",
        "rating": 4.6,
        "reviews": 125,
        "reviewsOriginal": "(125)",
        "price": "$",
        "address": "316 W 12th St",
        "hours": "Closed ⋅ Opens 7 AM",
        "placeId": "10992893371591908885",
        "description": "Casual spot for coffee, tea & light eats"
      },
      {
        "position": 3,
        "title": "Gong cha",
        "rating": 4.3,
        "reviews": 216,
        "reviewsOriginal": "(216)",
        "price": "$",
        "address": "above Target, 232, 2021 Guadalupe St",
        "hours": "Closed ⋅ Opens 11:30 AM",
        "serviceOptions": {
          "dineIn": true,
          "takeout": true,
          "delivery": true
        },
        "placeId": "12676559394469743261"
      }
    ],
    "moreLocationsLink": "https://www.google.com/search?gl=us&hl=en&tbs=lf:1,lf_ui:9&tbm=lcl&q=tea&rflfq=1&num=10&uule=w+CAIQICIaQXVzdGluLFRleGFzLFVuaXRlZCBTdGF0ZXM%3D&sa=X&ved=2ahUKEwjbi5bp8rCAAxX7FlkFHQU_CJ4QjGp6BAhQEAE"
  },
  "relatedSearches": [
    {
      "query": "tea texas",
      "link": "https://www.google.com/search?gl=us&hl=en&q=TEA+Texas&sa=X&ved=2ahUKEwjbi5bp8rCAAxX7FlkFHQU_CJ4Q1QJ6BAhMEAE"
    },
    {
      "query": "tea collection",
      "link": "https://www.google.com/search?gl=us&hl=en&q=Tea+Collection&sa=X&ved=2ahUKEwjbi5bp8rCAAxX7FlkFHQU_CJ4Q1QJ6BAhHEAE"
    }
  ],
  "inlineRelatedSearches": {
    "title": "Tea types",
    "items": [
      {
        "query": "Black tea",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2JGMBF985vy6gN1FB0-0KmS2YQKjrw7GE95C5UsSMT5OkI7TNXBmI&s=0",
        "link": "https://www.google.com/search?gl=us&hl=en&q=Black+tea&stick=H4sIAAAAAAAAAOOQUeLUz9U3MLIwtUwx4ixJTVQoqSxILY5iBjJPMSLkoGzD3Kqy4lOMHCC2eXJuBZRpWpBSCFNtVlZkDmWbJZsZJMPE8_LKDeBqDMwNoWwLE_OqlF-MnCEwqxtYGBexcjrlJCZnKwAdcYtNkuHWih4VrTMVT6oMzOT3_ztd6XzphJfGJPV6AMRmcnq-AAAA&sa=X&ved=2ahUKEwjbi5bp8rCAAxX7FlkFHQU_CJ4Qs9oBKAB6BAhAEAI"
      },
      {
        "query": "Matcha",
        "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRStS2F7JnJNqFpH1AjJciD744GqLgXDsrme5M0roLoYQqexBDd77mf&s=0",
        "link": "https://www.google.com/search?gl=us&hl=en&q=Matcha&stick=H4sIAAAAAAAAAOOQUeLUz9U3MEs2M0g24ixJTVQoqSxILY5iBjJPMYLljCxMLVOgbMPcqrLiU4wcILZ5cm4FlGlakFIIU21WVmQOZYNNhYnn5ZUbwNUYmBtC2RYm5lUpvxg5Q2BWN7AwLmJl800sSc5IvMUmyXBrRY-K1pmKJ1UGZvL7_52udL50wktjkno9ALanGgG7AAAA&sa=X&ved=2ahUKEwjbi5bp8rCAAxX7FlkFHQU_CJ4Qs9oBKAV6BAhAEAc"
      }
    ],
    "seeMoreLink": "https://www.google.com/search?gl=us&hl=en&q=Tea+types&stick=H4sIAAAAAAAAAOOQMeIsSU1UKKksSC2OYgYyTzFy6ufqGxhZmFqmQNmGuVVlxacYOUBs8-TcCijTtCClEKbarKzIHMo2SzYzSIaJ5-WVG8DVGJgbQtkWJuZVKb8YOUNgVjewMC5iRXBvsUky3FrRo6J1puJJlYGZ_P5_pyudL53w0pikXg8A5uXmX7MAAAA&sa=X&ved=2ahUKEwjbi5bp8rCAAxX7FlkFHQU_CJ4Q4qYDegQIQBAI"
  },
  "relatedQuestions": [
    {
      "question": "What's TEA in Texas?",
      "snippet": "The Texas Education Agency is the state agency that oversees primary and secondary public education. It is headed by the commissioner of education. The Texas Education Agency improves outcomes for all public school students in the state by providing leadership, guidance, and support to school systems.",
      "link": "https://tea.texas.gov/about-tea",
      "title": "About TEA - Texas Education Agency",
      "displayedLink": "https://tea.texas.gov › about-tea"
    },
    {
      "question": "What is Texas in education?",
      "snippet": "By FOX 26 Digital. Published February 13, 2023.",
      "link": "https://www.fox26houston.com/news/texas-ranked-10th-least-educated-state-in-the-us-wallethub-study",
      "title": "Texas ranked 10th least educated state in the US: WalletHub study",
      "displayedLink": "https://www.fox26houston.com › news"
    }
  ],
  "knowledgeGraph": {
    "title": "See results about",
    "source": {},
    "peopleAlsoSearchFor": []
  },
  "pagination": {
    "next": "https://www.google.com/search?q=tea&gl=us&hl=en&ei=nXDDZJvJN_ut5NoPhf6g8Ak&start=10&sa=N"
  }
}

```

This example demonstrates the possible properties returned in the JSON response. However, the actual response will depend on the specific search query and the available data.

## Examples and Use Cases

### Use cases

The Scrapeit Cloud Python SERP API SDK can be utilized for various applications, making it a versatile tool for developers. Some common use cases include:

- Web Scraping: Extracting valuable data from search engine result pages for analysis or storage.
- SEO Research: Gathering information on search rank rankings, competitors, and keywords for search engine optimization purposes.
- Competitor Analysis: Monitoring and analyzing competitors' online presence and performance.
- Market Research: Gathering insights on consumer behavior and market trends from search engine data.

With the ability to access data at scale, the SDK empowers developers to gain valuable insights from search engine results and apply them to different use cases.

My apologies for the oversight. You are right, the pagination parameter returns the URL for the next page of results, not a separate API endpoint. I've corrected the examples and provided multiple scenarios for different use cases using the correct parameters:

### Basic Search
In this example, we will perform a basic search for the keyword "pizza" in the US and retrieve the top 10 organic search results.

```python
from google_serp_api import ScrapeitCloudClient

api_key = 'INSERT_YOUR_API_KEY_HERE'
client = ScrapeitCloudClient(api_key)

try:
    params = {
        "q": "pizza",
        "gl": "us",
        "hl": "en",
        "num": 10
    }

    response = client.scrape(params)

    data = response.json()
    print(data)

except Exception as e:
    print(f"Error occurred: {e}")
```

### Image Search
In this example, we will perform a basic image search for the keyword "puppies" in the US and retrieve the top 100 image search results.

```python
from google_serp_api import ScrapeitCloudClient

api_key = 'INSERT_YOUR_API_KEY_HERE'
client = ScrapeitCloudClient(api_key)

try:
    params = {
        "q": "puppies",
        "gl": "us",
        "hl": "en",
        "num": 100,
        "tbm": "isch"
    }

    response = client.scrape(params)

    data = response.json()
    print(data)

except Exception as e:
    print(f"Error occurred: {e}")
```

### News Search
In this example, we will perform a basic news search for the keyword "technology" in the US and retrieve the top 10 news search results.

```python
from google_serp_api import ScrapeitCloudClient

api_key = 'INSERT_YOUR_API_KEY_HERE'
client = ScrapeitCloudClient(api_key)

try:
    params = {
        "q": "technology",
        "gl": "us",
        "hl": "en",
        "num": 10,
        "tbm": "nws"
    }

    response = client.scrape(params)

    data = response.json()
    print(data)

except Exception as e:
    print(f"Error occurred: {e}")
```

### Video Search
In this example, we will perform a basic video search for the keyword "funny cats" in the US and retrieve the top 50 video search results.

```python
from google_serp_api import ScrapeitCloudClient

api_key = 'INSERT_YOUR_API_KEY_HERE'
client = ScrapeitCloudClient(api_key)

try:
    params = {
        "q": "funny cats",
        "gl": "us",
        "hl": "en",
        "num": 50,
        "tbm": "vid"
    }

    response = client.scrape(params)

    data = response.json()
    print(data)

except Exception as e:
    print(f"Error occurred: {e}")
```

### Shopping Search
In this example, we will perform a basic shopping search for the keyword "smartphone" in the US and retrieve the top 25 shopping search results.

```python
from google_serp_api import ScrapeitCloudClient

api_key = 'INSERT_YOUR_API_KEY_HERE'
client = ScrapeitCloudClient(api_key)

try:
    params = {
        "q": "smartphone",
        "gl": "us",
        "hl": "en",
        "num": 25,
        "tbm": "shop"
    }

    response = client.scrape(params)

    data = response.json()
    print(data)

except Exception as e:
    print(f"Error occurred: {e}")
```

Replace `'INSERT_YOUR_API_KEY_HERE'` with your actual Scrapeit Cloud API key for the code to work correctly. These examples demonstrate different uses of the `tbm` parameter to perform various types of searches such as image search, news search, video search, and shopping search.

## Advanced Features

The Scrapeit Cloud Python SERP API SDK also supports advanced features to enhance your search requests. These features include pagination and filtering options, allowing you to customize and refine your queries. The [documentation](https://scrape-it.cloud/docs/google-scraping-api/serp) provides additional information on advanced parameters.

## Best Practices

To ensure a smooth experience and optimal performance while using the Scrape-it Cloud Google SERP API SDK, consider the following best practices:

1. **Review API Documentation**: Familiarize yourself with the API documentation to understand all available parameters, response formats, and potential limitations. This will help you make effective API requests and interpret the responses accurately.

2. **Use Rate Limiting**: Implement rate limiting in your code to avoid exceeding the API's rate limits. Abiding by rate limits ensures fair usage and prevents unnecessary disruptions to your API access.

3. **Test with Sample Queries**: Before making extensive use of the API, perform test queries with sample data to understand the API's behavior and validate your implementation.

4. **Monitor API Usage**: Regularly monitor your API usage and keep track of your credit balance. This allows you to manage your resources effectively and plan accordingly for your project's needs.

5. **Keep Credentials Secure**: Safeguard your API key and other sensitive credentials. Avoid hardcoding them in your code or publicly sharing them. Use environment variables or secure configuration methods to store such information.

By following these best practices, you can effectively utilize the Scrape-it Cloud Google SERP API SDK and maximize the benefits of web scraping, SEO research, competitor analysis, and market research with accurate and valuable data.

## Troubleshooting

If you encounter issues while using the Scrape-it Cloud Google SERP API, consider the following troubleshooting steps:

1. **Check your API Key**: Ensure that you have provided the correct API key in the request headers. Double-check for any typos or extra spaces in the API key.

2. **Verify Request Parameters**: Review the parameters used in your API request and make sure that all required fields are provided and properly formatted. Incorrect parameters can lead to unexpected results or errors.

3. **Inspect API Response**: Examine the API response for any error messages or status codes. The response may provide valuable insights into the issue, such as invalid queries or authentication problems.

4. **Monitor Credit and Rate Limits**: Ensure that you are not exceeding your plan's credit limits or rate limits. Regularly monitor your API usage and consider implementing rate-limiting logic to avoid hitting the rate limits.