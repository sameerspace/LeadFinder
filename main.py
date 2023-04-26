import pprint

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from geonamescache import GeonamesCache

from scraper import run_parse


app = FastAPI()
CORSMiddleware(app)

gc = GeonamesCache()
countries = gc.get_countries()
ct_by_cntry = {}


# for country in countries:
#     ct_by_cntry[country['name']] = [city['name'] for city['name'] in gc.get_cities(country['iso'])]

templates = Jinja2Templates("templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "name": "world",
        },
        media_type="text/html",
    )


# http://localhost:8000/search/?query=pizza&country=pakistan&city=karachi
@app.get("/search/")
def search(query: str):
    # link = f"https://www.google.com/maps/search/{query}+in+{city},{country}/"
    link = f"https://www.google.com/maps/search/{query}"
    run_parse(link)
    return {"response": f"Scraper ran succesfully {query}"}


@app.get("countries")
def get_countries():
    return
