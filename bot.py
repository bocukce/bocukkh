import pyrogram
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import random



api_id = 26597515 
api_hash = "e556b966e7192209f7f419b07de8cc6a"
bot_token = "6997698261:AAEiJJIQ_fy8PlQdUIdQLpw7V4h1rX4byBM"



app = Client(
     "ask_test",
     api_id=api_id,
     api_hash=api_hash,
     bot_token=bot_token
     )

 
OWNER_ID = 6905940236


# /start komutunu özel mesajlarda dinleyen bir handler tanımlıyoruz.
@app.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
      # butonları içeren bir klavye oluşturuyoruz.
      keyboard = InlineKeyboardMarkup(
           inline_keyboard=[
                [
                   # ilk buton destek chatine yönlendiriyor.
                   InlineKeyboardButton(text="Destek 🛠", url=f"https://t.me/yikilmayanchat"),
                   # gruba ekle butonu
                   InlineKeyboardButton(text="Gruba Ekle 👥", url=f"https://t.me/{app.me.username}?startgroup=true")
                ],
                [
                   # ikinci buton sahibin profiline yönlendiriyor.
                   InlineKeyboardButton(text="Owner 🐞", user_id=OWNER_ID)
                ]
           ]
      ) 
      # kullanıcıya yanıt olarak bir mesaj gönderiyoruz ve klavyeyi ekliyoruz.
      await message.reply("Merhaba, ben test deneme butonuyum. Aşağıdaki butonlardan birini seçebilirsiniz:",
                          reply_markup=keyboard)  






# slapmessages örnekleri 
slapmessages =[
    "{}, {}'in yüzüne tükürdü.😄",
    "{}, {}'i tekmeledi.🙊",
    "{}, {}'yı tekme tokat dövdü.😱",
    "{}, {}'e tokat attı.🤠",
    "{}, {}'i tekmeledi.🤡",
    "{}, {}'in telefonunu suya fırlattı.💀",
    "{}, {}'in üstüne kahve döktü.👾",
]
@app.on_message(filters.command(["sille"]) & filters.group)
async def sille(client, message):
    # komutun bir yanıt olup olmadığını kontrol ediyoruz.
    if not message.reply_to_message:
         await message.reply("bu mesajı kullanmak için bir mesajı yanıtlamalısınız.")
         return
         
    # yanıtlayan kişinin (gönderici) ve yanıtlanan kişinin (bilgilerini alıyoruz)
    sender = message.from_user
    target = message.reply_to_message.from_user

    # eğer yanıtlanan kişi OWNER_ID ise özel bir mesaj gönderiyoruz.
    if target.id == OWNER_ID:
        await message.reply("Beni tokatlayamazsın!")
        return
         
    # yanıtlayan ve yanıtlanan kişilerin mentionlarını alıyoruz
    sender_mention = sender.mention
    target_mention = target.mention

    # rastgele bir slap mesajı seçiyoruz ve isimlerle dolduruyoruz
    slap_message = random.choice(slapmessages).format(sender_mention, target_mention)

    # yanıtlanan mesaja gönderilecek metni oluşturuyoruz
    await message.reply_to_message.reply(slap_message)
    



@app.on_message(filters.command("kole") & filters.group) 
async def kole(client, message):
     
    if message.from_user.id == 6905940236:
         await message.reply_text("**Sayın sahibim!şu an sorunsuz çalışıyorum.**")

    elif message.from_user.id == 7142242630:
          await message.reply_text("**tırrek sassy çalışıyorum tabiki.**")
                     
    elif message.from_user.id == 7131686379:
          await message.reply_text("** titrek karı delisin ama ben kadar değil,yorma pls.**")

    elif message.from_user.id == 7182074621:
          await message.reply_text("**sedo kardaşım sen konuşma, sen kimdir dfhkslflzjcx**")

    elif message.from_user.id == 6604549799:
          await message.reply_text("**dayı beni öldürdüler dayı,kurtar beni bunların elinden**")

    elif message.from_user.id == 2040437974:
          await message.reply_text("**göttü can kardaşım, sen iste bütün botları çalıştırayım.**")

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
            message.reply(f"Hoş geldiniz, {member.mention}! Botun sahibinin gruba katılması büyük bir onur.")  # özel bir hoş geldin mesajı gönderiyoruz
        else:  # Eğer katılan kullanıcı bot sahibi değilse
            message.reply(f"Hoş geldiniz, {member.mention}! Grubumuza katıldığınız için mutluyuz.")  # genel hoş geldin mesajı gönderiyoruz

# bir kullanıcı gruptan ayrıldığında çalışacak fonksiyon
@app.on_message(filters.left_chat_member) 
def goodbye(client, message):
     member = message.left_chat_member
     if member.id == OWNER_ID:
          message.reply(f"maalesef, {member.mention} gruptan ayrıldı. Umarız tekrar gelirsin.! ")
     else:
          message.reply(f"hoşça kal, {member.mention} Seni özleyeceğiz. ")

# /para komutunu dinleyen handler 
@app.on_message(filters.command(["para"]) & filters.group)
async def para(client, message):
   # random olarak "yazı" veya "tura" seçimi yapma
     result = random.choice(["Yazı✋", "Tura🌑"])
     await message.reply(f"**{result}**")

