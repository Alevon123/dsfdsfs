from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model and labels
model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

def get_image(path):
    
        # Load and preprocess the image
    image = Image.open(path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.expand_dims(normalized_image_array, axis=0)

        # Predict using the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]
    return class_name, confidence_score
    




@bot.command()
async def check(ctx):
    attachments = ctx.message.attachments
    if not attachments:
        await ctx.send("В сообщении нет  изображений.")
        return
    
    for attachment in attachments:
        if attachment.content_type.startswith('image'):
            await attachment.save(f'images/{attachment.filename}')
            await ctx.send(f'Изображение "{attachment.filename}" сохранено!')
        else:
            await ctx.send(f'Файл "{attachment.filename}" не является изображением.')

bot.run("MTE1Mjk2MDkxMzc3MTYwMjAwMQ.Gvsrv4.SOxGnnRJmf0IPJ0kSwoZ9qRi6YRhZXC37mgH-k")






