import sqlite3 as sq
import json
from django.shortcuts import render
from requests import api
from .utilities import apiscrape

ergoallskills = apiscrape('Ergo')[4]
ergoleveldict = {}
ergoxpdict = {}
for skill in ergoallskills:
    if skill['id'] == 0:
        ergoleveldict['Attack'] = skill['level']
        ergoxpdict['Attack'] = skill['xp']
    elif skill['id'] == 1:
        ergoleveldict['Defence'] = skill['level']
        ergoxpdict['Defence'] = skill['xp']
    elif skill['id'] == 2:
        ergoleveldict['Strength'] = skill['level']
        ergoxpdict['Strength'] = skill['xp']
    elif skill['id'] == 3:
        ergoleveldict['Constitution'] = skill['level']
        ergoxpdict['Constitution'] = skill['xp']
    elif skill['id'] == 4:
        ergoleveldict['Ranged'] = skill['level']
        ergoxpdict['Ranged'] = skill['xp']
    elif skill['id'] == 5:
        ergoleveldict['Prayer'] = skill['level']
        ergoxpdict['Prayer'] = skill['xp']
    elif skill['id'] == 6:
        ergoleveldict['Magic'] = skill['level']
        ergoxpdict['Magic'] = skill['xp']
    elif skill['id'] == 7:
        ergoleveldict['Cooking'] = skill['level']
        ergoxpdict['Cooking'] = skill['xp']
    elif skill['id'] == 8:
        ergoleveldict['Woodcutting'] = skill['level']
        ergoxpdict['Woodcutting'] = skill['xp']
    elif skill['id'] == 9:
        ergoleveldict['Fletching'] = skill['level']
        ergoxpdict['Fletching'] = skill['xp']
    elif skill['id'] == 10:
        ergoleveldict['Fishing'] = skill['level']
        ergoxpdict['Fishing'] = skill['xp']
    elif skill['id'] == 11:
        ergoleveldict['Firemaking'] = skill['level']
        ergoxpdict['Firemaking'] = skill['xp']
    elif skill['id'] == 12:
        ergoleveldict['Crafting'] = skill['level']
        ergoxpdict['Crafting'] = skill['xp']
    elif skill['id'] == 13:
        ergoleveldict['Smithing'] = skill['level']
        ergoxpdict['Smithing'] = skill['xp']
    elif skill['id'] == 14:
        ergoleveldict['Mining'] = skill['level']
        ergoxpdict['Mining'] = skill['xp']
    elif skill['id'] == 15:
        ergoleveldict['Herblore'] = skill['level']
        ergoxpdict['Herblore'] = skill['xp']
    elif skill['id'] == 16:
        ergoleveldict['Agility'] = skill['level']
        ergoxpdict['Agility'] = skill['xp']
    elif skill['id'] == 17:
        ergoleveldict['Thieving'] = skill['level']
        ergoxpdict['Thieving'] = skill['xp']
    elif skill['id'] == 18:
        ergoleveldict['Slayer'] = skill['level']
        ergoxpdict['Slayer'] = skill['xp']
    elif skill['id'] == 19:
        ergoleveldict['Farming'] = skill['level']
        ergoxpdict['Farming'] = skill['xp']
    elif skill['id'] == 20:
        ergoleveldict['Runecrafting'] = skill['level']
        ergoxpdict['Runecrafting'] = skill['xp']
    elif skill['id'] == 21:
        ergoleveldict['Hunter'] = skill['level']
        ergoxpdict['Hunter'] = skill['xp']
    elif skill['id'] == 22:
        ergoleveldict['Construction'] = skill['level']
        ergoxpdict['Construction'] = skill['xp']
    elif skill['id'] == 23:
        ergoleveldict['Summoning'] = skill['level']
        ergoxpdict['Summoning'] = skill['xp']
    elif skill['id'] == 24:
        ergoleveldict['Dungeoneering'] = skill['level']
        ergoxpdict['Dungeoneering'] = skill['xp']
    elif skill['id'] == 25:
        ergoleveldict['Divination'] = skill['level']
        ergoxpdict['Divination'] = skill['xp']
    elif skill['id'] == 26:
        ergoleveldict['Invention'] = skill['level']
        ergoxpdict['Invention'] = skill['xp']
    elif skill['id'] == 27:
        ergoleveldict['Archaeology'] = skill['level']
        ergoxpdict['Archaeology'] = skill['xp']