# komutları ve emojileri tanımlayalım
commands = {
    "zar": "🎲",
    "dart": "🎯",
    "basket": "🏀",
    "futbol": "⚽️",
    "bowling": "🎳",
    "slot": "🎰",
}
# Her bir komut için fonksiyon tanımlayın
@app.on_message(filters.command(list(commands.keys())))
async def send_dice(client, message):
     command = message.command[0][1:] # komutu alır (başındaki '/' işaretini atarak)
     emoji = commands.get(command)
     if emoji:
         dice_message = await message.reply_dice(emoji=emoji)
          
         # zarın sonucunu beklemek için kısa bir süre uyuyalım
         await asyncio.sleep(3) # 3 saniye beklemek için

         # zarın sonucunu içeren mesajı güncelleyelim
         await message.reply(f"Zar durdu! Gelen sayı: {dice_message.dice.value}")

# Doğruluk ve cesaretlik soruları
dogruluk_soruları = [
     En son ne zaman yalan söyledin?
     En son ne zaman ağladın ve ne için?
     En büyük korkun ne?
     Annenin senin hakkında bilmediğine sevindiğin şey nedir?
     Hiç birini aldattın mı?
     Şimdiye kadar yaptığın en kötü şey ne?
     Hiç kimseye söylemediğin bir sır nedir?
     Gizli bir yeteneğin var mı?
     En son ne zaman yalan söyledin?
     en büyük korkun ne?
     Annenin senin hakkında bilmediğine sevindiğin şey nedir?
     Hiç birini aldattın mı?
     Şimdiye kadar yaptığın en kötü şey ne?
     Hiç kimseye söylemediğin bir sır nedir?
     Gizli bir yeteneğin var mı?
     Ünlü insanlardan aşık olduğun biri oldu mu?
     Şimdiye kadar yaşadığınız en kötü deneyim neydi?
     Hiç bir sınavda kopya çektin mi?
     Şimdiye kadar hiç sarhoş oldun mu?
     Hiç kanunu çiğnedin mi?
     Şimdiye kadar yaptığın en utanç verici şey nedir?
     En büyük güvensizliğin nedir?
     Şimdiye kadar yaptığın en büyük hata nedir?
     Şimdiye kadar yaptığın en iğrenç şey nedir?
     Birinin sana yaptığı en kötü şey neydi?
     Hiç karakola düşecek bir şey yaptın mı?
     En kötü alışkanlığın nedir?
     Şimdiye kadar birine söylediğin en kötü şey nedir?
     Gördüğün en garip rüya neydi?
     Hiç yapmaman gereken bir şeyi yaparken yakalandın mı?
     Hayatta yaşadığın en kötü buluşma nasıl oldu?
     En büyük pişmanlığın nedir?
     İnsanların senin hakkında düşündüklerinin aksine kötü olan gerçek yönün nedir?
     Kötü bir randevudan çıkmak için hiç yalan söyledin mi?
     İçinde bulunduğun en büyük sorun neydi?
     Hiç arkadaşının sırrını başkasıyla paylaştın mı?
     Benim mesajımı hiç görmezden geldin mi. Neden bunu yaptın?
     Hiç en iyi arkadaşına yalan söyledin mi?
     En iyi 2 arkadaşın arasında seçim yapsan hangisini seçerdin?
     En iyi arkadaşının en sevmediğin huyu nedir?
     Sevdiğin ama açılamadığın kişi sana en yakın arkadaşını sevdiğini söylese ne yapardın?
     Arkadaşının sevgilisini aldattığını bilseydin ne yapardın?
     Kendini daha iyi biri gibi göstermek için en iyi arkadaşın hakkında yalan söyledin mi?
     Kim daha güzel/yakışıklı? Sen mi (odadaki herhangi biri)……. mı?
     Gruptaki herhangi biri hakkındaki ilk izleniminiz neydi?
     Odadaki herkese 1’den 10’a kadar puan verin, 10’u en sıcak olanı; 1 ise en kötü ve soğuk olanı.
     Bir diş fırçasını en iyi arkadaşınla paylaşır mısın?
     Arkadaşın onun için yalan söylemeni istedi ve başının derde gireceğini biliyor olsaydın yine de söyler miydin?
     Okuldaki en popüler kız/erkek sen olsaydın arkadaşlarından vazgeçer misin?
     Biri size en iyi arkadaşınızın nasıl olduğunu sorduğunda, onu nasıl anlatırdın?
     Bir tatil kazansan ve iki kişi getirmenize izin verilse aramızdan kimleri seçerdin?
     Saklamanız söylendiği bir sırrı hiç anlattınız mı?
     Sevgilin ve en iyi dostun göle düşse önce hangisini kurtarırsın?
     Bu gruptaki insanlardan, kiminle çıkardın?
     Bu odada en iyi gülüşe kim sahip?
     Bu odada en şirin burun kimde?
     Bu odada en güzel gözler kimde?
     Bu odadaki en komik kim?
     Bir kız/erkek ile buluşmaya gittiğinde aynada kendini ne sıklıkta kontrol ediyorsun?
     Bu odada en güzel dans eden kim?
     Bu odadaki birinin bir fiziksel özelliğine sahip olsaydınız, bu ne olurdu?
     Yaşamak için bir haftan vardı ve bu odada biriyle evlenmek zorunda olsaydın, kim olurdu?
     Yaşamak için sadece 24 saatiniz olsa ve bu odadaki herhangi biriyle herhangi bir şey yapabilseydiniz, kim olurdu ve o kişiyle ne yapardınız?
     Dünyadaki son kişi ben olsam benimle çıkar mıydın?
     Yaptığın en çapkın şey nedir?

app.run()
