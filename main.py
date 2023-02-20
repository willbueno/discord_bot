from bot.bot_client import BotClient
import discord

def main():
    intents = discord.Intents.default()
    intents.message_content = True
    
    client = BotClient(intents=intents)
    client.run(TOKEN)

if __name__ == '__main__':
    main()