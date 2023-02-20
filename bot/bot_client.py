import discord

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

        if message.content.startswith('!hello') or message.content.startswith('!ola') or message.content.startswith('!olá'):
            await message.reply(f'Hello {username}!', mention_author=True)