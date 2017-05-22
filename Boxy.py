#!/usr/bin/python3

#All code written by Rishabh Ekbote and Alex Boyle
#With special assistance from Gary, Tyler, Otto, Pat and Nick <3

import discord
import asyncio
import random

import TermCommands
import GifCommands
import ImgRand
import WeatherCommands

botid = '<@!234799836925263874>'
adminid = '224736794644578304'
adminlist = [adminid]

def gifs(message):

    if message.content == '$list' :
        return 'http://bit.do/giflist'

    if message.content == '$gr':
        return GifCommands.gifrandom()

    if message.content == '$help':
        return GifCommands.help()

    if message.content.startswith('$gif '):
        return GifCommands.gifsearch(message.content[5:])


def terms(message):

    global terms
     #reference term by number
    if message.content.startswith('!t '):
        return TermCommands.term(message.content[3:])

    #search through terms
    if message.content.startswith('!ts '):
        return TermCommands.termSearch(message.content[4:])

    #recall 5 most recent terms
    if message.content == '!r' :
        return  TermCommands.recent()

    #link to t&c
    if message.content == '!link' :
        return 'http://bit.do/termcon'

    #pull up list of TermCommands
    if message.content == '!help' :
        return TermCommands.help()

    #Finds and prints all terms referenced in the last !ts or !t command
    if message.content == '!ref':
        return TermCommands.reference()

    #Random term
    if message.content == '!tr':
         return TermCommands.term(str(random.randint(1,len(TermCommands.termlist))))
		 
def weather(message):
    #get current weather
    if message.content == '+help' :
        return WeatherCommands.help()
    
    if message.content.startswith('+wn ') and message.content[4:].strip().isdigit():
	    return WeatherCommands.current_weather_z(message.content[4:])	
    elif message.content.startswith('+wn '):
         return WeatherCommands.current_weather_p(message.content[4:])
 
client = discord.Client()
@client.event 

async def on_message(message):

    #Gif Commands
    if message.content.startswith('$'):
        out = gifs(message)
        if out != None:
            await client.send_message(message.channel,out)

    #Terms and conditions commands
    if message.content.startswith('!'):
        out = terms(message)
        if out != None:
            await client.send_message(message.channel,out)
			
    #Weather commands
    if message.content.startswith('+'):
        out = weather(message)
        if out != None:
            await client.send_message(message.channel,out)

	#Greeting
    if (('hello' in message.content.lower()) or ('hi' in message.content.lower())) and botid in message.content.lower():
        await client.send_message(message.channel,'Hello, <@!%s>!' % (message.author.id))
		
	#Random Image from Imgur
    if ('random image' in message.content.lower() or 'random picture' in message.content.lower()) and ('please' in message.content.lower() or 'pls' in message.content.lower()):
        out = ImgRand.imgrand(ImgRand.options)
        await client.send_message(message.channel,out)

    #Random NSFW Image (From rule34)
    if message.content.lower() == "i am a filthy boy who needs an nsfw image" or message.content.lower() == "i am a filthy girl who needs an nsfw image":
        out = ImgRand.dirtyimage()
        await client.send_message(message.channel,out)

client.run('buymyasianbaby@gmail.com','')
