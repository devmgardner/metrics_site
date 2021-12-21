import sqlite3 as sq
import json
from django.shortcuts import render
from requests import api
from .utilities import apiscrape, dbscrape, quests

# Create your views here.
def ergo(request) :
    return render(request, 'feed/iportfolio.html', {'combatlevel':ergocombat, 'totalskill':ergototalskill, 'totalxp':ergototalxp, 'rank':ergorank, 'skills':ergoskilllevels, 'xp':ergoskillxp, 'questscomplete':ergoquestscomplete, 'questspercent':ergoquestspercent, 'name':'Ergo', 'activities':ergoact, 'allquests':ergoquests, 'xpc':ergoskillxpc, 'xpp':ergoskillxpp, 'xpp1':ergoskillxpp1, 'xpp2':ergoskillxpp2})

def alinthar(request) :
    return render(request, 'feed/iportfolio.html', {'combatlevel':alintharcombat, 'totalskill':alinthartotalskill, 'totalxp':alinthartotalxp, 'rank':alintharrank, 'skills':alintharskilllevels, 'xp':alintharskillxp, 'questscomplete':alintharquestscomplete, 'questspercent':alintharquestspercent, 'name':'Alinthar', 'activities':alintharact, 'allquests':alintharquests, 'xpc':alintharskillxpc, 'xpp':alintharskillxpp, 'xpp1':alintharskillxpp1, 'xpp2':alintharskillxpp2})

def dasn1u(request) :
    return render(request, 'feed/iportfolio.html', {'combatlevel':dasn1ucombat, 'totalskill':dasn1utotalskill, 'totalxp':dasn1utotalxp, 'rank':dasn1urank, 'skills':dasn1uskilllevels, 'xp':dasn1uskillxp, 'questscomplete':dasn1uquestscomplete, 'questspercent':dasn1uquestspercent, 'name':'dasn1u', 'activities':dasn1uact, 'allquests':dasn1uquests, 'xpc':dasn1uskillxpc, 'xpp':dasn1uskillxpp, 'xpp1':dasn1uskillxpp1, 'xpp2':dasn1uskillxpp2})

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
    ergoallskills = json.loads(apiscrape('Ergo')[4])
    ergoleveldict = {}
    for skill in ergoallskills:
        if skill['id'] == 0:
            ergoleveldict['Attack'] = skill['level']
        elif skill['id'] == 1:
            ergoleveldict['Defence'] = skill['level']
        elif skill['id'] == 2:
            ergoleveldict['Strength'] = skill['level']
        elif skill['id'] == 3:
            ergoleveldict['Constitution'] = skill['level']
        elif skill['id'] == 4:
            ergoleveldict['Ranged'] = skill['level']
        elif skill['id'] == 5:
            ergoleveldict['Prayer'] = skill['level']
        elif skill['id'] == 6:
            ergoleveldict['Magic'] = skill['level']
        elif skill['id'] == 7:
            ergoleveldict['Cooking'] = skill['level']
        elif skill['id'] == 8:
            ergoleveldict['Woodcutting'] = skill['level']
        elif skill['id'] == 9:
            ergoleveldict['Fletching'] = skill['level']
        elif skill['id'] == 10:
            ergoleveldict['Fishing'] = skill['level']
        elif skill['id'] == 11:
            ergoleveldict['Firemaking'] = skill['level']
        elif skill['id'] == 12:
            ergoleveldict['Crafting'] = skill['level']
        elif skill['id'] == 13:
            ergoleveldict['Smithing'] = skill['level']
        elif skill['id'] == 14:
            ergoleveldict['Mining'] = skill['level']
        elif skill['id'] == 15:
            ergoleveldict['Herblore'] = skill['level']
        elif skill['id'] == 16:
            ergoleveldict['Agility'] = skill['level']
        elif skill['id'] == 17:
            ergoleveldict['Thieving'] = skill['level']
        elif skill['id'] == 18:
            ergoleveldict['Slayer'] = skill['level']
        elif skill['id'] == 19:
            ergoleveldict['Farming'] = skill['level']
        elif skill['id'] == 20:
            ergoleveldict['Runecrafting'] = skill['level']
        elif skill['id'] == 21:
            ergoleveldict['Hunter'] = skill['level']
        elif skill['id'] == 22:
            ergoleveldict['Construction'] = skill['level']
        elif skill['id'] == 23:
            ergoleveldict['Summoning'] = skill['level']
        elif skill['id'] == 24:
            ergoleveldict['Dungeoneering'] = skill['level']
        elif skill['id'] == 25:
            ergoleveldict['Divination'] = skill['level']
        elif skill['id'] == 26:
            ergoleveldict['Invention'] = skill['level']
        elif skill['id'] == 27:
            ergoleveldict['Archaeology'] = skill['level']
    return ergoleveldict
