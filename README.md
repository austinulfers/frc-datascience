# frc-datascience

Utilizes Python 3.8 however, I belive most 3.x versions should work.

Create the environment:
- `python -m venv env`

Enable the environment:
- `\env\Scripts\activate`

Install the dependencies:
- `pip install -r requirements.txt`

Get your FIRST API authentication key:
- https://frc-events.firstinspires.org/services/api/register

Convert your api-key to a base64 token:
- `python src/base64_encode.py --string "API_KEY"`

Add your token to a newly created src/secrets.py file.
- `FIRST_AUTH_TOKEN = "API_TOKEN"`

Get your The Blue Alliance authetication key:
- https://www.thebluealliance.com/account

Add your key to the src/secrets.py file:
- `TBA_AUTH_KEY = "API_KEY"`