import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Sashreek007/59baa143843298c7d7f26a35afd85949/raw/64d6300fa724585ca514938de25f466f6f27bb6a/eden-marcho-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
        }

        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
    data = response.json().get("person")

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            "https://www.linkedin.com/in/eden-marco/",
        )
    )
