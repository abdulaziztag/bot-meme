from PIL import Image, ImageDraw, ImageFont
from telethon import TelegramClient, events

api_id = 901989
api_hash = '9a188355878585bb2237201d1a3b7ce5'
client = TelegramClient('anon', api_id, api_hash)


@client.on(events.InlineQuery)
async def handler(event):
    builder = event.builder

    font = ImageFont.truetype("arial.ttf", 48)
    fontSwitcher = ImageFont.truetype("arial.ttf", 40)
    imageon = Image.open('switch.jpg')
    imageoff = Image.open('switchoff.jpg')
    im = Image.new("RGB", (400, 200), "white")
    d = ImageDraw.Draw(im)
    txt = event.text.split(' ')
    deletedTxt = txt.pop()
    d.text((180, 50), ' '.join(txt), fill="black", anchor="ms", font=font)
    d.text((55, 110), 'Off', fill="black", font=fontSwitcher)
    d.text((280, 110), 'On', fill="black", font=fontSwitcher)
    if deletedTxt == 'off':
        im.paste(imageoff, (125, 100))
    elif deletedTxt == 'on':
        im.paste(imageon, (125, 100))

    im.save('rectangle.png')
    if deletedTxt == 'on' or deletedTxt == 'off':
        await event.answer([
            builder.photo('./rectangle.png')
        ])
    else:
        await event.answer([
            builder.photo('./error.jpg')
        ])


client.start()
client.run_until_disconnected()
