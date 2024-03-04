def get_gifs(query: str, api_key: str = giphy_api_key) -> list:
    """
    Get a list of URLs of GIFs based on a given query..
    """
    formatted_query = "+".join(query.split())
    url = f"https://api.giphy.com/v1/gifs/search?q={formatted_query}&api_key={api_key}"
    gifs = requests.get(url).json()["data"]
    return [gif["url"] for gif in gifs]


if __name__ == "__main__":
    print("\n".join(get_gifs("space ship")))

def extract_user_profile(script) -> dict:
    """
    May raise json.decoder.JSONDecodeError
    """
    data = script.contents[0]
    info = json.loads(data[data.find('{"config"') : -1])
    return info["entry_data"]["ProfilePage"][0]["graphql"]["user"]
#good
  def __init__(self, username):
        self.url = f"https://www.instagram.com/{username}/"
        self.user_data = self.get_json()

    def get_json(self) -> dict:
        """
        Return a dict of user information
        """
        html = requests.get(self.url, headers=headers).text
        scripts = BeautifulSoup(html, "html.parser").find_all("script")
        try:
            return extract_user_profile(scripts[4])
        except (json.decoder.JSONDecodeError, KeyError):
            return extract_user_profile(scripts[3])
