from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = "8434008270:AAHGoP-vTtUCQkam-Q1S_5q3NAlo19zlrSI"
ALLOWED_USER_ID = 6249696228

FILES_DIR = "files"
os.makedirs(FILES_DIR, exist_ok=True)

async def handle_file(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.from_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("⛔ دسترسی نداری")
        return

    file = update.message.document or update.message.video or update.message.audio
    if not file:
        await update.message.reply_text("❌ لطفاً فایل بفرست")
        return

    tg_file = await context.bot.get_file(file.file_id)
    filename = file.file_name or file.file_id
    path = os.path.join(FILES_DIR, filename)

    await tg_file.download_to_drive(path)

    base_url = context.bot_data.get("BASE_URL", "")
    link = f"{base_url}/files/{filename}"

    await update.message.reply_text(f"✅ لینک مستقیم:\n{link}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.bot_data["BASE_URL"] = os.environ.get("BASE_URL", "")
    app.add_handler(MessageHandler(filters.Document.ALL | filters.VIDEO | filters.AUDIO, handle_file))
    app.run_polling()

if __name__ == "__main__":
    main()
