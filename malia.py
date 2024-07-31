import random
import os
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, Application

# Token do Bot do BotFather
TOKEN = secrets.TELEGRAM_TOKEN

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Bem-vindo ao Bot pra Malia! Use /help para ver todos os comandos.')

async def mensagem(update: Update, context: CallbackContext) -> None:
    lista_mensagem = ["Eu te adoro minha bbzinha",
                      "Você é minha princezinha mais linda",
                      "Um colação pra você meu amor ❤️"]
    
    mensagem_final = random.choice(lista_mensagem)

    await update.message.reply_text(mensagem_final)

async def foto(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    lista_imagens = [image for image in os.listdir("fotos")]
    imagem_escolhida = random.choice(lista_imagens)
    with open(os.path.join("fotos", imagem_escolhida), 'rb') as image_file:
        texto = imagem_escolhida.split(".")[0]
        await context.bot.send_photo(chat_id=chat_id, photo=image_file)
        await update.message.reply_text(texto)

async def help(update: Update, context: CallbackContext) -> None:
    comandos = '''
/mensagem: retorna uma mensagem fofinha pro meu bb
/foto: retorna uma foto nossa juntos'''
    await update.message.reply_text(comandos)
def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('mensagem', mensagem))
    application.add_handler(CommandHandler('foto', foto))
    application.add_handler(CommandHandler('help', help))

    application.run_polling()

if __name__ == '__main__':
    main()