alintharallskills = apiscrape('Alinthar')[4]
alintharleveldict = {}
alintharxpdict = {}
for skill in alintharallskills:
    if skill['id'] == 0:
        alintharleveldict['Attack'] = skill['level']
        alintharxpdict['Attack'] = skill['xp']
    elif skill['id'] == 1:
        alintharleveldict['Defence'] = skill['level']
        alintharxpdict['Defence'] = skill['xp']
    elif skill['id'] == 2:
        alintharleveldict['Strength'] = skill['level']
        alintharxpdict['Strength'] = skill['xp']
    elif skill['id'] == 3:
        alintharleveldict['Constitution'] = skill['level']
        alintharxpdict['Constitution'] = skill['xp']
    elif skill['id'] == 4:
        alintharleveldict['Ranged'] = skill['level']
        alintharxpdict['Ranged'] = skill['xp']
    elif skill['id'] == 5:
        alintharleveldict['Prayer'] = skill['level']
        alintharxpdict['Prayer'] = skill['xp']
    elif skill['id'] == 6:
        alintharleveldict['Magic'] = skill['level']
        alintharxpdict['Magic'] = skill['xp']
    elif skill['id'] == 7:
        alintharleveldict['Cooking'] = skill['level']
        alintharxpdict['Cooking'] = skill['xp']
    elif skill['id'] == 8:
        alintharleveldict['Woodcutting'] = skill['level']
        alintharxpdict['Woodcutting'] = skill['xp']
    elif skill['id'] == 9:
        alintharleveldict['Fletching'] = skill['level']
        alintharxpdict['Fletching'] = skill['xp']
    elif skill['id'] == 10:
        alintharleveldict['Fishing'] = skill['level']
        alintharxpdict['Fishing'] = skill['xp']
    elif skill['id'] == 11:
        alintharleveldict['Firemaking'] = skill['level']
        alintharxpdict['Firemaking'] = skill['xp']
    elif skill['id'] == 12:
        alintharleveldict['Crafting'] = skill['level']
        alintharxpdict['Crafting'] = skill['xp']
    elif skill['id'] == 13:
        alintharleveldict['Smithing'] = skill['level']
        alintharxpdict['Smithing'] = skill['xp']
    elif skill['id'] == 14:
        alintharleveldict['Mining'] = skill['level']
        alintharxpdict['Mining'] = skill['xp']
    elif skill['id'] == 15:
        alintharleveldict['Herblore'] = skill['level']
        alintharxpdict['Herblore'] = skill['xp']
    elif skill['id'] == 16:
        alintharleveldict['Agility'] = skill['level']
        alintharxpdict['Agility'] = skill['xp']
    elif skill['id'] == 17:
        alintharleveldict['Thieving'] = skill['level']
        alintharxpdict['Thieving'] = skill['xp']
    elif skill['id'] == 18:
        alintharleveldict['Slayer'] = skill['level']
        alintharxpdict['Slayer'] = skill['xp']
    elif skill['id'] == 19:
        alintharleveldict['Farming'] = skill['level']
        alintharxpdict['Farming'] = skill['xp']
    elif skill['id'] == 20:
        alintharleveldict['Runecrafting'] = skill['level']
        alintharxpdict['Runecrafting'] = skill['xp']
    elif skill['id'] == 21:
        alintharleveldict['Hunter'] = skill['level']
        alintharxpdict['Hunter'] = skill['xp']
    elif skill['id'] == 22:
        alintharleveldict['Construction'] = skill['level']
        alintharxpdict['Construction'] = skill['xp']
    elif skill['id'] == 23:
        alintharleveldict['Summoning'] = skill['level']
        alintharxpdict['Summoning'] = skill['xp']
    elif skill['id'] == 24:
        alintharleveldict['Dungeoneering'] = skill['level']
        alintharxpdict['Dungeoneering'] = skill['xp']
    elif skill['id'] == 25:
        alintharleveldict['Divination'] = skill['level']
        alintharxpdict['Divination'] = skill['xp']
    elif skill['id'] == 26:
        alintharleveldict['Invention'] = skill['level']
        alintharxpdict['Invention'] = skill['xp']
    elif skill['id'] == 27:
        alintharleveldict['Archaeology'] = skill['level']
        alintharxpdict['Archaeology'] = skill['xp']

# Create your views here.
def ergo(request) :
    return render(request, 'feed/iportfolio.html', {'combatlevel':ergocombat, 'totalskill':ergototalskill, 'totalxp':ergototalxp, 'rank':ergorank, 'skills':ergoskilllevels, 'xp':ergoskillxp, 'questscomplete':ergoquestscomplete, 'questspercent':ergoquestspercent})

def alinthar(request) :
    return render(request, 'feed/iportfolio.html', {'combatlevel':alintharcombat, 'totalskill':alinthartotalskill, 'totalxp':alinthartotalxp, 'rank':alintharrank, 'skills':alintharskilllevels, 'xp':alintharskillxp, 'questscomplete':alintharquestscomplete, 'questspercent':alintharquestspercent})

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
def ergoquestspercent():
    completedpercentage = round(apiscrape('Ergo')[5] / 307 * 100, 2)
    return completedpercentage
def ergoquestscomplete():
    return apiscrape('Ergo')[5]
def ergoskilllevels():
    return ergoleveldict
def ergoskillxp():
    return ergoxpdict

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
def alintharquestspercent():
    completedpercentage = round(apiscrape('Alinthar')[5] / 307 * 100, 2)
    return completedpercentage
def alintharquestscomplete():
    return apiscrape('Alinthar')[5]
def alintharskilllevels():
    return alintharleveldict
def alintharskillxp():
    return alintharxpdict