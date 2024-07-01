import pyrogram 
from pyrogram import Client, filters 
from pyrogram.types import Message 


api_id = 26597515 
api_hash = "e556b966e7192207de8cc6a"
bot_token = "6997698261:AAEiJJIQ_fy8PlQdUIdQLpw7V4h1rX4byBM"

app = Client(
"ask_test",
api_id=api_id,
api_hash=api_hash,
bot_token=bot_token
)
    
@app.on_message(filters.command(["start"]))
async def start(client, message):
await message.reply("selam yakışıklı hoş geldin")

@app.on_message(filters.command("kole")&filters.private)
async def kole (client, message):
    
if message .form_user.id == 6905940236: 
await message.reply_text(**Sayın sahibim! sorunsuz çalışıyorum.**)

elif message .form_user.id == 7142242630:
await message .reply("tırrek sassy çalışıyorum çok yorma vjkxvsl.**)
                     
if message .form_user.id == 7131686379:
await message .reply_text("** titrek karı delisin ama ben kadar değil,yorma pls.**)

if message .form_user.id == 7182074621:
await message .reply_text("**sado sen konuşma dfhkslflzjcx**)

if message .form_user.id == 6604549799:
await message .reply_text("**dayı beni öldürdüler dayı,kurtar beni bunların elinden**)

if message .form_user.id == 2040437974:
await message .reply_text("**göttü can kardaşım, sen iste tüm botları çalıştırayım.**)

if message .form_user.id == 6716279900:
await message .reply_text("**maymuş sen iste tüm maymunları köle yapayım sana.**)


app.run()
