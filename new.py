from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import os
import asyncio

# ✅ Correct way (Railway will use this)
TOKEN = os.getenv("TOKEN")

# Your file_ids
VIDEO_ID = "BAACAgUAAxkBAAMQab2bVb3RxPKah3buIQKUB58ZVIoAAvkgAAIlWelVtockIScpKCE6BA"
AUDIO_ID = "CQACAgUAAxkBAAMOab2bMiXjPpCe-hiYVpUak5mupQcAAvcgAAIlWelV7a_xGZ-GJ6o6BA"
APK_ID = "BQACAgUAAxkBAAMSab2bdTsbxv_EpBWsgp1SNXRCR3cAAvogAAIlWelVKhDy5tOnOWU6BA"

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = user.id
    name = user.first_name

    # ✅ Approve request
    await update.chat_join_request.approve()

    try:
        # 👋 Welcome message
        await context.bot.send_message(
            chat_id=chat_id,
            text=f"""Hello dear {name} 👋

Tumhari Join Request mil gayi hai ✅  
Jaldi approve ho jayegi.

APK, Video aur Voice Guide niche diya hai 👇"""
        )

        await asyncio.sleep(1)

        # 🎥 Video
        await context.bot.send_video(
            chat_id=chat_id,
            video=VIDEO_ID,
            caption="""👍 Full video watch karo 💥💥

🔗 Link:
https://bdggame5.com//#/register?invitationCode=2176818821310"""
        )

        await asyncio.sleep(1)

        # 📦 APK
        await context.bot.send_document(
            chat_id=chat_id,
            document=APK_ID,
            caption="""👍 Full video watch karo 💥💥

Bro jaldi se hack INSTALL karo  
abhi only SURESHOT aa rha h  
is se pahle hack work na kare  
profit bna lo 🚀"""
        )

        await asyncio.sleep(1)

        # 🎧 Audio
        await context.bot.send_audio(
            chat_id=chat_id,
            audio=AUDIO_ID,
            caption="🎧 PURA VOICE SUNO OR KARO 💯"
        )

    except Exception as e:
        print("Error (user may not have started bot):", e)


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join_request))

app.run_polling()
