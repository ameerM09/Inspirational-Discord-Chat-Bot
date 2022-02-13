import discord
import os
import random
import requests
import json
from keep_online import online

client = discord.Client()
encourage_key = [
    'sad', 'stressed', 'worried', 'unhappy', 'depressed', 'angry',
    'depressing', 'sadness', 'worrying', 'SAD', 'STRESSED', 'WORRIED',
    'UNHAPPY', 'DEPRESSED', 'ANGRY', 'DEPRESSING', 'SADNESS',
    'WORRYING', 'SAD', 'STRESSED', 'Sad', 'Stressed', 'Worried', 'Unhappy',
    'Depressed', 'Angry', 'Depressing', 'Sadness', 'Worrying'
]

encourage_statements = [
    "When you're happy you enjoy the music, but when you're sad you understand the lyrics. -Frank Ocean",
    "It's in the darkest moments that we find our greatest strengths. -Steven Aitchison",
    "The best way to cheer yourself is to try to cheer someone else up. -Mark Twain",
    "Every pain gives a lesson, and every lesson changes a person for the better. -Anonymous",
    "Never put your happiness in another's hands. -Anonymous",
    "To lose patience is to lose the battle. -Mahatma Ghandi",
    "It's fine to celebrate success, but it is more important to heed the lessons of failure. -Bill Gates",
    "Failure is an option here. If things are not failing, you are not innovating enough. -Elon Musk",
    "It is impossible to live without failing at something, unless you live so cautiously that you might as well not have lived at all in which case you fail by default. -Joanne Rowling",
    "Tears come from the heart and not the brain. -Anonymous",
    "Don't give up because of one bad chapter in your life. Keep going. Your story doesn't end here. -Anonymous",
    "It hurts to leave a light on for nobody. -Graham Foust",
    "You keep a lot to yourself because it's difficult to find people who understand. -Anonymous",
    "What brings us to tears, will lead to grace. Our pain is never wasted. -Bob Goff",
    "Don't desire happiness because it creates only unhappiness and nothing else. -Anonymous",
    "Sometimes life is going to hit you in the head with a brick. Don't lose faith. -Steve Jobs",
    "If you don't love it, you're going to fail. -Steve Jobs",
    "Always wake up with a smile, knowing that today you are going to have fun accomplishing what others are too afraid to do. -Mark Cuban",
    "It doesn't matter how many times you fail. You only have to be right once and then everyone can tell you that you are an overnight success. -Mark Cuban",
    "It always seems impossible until it is done. -Nelson Mandela",
    "Anyone who has never made a mistake has never tried anything new. -Albert Einstein",
    "The future belongs to those who prepare for it today. -Malcolm X"
]


@client.event
async def on_ready():
    print('We have connected and logged in as {0.user}'.format(client))


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$spire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello! How are you doing?')

    if any(word in message.content for word in encourage_key):
        await message.channel.send(random.choice(encourage_statements))

online()

KEY = os.environ['TOKEN']
client.run(KEY)
