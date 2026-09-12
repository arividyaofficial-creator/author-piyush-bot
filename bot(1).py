import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

HOME = "https://authorpiyush.com/"
BOOKS = "https://authorpiyush.com/author-piyush-singh-books"
BLOG = "https://authorpiyush.com/author-piyush-singh-blog"
PSYCHOLOGY = "https://authorpiyush.com/sukoon-talk"
ABOUT = "https://authorpiyush.com/about-author-piyush-biography"
CONTACT = "https://authorpiyush.com/contact-author-piyush-singh"
ARIVIDYA = "https://arividya.in/"

def main_menu():
    keyboard = [
        [InlineKeyboardButton("📱 Open Author Piyush", web_app=WebAppInfo(url=HOME))],
        [InlineKeyboardButton("📚 My Books", url=BOOKS),
         InlineKeyboardButton("✍️ Blog", url=BLOG)],
        [InlineKeyboardButton("🧠 Psychology", url=PSYCHOLOGY),
         InlineKeyboardButton("👤 About Me", url=ABOUT)],
        [InlineKeyboardButton("🎓 ARIvidya", url=ARIVIDYA),
         InlineKeyboardButton("📩 Contact", url=CONTACT)],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "नमस्कार! 👋\n\n"
        "Welcome to the official Author Piyush Bot.\n\n"
        "यहाँ से मेरी books, blog, psychology content, "
        "ARIvidya और मेरे बारे में जानकारी सीधे खोल सकते हैं।\n\n"
        "नीचे अपना विकल्प चुनें:"
    )
    await update.message.reply_text(text, reply_markup=main_menu())

async def app_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Author Piyush खोलने के लिए नीचे tap करें:",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📱 Open Author Piyush", web_app=WebAppInfo(url=HOME))]
        ])
    )

async def books(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📚 मेरी Books:", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("📚 Explore My Books", url=BOOKS)]
    ]))

async def blog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✍️ Latest Articles:", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("✍️ Read Blog", url=BLOG)]
    ]))

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👤 About Author Piyush:", reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("👤 Read About Me", url=ABOUT)]
    ]))

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN environment variable is missing.")

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("app", app_command))
    app.add_handler(CommandHandler("books", books))
    app.add_handler(CommandHandler("blog", blog))
    app.add_handler(CommandHandler("about", about))

    app.run_polling()

if __name__ == "__main__":
    main()
