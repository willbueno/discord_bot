import discord, random

from api.google_drive import drive_service
from datetime import datetime

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
    
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        # Get data about the user
        username_code = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if not channel.startswith('m0v1'):
            return

        username = username_code.split('#')[0]

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # Just for fun
        if message.content.startswith('!gc') or message.content.startswith('!rank'):
            if username == 'willzera':
                await message.reply(f'Your GC level is 20!', mention_author=True)
                return
            if username == 'danshimo':
                await message.reply(f'Your GC level is 20!', mention_author=True)
                return
            if username == 'Nkc.Yuji':
                await message.reply(f'Your GC level is 18!', mention_author=True)
                return
            if username == 'CrazyLog':
                await message.reply(f'Your GC level is 2!', mention_author=True)
                return
            await message.reply(f'Your GC level is {random.randint(0, 20)}!', mention_author=True)

        if message.content.startswith('!hello') or message.content.startswith('!ola') or message.content.startswith('!olá'):
            await message.reply(f'Hello {username}!', mention_author=True)

        if message.content.startswith('!help'):
            await message.reply(f'No help!', mention_author=False)

        if message.content.startswith('!link'):
            await message.reply('Here is the link:\nhttps://mylink.com/')

        if message.content.startswith('!files'):
            files = drive_service.get_data()

            if not files:
                await message.reply('Sorry! I didn\'t find any files!', mention_author=False)
                return

            response = f'Hey {username}! Here is the list of files:\n'
            
            for file in files:
                name = file.get('name')
                modifiedTimeStr = file.get('modifiedTime')
                modifiedTime = datetime.strptime(modifiedTimeStr, '%Y-%m-%dT%H:%M:%S.%fZ')
                modifiedTimeFormat = modifiedTime.strftime('%d/%m/%Y')
                fileDescription = f'{name} ({modifiedTimeFormat})'
                print(f'File: {fileDescription}')
                response = response + '- ' + fileDescription + '\n'
            
            await message.reply(response, mention_author=False)