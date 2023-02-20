from bot.bot_client import BotClient
import os, discord

discord_token = os.environ.get('DISCORD_TOKEN')

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = BotClient(intents=intents)
    client.run(discord_token)

if __name__ == '__main__':
    main()