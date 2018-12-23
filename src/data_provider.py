import requests
from logger import Logger
import json
import urllib3

class DataProvider:

    def __init__(self):
        self.logger = Logger()

    def get_team_details_by_id(self, team_id):

        url = "https://sportsrivals.cronelea.ie/sportsrivals-data-service/api/teams/" + team_id

        try:
            result = requests.get(url)

            if (result.status_code == 200):

                team_dict = json.loads(result.text)

                teamId = team_dict["id"]
                rating = team_dict["rating"]

                return {"teamId": teamId, "rating": rating}
            else:
                self.logger.info_log("Error Getting Team From Api Id: " + team_id)
        except TimeoutError:
            self.logger.info_log("REST request has timed out")
        except urllib3.exceptions.NewConnectionError:
            self.logger.info_log("REST new connection error")
        except urllib3.exceptions.MaxRetryError:
            self.logger.info_log("REST max retry error")
        except requests.exceptions.ConnectionError:
            self.logger.info_log("REST connection error")
        except:
            self.logger.info_log("REST error")