def ergoskillxp():
    ergoallskills = json.loads(apiscrape('Ergo')[4])
    ergoxpdict = {}
    for skill in ergoallskills:
        skill['xp'] /= 10
        if skill['id'] == 0:
            ergoxpdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            ergoxpdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            ergoxpdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            ergoxpdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            ergoxpdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            ergoxpdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            ergoxpdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            ergoxpdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            ergoxpdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            ergoxpdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            ergoxpdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            ergoxpdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            ergoxpdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            ergoxpdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            ergoxpdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            ergoxpdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            ergoxpdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            ergoxpdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            ergoxpdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            ergoxpdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            ergoxpdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            ergoxpdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            ergoxpdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            ergoxpdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            ergoxpdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            ergoxpdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            ergoxpdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            ergoxpdict['Archaeology'] = skill['xp']
    return ergoxpdict
def ergoskillxpp():
    ergoallskills = json.loads(apiscrape('Ergo')[4])
    ergoxppdict = {}
    for skill in ergoallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            ergoxppdict['Attack'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 1:
            ergoxppdict['Defence'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 2:
            ergoxppdict['Strength'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 3:
            ergoxppdict['Constitution'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 4:
            ergoxppdict['Ranged'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 5:
            ergoxppdict['Prayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 6:
            ergoxppdict['Magic'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 7:
            ergoxppdict['Cooking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 8:
            ergoxppdict['Woodcutting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 9:
            ergoxppdict['Fletching'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 10:
            ergoxppdict['Fishing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 11:
            ergoxppdict['Firemaking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 12:
            ergoxppdict['Crafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 13:
            ergoxppdict['Smithing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 14:
            ergoxppdict['Mining'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 15:
            ergoxppdict['Herblore'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 16:
            ergoxppdict['Agility'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 17:
            ergoxppdict['Thieving'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 18:
            ergoxppdict['Slayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 19:
            ergoxppdict['Farming'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 20:
            ergoxppdict['Runecrafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 21:
            ergoxppdict['Hunter'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 22:
            ergoxppdict['Construction'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 23:
            ergoxppdict['Summoning'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 24:
            ergoxppdict['Dungeoneering'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 25:
            ergoxppdict['Divination'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 26:
            ergoxppdict['Invention'] = round(skill['xp']/36073511, 2)
        elif skill['id'] == 27:
            ergoxppdict['Archaeology'] = round(skill['xp']/13034431, 2)
    return ergoxppdict
def ergoskillxpp1():
    ergoallskills = json.loads(apiscrape('Ergo')[4])
    ergoxpp1dict = {}
    for skill in ergoallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            ergoxpp1dict['Attack'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 1:
            ergoxpp1dict['Defence'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 2:
            ergoxpp1dict['Strength'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 3:
            ergoxpp1dict['Constitution'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 4:
            ergoxpp1dict['Ranged'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 5:
            ergoxpp1dict['Prayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 6:
            ergoxpp1dict['Magic'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 7:
            ergoxpp1dict['Cooking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 8:
            ergoxpp1dict['Woodcutting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 9:
            ergoxpp1dict['Fletching'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 10:
            ergoxpp1dict['Fishing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 11:
            ergoxpp1dict['Firemaking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 12:
            ergoxpp1dict['Crafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 13:
            ergoxpp1dict['Smithing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 14:
            ergoxpp1dict['Mining'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 15:
            ergoxpp1dict['Herblore'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 16:
            ergoxpp1dict['Agility'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 17:
            ergoxpp1dict['Thieving'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 18:
            ergoxpp1dict['Slayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 19:
            ergoxpp1dict['Farming'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 20:
            ergoxpp1dict['Runecrafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 21:
            ergoxpp1dict['Hunter'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 22:
            ergoxpp1dict['Construction'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 23:
            ergoxpp1dict['Summoning'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 24:
            ergoxpp1dict['Dungeoneering'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 25:
            ergoxpp1dict['Divination'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 26:
            ergoxpp1dict['Invention'] = round(skill['xp']/80618654, 2)
        elif skill['id'] == 27:
            ergoxpp1dict['Archaeology'] = round(skill['xp']/104273167, 2)
    return ergoxpp1dict
def ergoskillxpp2():
    ergoallskills = json.loads(apiscrape('Ergo')[4])
    ergoxpp2dict = {}
    for skill in ergoallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            ergoxpp2dict['Attack'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 1:
            ergoxpp2dict['Defence'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 2:
            ergoxpp2dict['Strength'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 3:
            ergoxpp2dict['Constitution'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 4:
            ergoxpp2dict['Ranged'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 5:
            ergoxpp2dict['Prayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 6:
            ergoxpp2dict['Magic'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 7:
            ergoxpp2dict['Cooking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 8:
            ergoxpp2dict['Woodcutting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 9:
            ergoxpp2dict['Fletching'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 10:
            ergoxpp2dict['Fishing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 11:
            ergoxpp2dict['Firemaking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 12:
            ergoxpp2dict['Crafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 13:
            ergoxpp2dict['Smithing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 14:
            ergoxpp2dict['Mining'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 15:
            ergoxpp2dict['Herblore'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 16:
            ergoxpp2dict['Agility'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 17:
            ergoxpp2dict['Thieving'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 18:
            ergoxpp2dict['Slayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 19:
            ergoxpp2dict['Farming'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 20:
            ergoxpp2dict['Runecrafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 21:
            ergoxpp2dict['Hunter'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 22:
            ergoxpp2dict['Construction'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 23:
            ergoxpp2dict['Summoning'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 24:
            ergoxpp2dict['Dungeoneering'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 25:
            ergoxpp2dict['Divination'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 26:
            ergoxpp2dict['Invention'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 27:
            ergoxpp2dict['Archaeology'] = round(skill['xp']/200000000, 2)
    return ergoxpp2dict
def ergoskillxpc():
    ergoallskills = json.loads(apiscrape('Ergo')[4])
    ergoxpcdict = {}
    for skill in ergoallskills:
        skill['xp'] = "{:,}".format(skill['xp']/10)
        if skill['id'] == 0:
            ergoxpcdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            ergoxpcdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            ergoxpcdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            ergoxpcdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            ergoxpcdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            ergoxpcdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            ergoxpcdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            ergoxpcdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            ergoxpcdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            ergoxpcdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            ergoxpcdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            ergoxpcdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            ergoxpcdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            ergoxpcdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            ergoxpcdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            ergoxpcdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            ergoxpcdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            ergoxpcdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            ergoxpcdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            ergoxpcdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            ergoxpcdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            ergoxpcdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            ergoxpcdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            ergoxpcdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            ergoxpcdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            ergoxpcdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            ergoxpcdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            ergoxpcdict['Archaeology'] = skill['xp']
    return ergoxpcdict
def ergoact():
    return dbscrape('Ergo')
def ergoquests():
    return quests('Ergo')

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
    alintharallskills = json.loads(apiscrape('Alinthar')[4])
    alintharleveldict = {}
    for skill in alintharallskills:
        if skill['id'] == 0:
            alintharleveldict['Attack'] = skill['level']
        elif skill['id'] == 1:
            alintharleveldict['Defence'] = skill['level']
        elif skill['id'] == 2:
            alintharleveldict['Strength'] = skill['level']
        elif skill['id'] == 3:
            alintharleveldict['Constitution'] = skill['level']
        elif skill['id'] == 4:
            alintharleveldict['Ranged'] = skill['level']
        elif skill['id'] == 5:
            alintharleveldict['Prayer'] = skill['level']
        elif skill['id'] == 6:
            alintharleveldict['Magic'] = skill['level']
        elif skill['id'] == 7:
            alintharleveldict['Cooking'] = skill['level']
        elif skill['id'] == 8:
            alintharleveldict['Woodcutting'] = skill['level']
        elif skill['id'] == 9:
            alintharleveldict['Fletching'] = skill['level']
        elif skill['id'] == 10:
            alintharleveldict['Fishing'] = skill['level']
        elif skill['id'] == 11:
            alintharleveldict['Firemaking'] = skill['level']
        elif skill['id'] == 12:
            alintharleveldict['Crafting'] = skill['level']
        elif skill['id'] == 13:
            alintharleveldict['Smithing'] = skill['level']
        elif skill['id'] == 14:
            alintharleveldict['Mining'] = skill['level']
        elif skill['id'] == 15:
            alintharleveldict['Herblore'] = skill['level']
        elif skill['id'] == 16:
            alintharleveldict['Agility'] = skill['level']
        elif skill['id'] == 17:
            alintharleveldict['Thieving'] = skill['level']
        elif skill['id'] == 18:
            alintharleveldict['Slayer'] = skill['level']
        elif skill['id'] == 19:
            alintharleveldict['Farming'] = skill['level']
        elif skill['id'] == 20:
            alintharleveldict['Runecrafting'] = skill['level']
        elif skill['id'] == 21:
            alintharleveldict['Hunter'] = skill['level']
        elif skill['id'] == 22:
            alintharleveldict['Construction'] = skill['level']
        elif skill['id'] == 23:
            alintharleveldict['Summoning'] = skill['level']
        elif skill['id'] == 24:
            alintharleveldict['Dungeoneering'] = skill['level']
        elif skill['id'] == 25:
            alintharleveldict['Divination'] = skill['level']
        elif skill['id'] == 26:
            alintharleveldict['Invention'] = skill['level']
        elif skill['id'] == 27:
            alintharleveldict['Archaeology'] = skill['level']
    return alintharleveldict
def alintharskillxp():
    alintharallskills = json.loads(apiscrape('Alinthar')[4])
    alintharxpdict = {}
    for skill in alintharallskills:
        skill['xp'] /= 10
        if skill['id'] == 0:
            alintharxpdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            alintharxpdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            alintharxpdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            alintharxpdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            alintharxpdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            alintharxpdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            alintharxpdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            alintharxpdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            alintharxpdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            alintharxpdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            alintharxpdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            alintharxpdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            alintharxpdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            alintharxpdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            alintharxpdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            alintharxpdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            alintharxpdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            alintharxpdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            alintharxpdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            alintharxpdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            alintharxpdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            alintharxpdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            alintharxpdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            alintharxpdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            alintharxpdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            alintharxpdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            alintharxpdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            alintharxpdict['Archaeology'] = skill['xp']
    return alintharxpdict
def alintharskillxpp():
    alintharallskills = json.loads(apiscrape('Alinthar')[4])
    alintharxppdict = {}
    for skill in alintharallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            alintharxppdict['Attack'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 1:
            alintharxppdict['Defence'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 2:
            alintharxppdict['Strength'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 3:
            alintharxppdict['Constitution'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 4:
            alintharxppdict['Ranged'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 5:
            alintharxppdict['Prayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 6:
            alintharxppdict['Magic'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 7:
            alintharxppdict['Cooking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 8:
            alintharxppdict['Woodcutting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 9:
            alintharxppdict['Fletching'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 10:
            alintharxppdict['Fishing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 11:
            alintharxppdict['Firemaking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 12:
            alintharxppdict['Crafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 13:
            alintharxppdict['Smithing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 14:
            alintharxppdict['Mining'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 15:
            alintharxppdict['Herblore'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 16:
            alintharxppdict['Agility'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 17:
            alintharxppdict['Thieving'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 18:
            alintharxppdict['Slayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 19:
            alintharxppdict['Farming'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 20:
            alintharxppdict['Runecrafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 21:
            alintharxppdict['Hunter'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 22:
            alintharxppdict['Construction'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 23:
            alintharxppdict['Summoning'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 24:
            alintharxppdict['Dungeoneering'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 25:
            alintharxppdict['Divination'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 26:
            alintharxppdict['Invention'] = round(skill['xp']/36073511, 2)
        elif skill['id'] == 27:
            alintharxppdict['Archaeology'] = round(skill['xp']/13034431, 2)
    return alintharxppdict
def alintharskillxpp1():
    alintharallskills = json.loads(apiscrape('Alinthar')[4])
    alintharxpp1dict = {}
    for skill in alintharallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            alintharxpp1dict['Attack'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 1:
            alintharxpp1dict['Defence'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 2:
            alintharxpp1dict['Strength'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 3:
            alintharxpp1dict['Constitution'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 4:
            alintharxpp1dict['Ranged'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 5:
            alintharxpp1dict['Prayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 6:
            alintharxpp1dict['Magic'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 7:
            alintharxpp1dict['Cooking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 8:
            alintharxpp1dict['Woodcutting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 9:
            alintharxpp1dict['Fletching'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 10:
            alintharxpp1dict['Fishing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 11:
            alintharxpp1dict['Firemaking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 12:
            alintharxpp1dict['Crafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 13:
            alintharxpp1dict['Smithing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 14:
            alintharxpp1dict['Mining'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 15:
            alintharxpp1dict['Herblore'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 16:
            alintharxpp1dict['Agility'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 17:
            alintharxpp1dict['Thieving'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 18:
            alintharxpp1dict['Slayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 19:
            alintharxpp1dict['Farming'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 20:
            alintharxpp1dict['Runecrafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 21:
            alintharxpp1dict['Hunter'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 22:
            alintharxpp1dict['Construction'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 23:
            alintharxpp1dict['Summoning'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 24:
            alintharxpp1dict['Dungeoneering'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 25:
            alintharxpp1dict['Divination'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 26:
            alintharxpp1dict['Invention'] = round(skill['xp']/80618654, 2)
        elif skill['id'] == 27:
            alintharxpp1dict['Archaeology'] = round(skill['xp']/104273167, 2)
    return alintharxpp1dict
def alintharskillxpp2():
    alintharallskills = json.loads(apiscrape('Alinthar')[4])
    alintharxpp2dict = {}
    for skill in alintharallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            alintharxpp2dict['Attack'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 1:
            alintharxpp2dict['Defence'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 2:
            alintharxpp2dict['Strength'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 3:
            alintharxpp2dict['Constitution'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 4:
            alintharxpp2dict['Ranged'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 5:
            alintharxpp2dict['Prayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 6:
            alintharxpp2dict['Magic'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 7:
            alintharxpp2dict['Cooking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 8:
            alintharxpp2dict['Woodcutting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 9:
            alintharxpp2dict['Fletching'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 10:
            alintharxpp2dict['Fishing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 11:
            alintharxpp2dict['Firemaking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 12:
            alintharxpp2dict['Crafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 13:
            alintharxpp2dict['Smithing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 14:
            alintharxpp2dict['Mining'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 15:
            alintharxpp2dict['Herblore'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 16:
            alintharxpp2dict['Agility'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 17:
            alintharxpp2dict['Thieving'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 18:
            alintharxpp2dict['Slayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 19:
            alintharxpp2dict['Farming'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 20:
            alintharxpp2dict['Runecrafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 21:
            alintharxpp2dict['Hunter'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 22:
            alintharxpp2dict['Construction'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 23:
            alintharxpp2dict['Summoning'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 24:
            alintharxpp2dict['Dungeoneering'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 25:
            alintharxpp2dict['Divination'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 26:
            alintharxpp2dict['Invention'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 27:
            alintharxpp2dict['Archaeology'] = round(skill['xp']/200000000, 2)
    return alintharxpp2dict
def alintharskillxpc():
    alintharallskills = json.loads(apiscrape('Alinthar')[4])
    alintharxpcdict = {}
    for skill in alintharallskills:
        skill['xp'] = "{:,}".format(skill['xp']/10)
        if skill['id'] == 0:
            alintharxpcdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            alintharxpcdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            alintharxpcdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            alintharxpcdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            alintharxpcdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            alintharxpcdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            alintharxpcdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            alintharxpcdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            alintharxpcdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            alintharxpcdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            alintharxpcdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            alintharxpcdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            alintharxpcdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            alintharxpcdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            alintharxpcdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            alintharxpcdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            alintharxpcdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            alintharxpcdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            alintharxpcdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            alintharxpcdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            alintharxpcdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            alintharxpcdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            alintharxpcdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            alintharxpcdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            alintharxpcdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            alintharxpcdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            alintharxpcdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            alintharxpcdict['Archaeology'] = skill['xp']
    return alintharxpcdict
def alintharact():
    return dbscrape('Alinthar')
def alintharquests():
    return quests('Alinthar')


def dasn1ucombat():
    return apiscrape('dasn1u')[0]
def dasn1utotalskill():
    return apiscrape('dasn1u')[1]
def dasn1utotalxp():
    return apiscrape('dasn1u')[2]
def dasn1urank():
    return apiscrape('dasn1u')[3]
def dasn1uskills():
    return apiscrape('dasn1u')[4]
def dasn1uquestspercent():
    completedpercentage = round(apiscrape('dasn1u')[5] / 307 * 100, 2)
    return completedpercentage
def dasn1uquestscomplete():
    return apiscrape('dasn1u')[5]
def dasn1uskilllevels():
    dasn1uallskills = json.loads(apiscrape('dasn1u')[4])
    dasn1uleveldict = {}
    for skill in dasn1uallskills:
        if skill['id'] == 0:
            dasn1uleveldict['Attack'] = skill['level']
        elif skill['id'] == 1:
            dasn1uleveldict['Defence'] = skill['level']
        elif skill['id'] == 2:
            dasn1uleveldict['Strength'] = skill['level']
        elif skill['id'] == 3:
            dasn1uleveldict['Constitution'] = skill['level']
        elif skill['id'] == 4:
            dasn1uleveldict['Ranged'] = skill['level']
        elif skill['id'] == 5:
            dasn1uleveldict['Prayer'] = skill['level']
        elif skill['id'] == 6:
            dasn1uleveldict['Magic'] = skill['level']
        elif skill['id'] == 7:
            dasn1uleveldict['Cooking'] = skill['level']
        elif skill['id'] == 8:
            dasn1uleveldict['Woodcutting'] = skill['level']
        elif skill['id'] == 9:
            dasn1uleveldict['Fletching'] = skill['level']
        elif skill['id'] == 10:
            dasn1uleveldict['Fishing'] = skill['level']
        elif skill['id'] == 11:
            dasn1uleveldict['Firemaking'] = skill['level']
        elif skill['id'] == 12:
            dasn1uleveldict['Crafting'] = skill['level']
        elif skill['id'] == 13:
            dasn1uleveldict['Smithing'] = skill['level']
        elif skill['id'] == 14:
            dasn1uleveldict['Mining'] = skill['level']
        elif skill['id'] == 15:
            dasn1uleveldict['Herblore'] = skill['level']
        elif skill['id'] == 16:
            dasn1uleveldict['Agility'] = skill['level']
        elif skill['id'] == 17:
            dasn1uleveldict['Thieving'] = skill['level']
        elif skill['id'] == 18:
            dasn1uleveldict['Slayer'] = skill['level']
        elif skill['id'] == 19:
            dasn1uleveldict['Farming'] = skill['level']
        elif skill['id'] == 20:
            dasn1uleveldict['Runecrafting'] = skill['level']
        elif skill['id'] == 21:
            dasn1uleveldict['Hunter'] = skill['level']
        elif skill['id'] == 22:
            dasn1uleveldict['Construction'] = skill['level']
        elif skill['id'] == 23:
            dasn1uleveldict['Summoning'] = skill['level']
        elif skill['id'] == 24:
            dasn1uleveldict['Dungeoneering'] = skill['level']
        elif skill['id'] == 25:
            dasn1uleveldict['Divination'] = skill['level']
        elif skill['id'] == 26:
            dasn1uleveldict['Invention'] = skill['level']
        elif skill['id'] == 27:
            dasn1uleveldict['Archaeology'] = skill['level']
    return dasn1uleveldict
def dasn1uskillxp():
    dasn1uallskills = json.loads(apiscrape('dasn1u')[4])
    dasn1uxpdict = {}
    for skill in dasn1uallskills:
        skill['xp'] /= 10
        if skill['id'] == 0:
            dasn1uxpdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            dasn1uxpdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            dasn1uxpdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            dasn1uxpdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            dasn1uxpdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            dasn1uxpdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            dasn1uxpdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            dasn1uxpdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            dasn1uxpdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            dasn1uxpdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            dasn1uxpdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            dasn1uxpdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            dasn1uxpdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            dasn1uxpdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            dasn1uxpdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            dasn1uxpdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            dasn1uxpdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            dasn1uxpdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            dasn1uxpdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            dasn1uxpdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            dasn1uxpdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            dasn1uxpdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            dasn1uxpdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            dasn1uxpdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            dasn1uxpdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            dasn1uxpdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            dasn1uxpdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            dasn1uxpdict['Archaeology'] = skill['xp']
    return dasn1uxpdict
def dasn1uskillxpp():
    dasn1uallskills = json.loads(apiscrape('dasn1u')[4])
    dasn1uxppdict = {}
    for skill in dasn1uallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            dasn1uxppdict['Attack'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 1:
            dasn1uxppdict['Defence'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 2:
            dasn1uxppdict['Strength'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 3:
            dasn1uxppdict['Constitution'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 4:
            dasn1uxppdict['Ranged'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 5:
            dasn1uxppdict['Prayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 6:
            dasn1uxppdict['Magic'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 7:
            dasn1uxppdict['Cooking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 8:
            dasn1uxppdict['Woodcutting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 9:
            dasn1uxppdict['Fletching'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 10:
            dasn1uxppdict['Fishing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 11:
            dasn1uxppdict['Firemaking'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 12:
            dasn1uxppdict['Crafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 13:
            dasn1uxppdict['Smithing'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 14:
            dasn1uxppdict['Mining'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 15:
            dasn1uxppdict['Herblore'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 16:
            dasn1uxppdict['Agility'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 17:
            dasn1uxppdict['Thieving'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 18:
            dasn1uxppdict['Slayer'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 19:
            dasn1uxppdict['Farming'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 20:
            dasn1uxppdict['Runecrafting'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 21:
            dasn1uxppdict['Hunter'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 22:
            dasn1uxppdict['Construction'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 23:
            dasn1uxppdict['Summoning'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 24:
            dasn1uxppdict['Dungeoneering'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 25:
            dasn1uxppdict['Divination'] = round(skill['xp']/13034431, 2)
        elif skill['id'] == 26:
            dasn1uxppdict['Invention'] = round(skill['xp']/36073511, 2)
        elif skill['id'] == 27:
            dasn1uxppdict['Archaeology'] = round(skill['xp']/13034431, 2)
    return dasn1uxppdict
def dasn1uskillxpp1():
    dasn1uallskills = json.loads(apiscrape('dasn1u')[4])
    dasn1uxpp1dict = {}
    for skill in dasn1uallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            dasn1uxpp1dict['Attack'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 1:
            dasn1uxpp1dict['Defence'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 2:
            dasn1uxpp1dict['Strength'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 3:
            dasn1uxpp1dict['Constitution'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 4:
            dasn1uxpp1dict['Ranged'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 5:
            dasn1uxpp1dict['Prayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 6:
            dasn1uxpp1dict['Magic'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 7:
            dasn1uxpp1dict['Cooking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 8:
            dasn1uxpp1dict['Woodcutting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 9:
            dasn1uxpp1dict['Fletching'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 10:
            dasn1uxpp1dict['Fishing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 11:
            dasn1uxpp1dict['Firemaking'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 12:
            dasn1uxpp1dict['Crafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 13:
            dasn1uxpp1dict['Smithing'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 14:
            dasn1uxpp1dict['Mining'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 15:
            dasn1uxpp1dict['Herblore'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 16:
            dasn1uxpp1dict['Agility'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 17:
            dasn1uxpp1dict['Thieving'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 18:
            dasn1uxpp1dict['Slayer'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 19:
            dasn1uxpp1dict['Farming'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 20:
            dasn1uxpp1dict['Runecrafting'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 21:
            dasn1uxpp1dict['Hunter'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 22:
            dasn1uxpp1dict['Construction'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 23:
            dasn1uxpp1dict['Summoning'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 24:
            dasn1uxpp1dict['Dungeoneering'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 25:
            dasn1uxpp1dict['Divination'] = round(skill['xp']/104273167, 2)
        elif skill['id'] == 26:
            dasn1uxpp1dict['Invention'] = round(skill['xp']/80618654, 2)
        elif skill['id'] == 27:
            dasn1uxpp1dict['Archaeology'] = round(skill['xp']/104273167, 2)
    return dasn1uxpp1dict
def dasn1uskillxpp2():
    dasn1uallskills = json.loads(apiscrape('dasn1u')[4])
    dasn1uxpp2dict = {}
    for skill in dasn1uallskills:
        skill['xp'] *= 10
        if skill['id'] == 0:
            dasn1uxpp2dict['Attack'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 1:
            dasn1uxpp2dict['Defence'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 2:
            dasn1uxpp2dict['Strength'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 3:
            dasn1uxpp2dict['Constitution'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 4:
            dasn1uxpp2dict['Ranged'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 5:
            dasn1uxpp2dict['Prayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 6:
            dasn1uxpp2dict['Magic'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 7:
            dasn1uxpp2dict['Cooking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 8:
            dasn1uxpp2dict['Woodcutting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 9:
            dasn1uxpp2dict['Fletching'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 10:
            dasn1uxpp2dict['Fishing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 11:
            dasn1uxpp2dict['Firemaking'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 12:
            dasn1uxpp2dict['Crafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 13:
            dasn1uxpp2dict['Smithing'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 14:
            dasn1uxpp2dict['Mining'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 15:
            dasn1uxpp2dict['Herblore'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 16:
            dasn1uxpp2dict['Agility'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 17:
            dasn1uxpp2dict['Thieving'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 18:
            dasn1uxpp2dict['Slayer'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 19:
            dasn1uxpp2dict['Farming'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 20:
            dasn1uxpp2dict['Runecrafting'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 21:
            dasn1uxpp2dict['Hunter'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 22:
            dasn1uxpp2dict['Construction'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 23:
            dasn1uxpp2dict['Summoning'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 24:
            dasn1uxpp2dict['Dungeoneering'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 25:
            dasn1uxpp2dict['Divination'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 26:
            dasn1uxpp2dict['Invention'] = round(skill['xp']/200000000, 2)
        elif skill['id'] == 27:
            dasn1uxpp2dict['Archaeology'] = round(skill['xp']/200000000, 2)
    return dasn1uxpp2dict
def dasn1uskillxpc():
    dasn1uallskills = json.loads(apiscrape('dasn1u')[4])
    dasn1uxpcdict = {}
    for skill in dasn1uallskills:
        skill['xp'] = "{:,}".format(skill['xp']/10)
        if skill['id'] == 0:
            dasn1uxpcdict['Attack'] = skill['xp']
        elif skill['id'] == 1:
            dasn1uxpcdict['Defence'] = skill['xp']
        elif skill['id'] == 2:
            dasn1uxpcdict['Strength'] = skill['xp']
        elif skill['id'] == 3:
            dasn1uxpcdict['Constitution'] = skill['xp']
        elif skill['id'] == 4:
            dasn1uxpcdict['Ranged'] = skill['xp']
        elif skill['id'] == 5:
            dasn1uxpcdict['Prayer'] = skill['xp']
        elif skill['id'] == 6:
            dasn1uxpcdict['Magic'] = skill['xp']
        elif skill['id'] == 7:
            dasn1uxpcdict['Cooking'] = skill['xp']
        elif skill['id'] == 8:
            dasn1uxpcdict['Woodcutting'] = skill['xp']
        elif skill['id'] == 9:
            dasn1uxpcdict['Fletching'] = skill['xp']
        elif skill['id'] == 10:
            dasn1uxpcdict['Fishing'] = skill['xp']
        elif skill['id'] == 11:
            dasn1uxpcdict['Firemaking'] = skill['xp']
        elif skill['id'] == 12:
            dasn1uxpcdict['Crafting'] = skill['xp']
        elif skill['id'] == 13:
            dasn1uxpcdict['Smithing'] = skill['xp']
        elif skill['id'] == 14:
            dasn1uxpcdict['Mining'] = skill['xp']
        elif skill['id'] == 15:
            dasn1uxpcdict['Herblore'] = skill['xp']
        elif skill['id'] == 16:
            dasn1uxpcdict['Agility'] = skill['xp']
        elif skill['id'] == 17:
            dasn1uxpcdict['Thieving'] = skill['xp']
        elif skill['id'] == 18:
            dasn1uxpcdict['Slayer'] = skill['xp']
        elif skill['id'] == 19:
            dasn1uxpcdict['Farming'] = skill['xp']
        elif skill['id'] == 20:
            dasn1uxpcdict['Runecrafting'] = skill['xp']
        elif skill['id'] == 21:
            dasn1uxpcdict['Hunter'] = skill['xp']
        elif skill['id'] == 22:
            dasn1uxpcdict['Construction'] = skill['xp']
        elif skill['id'] == 23:
            dasn1uxpcdict['Summoning'] = skill['xp']
        elif skill['id'] == 24:
            dasn1uxpcdict['Dungeoneering'] = skill['xp']
        elif skill['id'] == 25:
            dasn1uxpcdict['Divination'] = skill['xp']
        elif skill['id'] == 26:
            dasn1uxpcdict['Invention'] = skill['xp']
        elif skill['id'] == 27:
            dasn1uxpcdict['Archaeology'] = skill['xp']
    return dasn1uxpcdict
def dasn1uact():
    return dbscrape('dasn1u')
def dasn1uquests():
    return quests('dasn1u')