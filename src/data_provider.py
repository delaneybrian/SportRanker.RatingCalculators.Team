import requests
from logger import Logger
import json

class DataProvider:

    def __init__(self):
        self.logger = Logger()

    def get_team_details_by_id(self, team_id):

        url = "http://sports-rivals.appspot.com/api/teams/search/findFirstBySportRadarId?sportRadarId=" + team_id

        result = requests.get(url)

        if(result.status_code == 200):

            team_dict = json.loads(result.text)

            teamId = team_dict["id"]
            rating = team_dict["rating"]

            return {"teamId": teamId, "rating": rating}
        else:
            self.logger.info_log("Error Getting Team From Api Id: " + team_id)