# bot.py
import os
import discord
from dotenv import load_dotenv
import operator
import re
import math
from heapq import nlargest

from SummonerAPI import SummonerAPI as Summoner
from LeagueAPI import LeagueAPI as League
from ChampMasteryAPI import ChampMasteryAPI as ChampMastery
from MatchAPI import MatchAPI as Match
from ClashAPI import ClashAPI as Clash

import LoLConsts as Consts

SummonerAPI = Summoner(Consts.KEY['api_key'])               # SummonerAPI Test
LeagueAPI = League(Consts.KEY['api_key'])                   # LeagueAPI Test
ChampMasteryAPI = ChampMastery(Consts.KEY['api_key'])       # MasteryAPI Test
MatchAPI = Match(Consts.KEY['api_key'])                     # MatchAPI Test
ClashAPI = Clash(Consts.KEY['api_key'])                     # ClashAPI Test

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

# @client.event
# async def on_member_join(member):
#     await member.create_dm()
#     await member.dm_channel.send(
#         f'Hi {member.name}, welcome to my Discord server!'
#     )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

<<<<<<< HEAD
    # rather than putting all of the vital lines of code in each if statement
    # we can just put them all in the on_message method
    # and then put all the specific code inside of the future if statements

    # the summoner name isn't always going to be in the same index
    # but the summoner name will always be after the second white space
    # we have to find the second white space in message
    # that will be the start of summoner
    if message.content.startswith('-lol'):
        
        # help menu
        # if message.content == '-lol help':
        type(message)

        command = message.content[message.content.find(' ')+1:]
        summoner_name = command[command.find(' ')+1:]                             # get the summoner name
        summoner = SummonerAPI.get_summoner_by_name(summoner_name)       # access the SummonerAPI based off of summoner_name

        summoner_id = summoner['id']
        account_id = summoner['accountId']

        league = LeagueAPI.rank_of_summoner(summoner_id)
        matchlist = MatchAPI.get_matchlist(account_id)

        matchlist_ranked = MatchAPI.get_matchlist_ranked(account_id, 420, 13)
        gameId_dict = {}                                                                # this will store the matchId and the champion that was player
        champ_occurrences = {}

        # find the rank of the summoner
        if message.content.startswith('-lol rank '):
            # test if it works
            count = 0
            for i in league:
                if i['queueType'] == 'RANKED_SOLO_5x5':
                    await message.channel.send(str(summoner['name']) + " is " + league[count]['tier']+ " " +league[count]['rank'])
            

        # find the 5 most played champs
        if message.content.startswith('-lol champs '):
            for games in matchlist_ranked['matches']:
                gameId_dict[games['gameId']] = games['champion']
                if games['champion'] in champ_occurrences:
                    champ_occurrences[games['champion']] += 1
                else:
                    champ_occurrences[games['champion']] = 1
            
            three_highest = nlargest(3, champ_occurrences, key = champ_occurrences.get)
            await message.channel.send("**Most Played Champion in Ranked**")
            for val in three_highest:
                await message.channel.send('   - **' + re.sub(r"(\w)([A-Z])", r"\1 \2", ChampMasteryAPI.get_champion(str(val))) + "** : " + str(champ_occurrences.get(val)) + " games")
            
            # await message.channel.send("this is the total amount of games " + str(matchlist_ranked['totalGames']))
=======
    league_status = 'you are silver 3'
    if message.content == '-lol':
        await message.channel.send(league_status)
>>>>>>> 2f3c450d2a8de8e8ba1ede9b37729e84d8f00d0b

            

client.run(TOKEN)






