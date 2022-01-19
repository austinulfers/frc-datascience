import requests
import pandas as pd
from secrets import AUTH_TOKEN


def get_event_schedule(
        year: int,
        event_code: str,
        team_number: int,
        tournamanet_level: str,
        start: int = None,
        end: int = None) -> dict:
    """Retrieves the event schedule for a given event.

    Args:
        year (int): The year of the event.
        event_code (str): The event code of the event.
        team_number (int): The team number of the team.
        tournamanet_level (str): The tournamanet level of the matches.
        start (int, optional): The start match number of the event, inclusive. 
            Defaults to None.
        end (int, optional): The end match number of the event, inclusive. 
            Defaults to None.

    Returns:
        dict: The event schedule as a dict.
    """
    url = f"https://frc-api.firstinspires.org/v3.0/{year}/schedule/{event_code}"
    params = {
        "tournamentLevel": tournamanet_level,
        "teamNumber": team_number,
        "start": start,
        "end": end
    }
    headers = {
        "Authorization": f"Basic {AUTH_TOKEN}"
    }
    return requests.get(url, params=params, headers=headers).json()


def get_match_scores(
        year: int,
        event_code: str,
        tournament_level: str,
        match_number: int = None,
        start: int = None,
        end: int = None) -> dict:
    """Retrieves the match scores for a given event.

    Args:
        year (int): The year of the event.
        event_code (str): The event code of the event.
        tournament_level (str): The tournamanet level of the match.
        match_number (int, optional): The match to find. Defaults to None.
        start (int, optional): The start match number of the event, inclusive. 
            Defaults to None.
        end (int, optional): The end match number of the event, inclusive. 
            Defaults to None.

    Returns:
        dict: The match scores as a dict.
    """
    url = f"https://frc-api.firstinspires.org/v3.0/{year}/scores/{event_code}/{tournament_level}"
    params = {
        "matchNumber": match_number,
        "start": start,
        "end": end
    }
    headers = {
        "Authorization": f"Basic {AUTH_TOKEN}"
    }
    # Call the api and return the response as a dict
    return requests.get(url, params=params, headers=headers).json()


def flatten_json(y: dict) -> dict:
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


if __name__ == "__main__":
    # a = get_event_schedule(2020, "WASNO", 492, "qual")
    scores = get_match_scores(2019, "WASNO", "qual")
    flattened = [flatten_json(x) for x in scores["MatchScores"]]
    df = pd.DataFrame(flattened)
    print(df)
