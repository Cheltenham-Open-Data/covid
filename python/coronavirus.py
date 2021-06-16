# import
from requests import get
import json
import pathlib
import os

city = os.getenv('CITY_CODE') or 'Cheltenham'

def get_covid_data():
    endpoint = (
        f'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=ltla;areaName={city}&'
        'structure={"date":"date","areaName":"areaName","areaCode":"areaCode","cases": {"daily":"newCasesByPublishDate","cumulative":"cumCasesByPublishDate"},"deaths": {"daily":"newDeathsByDeathDate","cumulative":"cumDeathsByDeathDate"}}'
    )
    response = get(endpoint, timeout=10)
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
    return response.json()['data']

# output
if __name__ == "__main__":
    root = pathlib.Path(__file__).parent.parent.resolve()
    with open( root / "corona.json", 'r+') as filehandle:
        data = json.load(filehandle)
        new_data = get_covid_data()
        filehandle.seek(0)
        json.dump(new_data, filehandle, indent=4)
