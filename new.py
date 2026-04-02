from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ChatJoinRequestHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TOKEN = "8784449458:AAHlJ7YtRSAJsxn3BAPaBSpiclqPfmgUi7A"

# Your file_ids
VIDEO_ID = "BAACAgUAAxkBAAICdmnLi_cuDu0tpmomDvfRmXL1ITwnAALtIwAC00BZVjy0fbBP8pGqOgQ"
AUDIO_ID = "CQACAgUAAxkBAAICeGnLjBVtwOnB4iGRtLCcwgLzleXdAALzHAACXGvxVQU1r_kweS2UOgQ"
APK_ID = "BQACAgUAAxkBAAIQG2nONyNderCxULVuwMjkonxzWTdPAAIPHAACc9RxVmUWabjHcHoXOgQ"

# 🔴 MULTIPLE ADMINS
ADMIN_IDS = {1442856537}  # replace with your IDs


# ✅ ADMIN FILE ID GENERATOR
async def get_file_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Only admins allowed
    if user_id not in ADMIN_IDS:
        return

    msg = update.message

    if msg.video:
        await msg.reply_text(f"VIDEO_ID:\n{msg.video.file_id}")
    elif msg.audio:
        await msg.reply_text(f"AUDIO_ID:\n{msg.audio.file_id}")
    elif msg.document:
        await msg.reply_text(f"DOCUMENT_ID:\n{msg.document.file_id}")


# ================= YOUR ORIGINAL CODE =================

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = user.id  # DM the user

    name = user.first_name

    # Approve request (optional)
    await update.chat_join_request.approve()

    # Send message
    await context.bot.send_message(chat_id=chat_id, text=f'''Hello dear {name}👋
Tumhari Join Request mil gayi hai ✅
Jaldi approve ho jayegi.

APK, Video aur Voice Guide niche diya hai 👇''')

    # Send files
    await context.bot.send_video(chat_id=chat_id, video=VIDEO_ID , caption='''👍 Full video watch karo 💥💥

🔗Link:
https://www.jaiclub01.com/#/register?invitationCode=24884129118''')

    await context.bot.send_document(chat_id=chat_id, document=APK_ID, caption='''👍 Full video watch karo 💥💥

Bro jaldi se hack INSTALL karo abhi only SURESHOT aa rha h is se pahle hack work na kare profit bna lo 🚀''')

    await context.bot.send_audio(chat_id=chat_id, audio=AUDIO_ID , caption='''PURA VOICE SUNO OR KARO💯''')


# ================= APP =================

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(ChatJoinRequestHandler(handle_join_request))
app.add_handler(MessageHandler(filters.ALL, get_file_id))

app.run_polling()
