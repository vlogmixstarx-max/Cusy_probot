from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters,)
import requests
TOKEN ="8629533245:AAG561-Z2tGM8dIo_EIE57JxhC-QxqeaMpU"
ADMIN_ID = 6516959286
OPENROUTER_API_KEY = "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"
notes_db = {}
users = set()

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    users.add(update.effective_user.id)
    keyboard = [
        [InlineKeyboardButton("📌 Save Note", callback_data="save")],
        [InlineKeyboardButton("📖 View Notes", callback_data="view")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome! Ye ek advanced bot hai 🔥",
        reply_markup=reply_markup
    )

# Save note
async def save_note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Note bhejo jo save karna hai:")
    context.user_data["waiting_for_note"] = True

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Anti spam basic
    if len(update.message.text) > 500:
        await update.message.reply_text("Message too long 🚫")
        return

    if context.user_data.get("waiting_for_note"):
        notes_db.setdefault(user_id, []).append(update.message.text)
        await update.message.reply_text("Note saved ✅")
        context.user_data["waiting_for_note"] = False

# View notes
async def view_notes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_notes = notes_db.get(user_id, [])

    if not user_notes:
        await update.message.reply_text("No notes found.")
    else:
        text = "\n\n".join(user_notes)
        await update.message.reply_text(f"📖 Your Notes:\n\n{text}")

# Button handler
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "save":
        context.user_data["waiting_for_note"] = True
        await query.message.reply_text("how are you:")

    elif query.data == "view":
        await view_notes(update, context)
async def ai_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    result = response.json()

    try:
        answer = result["choices"][0]["message"]["content"]
    except:
        answer = "⚠️ AI error aaya, baad me try karo."

    await update.message.reply_text(answer)
# Broadcast (Admin only)
async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("Not authorized 🚫")
        return

    message = " ".join(context.args)
    for user in users:
        try:
            await context.bot.send_message(chat_id=user, text=message)
        except:
            pass

    await update.message.reply_text("Broadcast sent ✅")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("broadcast", broadcast))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, ai_reply))
app.add_handler(CallbackQueryHandler(button_handler))
app.run_polling()
