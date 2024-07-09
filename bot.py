import pyrogram 
from pyrogram import Client, filters 
from pyrogram.types import Message 




api_id = 26597515 
api_hash = "ea74a2439c1f8fff561d8d86af6f1540"
bot_token = "6997698261:AAEiJJIQ_fy8PlQdUIdQLpw7V4h1rX4byBM"



app = Client(
     "ask_test",
     api_id=api_id,
     api_hash=api_hash,
     bot_token=bot_token
     )



@app.on_message(filters.command(["start"]))
async def start(client, message):
   await message.reply("selam,ben text deneme botuyum.")

 

@app.on_message(filters.command("kole") & filters.group) 
async def kole(client, message):

    if message.from_user.id == 6905940236:
         await message.reply_text("**Sayın sahibim!şu an sorunsuz çalışıyorum.**")

    elif message.from_user.id == 7142242630:
          await message.reply_text("**tırrek sassy çalışıyorum çok yorma vjkxvsl.**")
                     
    elif message.from_user.id == 7131686379:
          await message.reply_text("** titrek karı delisin ama ben kadar değil,yorma pls.**")

    elif message.from_user.id == 7182074621:
          await message.reply_text("**sado sen konuşma dfhkslflzjcx**")

    elif message.from_user.id == 6604549799:
          await message.reply_text("**dayı beni öldürdüler dayı,kurtar beni bunların elinden**")

    elif message.from_user.id == 2040437974:
          await message.reply_text("**göttü can kardaşım, sen iste tüm botları çalıştırayım.**")

    elif message.from_user.id == 6716279900:
          await message.reply_text("**maymuş sen iste tüm maymunları köle yapayım sana.**") 

    elif message.from_user.id == 6423044130:
          await message.reply_text("**sahibimin canı canı**")

    else:
       await message.reply_text("**seni tanımıyorum sen de kimsin.**")

# yeni bir kullanıcı gruba katıldığında çalışacak
@app.on_message(filters.new_chat_members)  # yeni bir kullanıcı gruba katıldığında bu fonksiyon tetiklenecek
def welcome(client, message):  # hoş geldin mesajı fonksiyonunu tanımlıyoruz
    for member in message.new_chat_members:  # yeni katılan her kullanıcı için döngü başlatıyoruz
        if member.id == OWNER_ID:  # eğer katılan kullanıcı bot sahibiyse
            message.reply(f"Hoş geldiniz, {member.mention}! Botun sahibinin gruba katılması büyük bir onur.")  # özel bir hoşgeldin mesajı gönderiyoruz
        else:  # Eğer katılan kullanıcı bot sahibi değilse
            message.reply(f"Hoş geldiniz, {member.mention}! Grubumuza katıldığınız için mutluyuz.")  # genel hoş geldin mesajı gönderiyoruz

app.run()
