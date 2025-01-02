import discord
import random

# Читаем токен из файла DISCORD_TOKEN.txt
with open("DISCORD_TOKEN.txt", "r") as file:
    DISCORD_TOKEN = file.read().strip()

# Создаём объект Intents
intents = discord.Intents.default()
intents.messages = True  # Если нужно отслеживать сообщения
intents.guilds = True    # Если нужен доступ к серверам

# Создаем клиента с намерениями
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Вошли как {client.user}")

@client.event
async def on_message(message):
    # Не реагируем на сообщения от самого бота
    if message.author == client.user:
        return

    # Список фраз для проверки
    trigger_phrases = [
        # Английские приветствия
        "GM", "gm", "Good morning", "good morning", 
        "GN", "gn", "Good night", "good night", 
        "Hello!", "hello!", "Hi", "hi", "Hey", "hey", 
        "Sup", "sup", "What’s up", "what’s up", 
        "Yo", "yo", "Howdy", "howdy", "Wassup", "wassup", 
        "Greetings", "greetings", "Salutations", "salutations", 
        "Hey there", "hey there", "What’s going on", "what’s going on",
        "hello", "Hello",

        # Русские приветствия
        "Привет", "привет", "Здарова", "здарова", "Здравствуй", "здравствуй", 
        "Здравствуйте", "здравствуйте", "Прив", "прив", 
        "Хай", "хай", "Хелло", "хелло", 
        "Йо", "йо", "Чё как", "чё как", "Как дела", "как дела", 
        "Салют", "салют", "Всем привет", "всем привет", 
        "Здорова", "здорово", "Приветик", "приветик", "Приветище", "приветище",

        # Разговорные и сленговые фразы (смешанные и на разных языках)
        "Yo yo", "yo yo", "What’s up, bro?", "what’s up, bro?", 
        "Sup, dude", "sup, dude", "Yo, man", "yo, man", 
        "Heyo", "heyo", "What’s good", "what’s good", 
        "Whassup", "whassup", "Aloha", "aloha", 
        "Hola", "hola", "Ciao", "ciao", "Bonjour", "bonjour", 
        "Yoo", "yoo", "Hiya", "hiya", "Good day", "good day", 
        "What’s cracking", "what’s cracking", "Sup homie", "sup homie", 
        "Yo fam", "yo fam", "Wazzup", "wazzup"
    ]

    # Список ответов для вариативности
    responses = [
        "# ONLY OHIO!",
        "# OHIO. Only ohio.",
        "# OHIO IS THE BEST.",
        "# OHIO. Nothing else.",
        "# Ohio, only Ohio.",
        "# Just OHIO.",
        "# OHIO, my friend.",
        "# OHIO, forever and always!",
        "# No way but OHIO."
    ]

    # Проверка, если сообщение содержит одну из фраз из списка
    if any(phrase in message.content for phrase in trigger_phrases):
        # Выбор случайного ответа
        response = random.choice(responses)
        # Ответ на сообщение в формате reply
        await message.reply(response)  # Ответ в виде Reply на исходное сообщение

client.run(DISCORD_TOKEN)
