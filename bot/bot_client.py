import discord, random

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