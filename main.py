# APACHE LICENSE
# Copyright 2020 Stuart Paterson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# External Packages
import os
import discord
from dotenv import load_dotenv
from random import randint, choice


# Local Files
import utils

# Create the bot
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

#compliment list
compliment_list = ["You look nice today ", "I see you are dripped out the wazoo ", "Among dripped out today ", "no"]

#cat list 
cat = ["https://tenor.com/view/cat-meow-big-lips-gif-13233291", "https://tenor.com/view/happy-cat-pinch-cute-squishy-gif-4427877", "https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981"]

def get_channel_by_name(client, guild, name):
    """Returns a channel by name from a specific guild"""
    for server in client.guilds:
        if server == guild:
            for channel in server.text_channels:
                if channel.name == name:
                    return channel


@client.event
async def on_ready():
    # Triggered when starting up the bot
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_member_update(before, after):
    if str(before.status) == "offline" and str(after.status) == "online":
        # When a user comes online
        channel = utils.get_channel_by_name(client, after.guild, 'general')
        try:
            # Send your message when a user comes online here!
            pass
        except discord.errors.Forbidden:
            pass


@client.event
async def on_message(message):
    if message.author == client.user:
        # Ignore messages this bot sends
        return

    current_channel = message.channel

    if message.content and len(message.content) > 1 and message.content[0] == '!':
        # First we extract the message after the ! then split it on spaces to
        # get a list or the arguments the user gave
        message_text = message.content[1:]
        split_message = message_text.split(" ")
        command = split_message[0]
        

        if command == "test":
            response = "test successful"
            await current_channel.send(response)
        elif command == "hello":
            response = "Hello "+message.author.mention
            await current_channel.send(response)
        elif command == "compliment":
            response = choice(compliment_list)+message.author.mention
            await current_channel.send(response)
        elif command == "guess":
              try:
                x = split_message[1]
                int(x)
              except:
                response = "Whoops Invalid Command!"
                await current_channel.send(response)
                return
              y = str(randint(1,100))
              if x == y:
                response = "That's a match!"
              elif int(x) > 100:
                response = "give a number between 1 and 100"
              else: 
                response = "Sorry, you guessed "+x+" but I was thinking of "+y
              await current_channel.send(response)
        elif command == "meow":
          response = choice(cat)
          await current_channel.send(response)
              
              
        elif command == "stop":
            await client.logout()
        # elif command == "foo":
        #     # Add your extra commands in blocks like this!
        #     pass





# Run the bot
client.run(TOKEN)