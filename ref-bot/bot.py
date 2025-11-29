import json
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8339004968:AAHcTG35zSHSY1sJyGD6Wffa03wVdvTKmlo"   # <-- thay token

# ---- Đọc JSON ----
def load_data():
    with open("data.json", "r", encoding="utf-8") as f:
        return json.load(f)

# ---- Lưu JSON ----
def save_data(data):
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


# ====== START ======
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton("💰 Số dư của tôi")],
        [KeyboardButton("🛒 Rút code"), KeyboardButton("📮 MỜI BẠN BÈ")],
        [KeyboardButton("📄 Link Game"), KeyboardButton("📊 CSKH Hỗ Trợ")]
    ]

    reply = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Chọn chức năng:", reply_markup=reply)


# ====== XỬ LÝ NÚT BẤM ======
async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    data = load_data()   # luôn đọc dữ liệu mới từ JSON

    if text == "💰 Số dư của tôi":
        await update.message.reply_text(f"Số dư: {data['balance']}đ")

    elif text == "🛒 Rút code":
        await update.message.reply_text(data["withdraw_code_note"])

    elif text == "📮 MỜI BẠN BÈ":
        await update.message.reply_text(f"Link mời: {data['invite_link']}")

    elif text == "📄 Link Game":
        await update.message.reply_text(f"Link Game: {data['game_link']}")

    elif text == "📊 CSKH Hỗ Trợ":
        await update.message.reply_text("@hotrocpbank")

    else:
        await update.message.reply_text("Không hiểu lệnh.")


# ====== MAIN ======
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, handle_buttons))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
