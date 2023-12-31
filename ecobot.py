import discord
import random
import os
import requests
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def mem(ctx):
    images = os.listdir('images')
    img_name = random.choice(images)

    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)

@bot.command()
async def advice(ctx):
    ad = ['Посадить дерево.', 'Построить скворечник, синичник.', 'Повесить и своевременно наполнять кормушку, поилку для птиц.', 'Ездить волонтером на проекты по спасению, восстановлению, учету животных.'
               , 'Поддерживать фонды помощи животным.', 'Реже пользоваться кондиционером.', 'Убавлять индивидуальное отопление.', 'Покупать энергосберегающие приборы.', 'Выбрать электротранспорт.'
               , 'Больше ездить на велосипеде и ходить пешком.', ' Сортировать мусор.', 'Раздавать и продавать ненужные вещи, уменьшая количество мусора.', 'Не повреждать и не рвать без нужды растения, не ломать ветки.'
               ]
    advicee = random.choice(ad)

    await ctx.send(advicee)

@bot.command()
async def ecolink(ctx):
    ad = ['https://www.nationalgeographic.com/', 'https://www.iucnredlist.org/', 'https://ru.wikipedia.org/wiki/%D0%AD%D0%BA%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F']
    links = random.choice(ad)

    await ctx.send(links)

@bot.command()
async def helpp(ctx):
    await ctx.send('''Этот Бот предназначен чтобы помочь Миру с проблемой мирового загрязнения экологии, тут вы можете встретить следующие команды:
    mem - Мемы связанные с экологией
    advice - Советы как помочь с экологией
    ecolink - Полезные сайты
    animal - То что мы стараемся защитить''')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_fox_image_url():    
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)
    data = res.json()
    return data['image']

#block of random animals
@bot.command()
async def animal(ctx):
    animals = ['duck', 'dog', 'fox']
    random_animal = random.choice(animals)

    if random_animal == 'duck':
        image_url = get_duck_image_url()
    elif random_animal == 'dog':
        image_url = get_dog_image_url()
    elif random_animal == 'fox':
        image_url = get_fox_image_url()

    await ctx.send(image_url)

bot.run("token")