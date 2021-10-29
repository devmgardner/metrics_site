import sqlite3 as sq
import json
from django.shortcuts import render
from requests import api
from .utilities import apiscrape

# Create your views here.
def ergo(request) :
    return render(request, 'feed/iportfolio.html', {'combatlevel':ergocombat, 'totalskill':ergototalskill, 'totalxp':ergototalxp, 'rank':ergorank, 'skills':ergoskills})

def alinthar(request) :
    return render(request, 'feed/iportfolio.html', {'combatlevel':alintharcombat, 'totalskill':alinthartotalskill, 'totalxp':alinthartotalxp, 'rank':alintharrank, 'skills':alintharskills})

def ergocombat():
    return apiscrape('Ergo')[0]
def ergototalskill():
    return apiscrape('Ergo')[1]
def ergototalxp():
    return apiscrape('Ergo')[2]
def ergorank():
    return apiscrape('Ergo')[3]
def ergoskills():
    return apiscrape('Ergo')[4]

def alintharcombat():
    return apiscrape('Alinthar')[0]
def alinthartotalskill():
    return apiscrape('Alinthar')[1]
def alinthartotalxp():
    return apiscrape('Alinthar')[2]
def alintharrank():
    return apiscrape('Alinthar')[3]
def alintharskills():
    return apiscrape('Alinthar')[4]