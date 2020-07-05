import pickle
from skyline import *
from cl.SkylineVisitor import SkylineVisitor
from cl.SkylineParser import SkylineParser
from cl.SkylineLexer import SkylineLexer
from antlr4 import *
import os
import matplotlib.pyplot as plt
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import matplotlib
matplotlib.use('Agg')


def start(update, context):
    message = "SkyLine Bot!\nBenvingut " + update.effective_chat.first_name + "!\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    if not os.path.exists(str(update.message.chat_id)):
        os.makedirs(str(update.message.chat_id))


def author(update, context):
    message = "SkyLine Bot!\n@ Jing Luis Cao, 2020\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def get_help(update, context):
    message = "/start: inicia la conversa amb el Bot.\n" + "/help: llista les possibles comandes i una breu descripcio.\n" + "/author: indica el nom complet de l'autor del projecte i el correu electronic\n" + \
        "/lst: mostra els identificadors definits i la seva corresponent àrea.\n" + "/clean: esborra tots els identificadors definits.\n" + \
        "/save id: guarda un skyline definit amb el nom id.sky.\n" + \
        "/load id: carrega un skyline de l'arxiu id.sky.\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def list_skylines(update, context):
    message = "Aquí tens la llista de skylines definits amb l'alçada corresponent: \n"
    for elem in context.user_data:
        message += elem
        message += ":\t"
        x, y = context.user_data[elem].get_information()
        message += str(x)
        message += "\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


def clean_skylines(update, context):
    context.user_data.clear()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="skylines esborrats amb èxit")


def get_skyline(update, context):
    message = update.message.text
    print(message)
    try:
        lexer = SkylineLexer(InputStream(message))
        token_stream = CommonTokenStream(lexer)
        parser = SkylineParser(token_stream)
        tree = parser.root()
        visitor = SkylineVisitor(context.user_data)
        skyl = visitor.visit(tree)

        if isinstance(skyl, Skyline):
            fitxer = "%d.png" % random.randint(1000000, 9999999)
            x, y, w = skyl.get_values_of_plot()
            plt.clf()
            plt.bar(x, y, width=w, color=(1, 0, 0, 1))
            plt.savefig(fitxer, bbox_inches='tight')
            context.bot.send_photo(
                chat_id=update.effective_chat.id, photo=open(
                    fitxer, 'rb'))
            os.remove(fitxer)
            area, height = skyl.get_information()
            message = "area: " + str(area) + "\nalçada: " + str(height) + "\n"
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=message)
        else:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text='💣 Error en realitzar l\'operació')

    except Exception as e:
        print(e)
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣 Error en realitzar l\'operació')


def save_skylines(update, context):
    skyline_id = context.args[0]
    if skyline_id not in context.user_data:
        context.bot.send_message(chat_id=update.effective_chat.id, text='💣')
    file_name = "./" + str(update.message.chat_id) + "/" + skyline_id + ".sky"
    file = open(file_name, 'wb')
    pickle.dump(context.user_data[skyline_id], file)
    file.close()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='skyline guardat amb èxit')


def load_skylines(update, context):
    skyline_id = context.args[0]
    file_name = "./" + str(update.message.chat_id) + "/" + skyline_id + ".sky"
    try:
        file = open(file_name, 'rb')
        context.user_data[skyline_id] = pickle.load(file)
        file.close()
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='skyline carregat amb èxit')
        fitxer = "%d.png" % random.randint(1000000, 9999999)
        x, y, w = context.user_data[skyline_id].get_values_of_plot()
        plt.clf()
        plt.bar(x, y, width=w, color=(1, 0, 0, 1))
        plt.savefig(fitxer, bbox_inches='tight')
        context.bot.send_photo(
            chat_id=update.effective_chat.id, photo=open(
                fitxer, 'rb'))
        os.remove(fitxer)
        area, height = context.user_data[skyline_id].get_information()
        message = "area: " + str(area) + "\nalçada: " + str(height) + "\n"
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message)
    except Exception as e:
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='💣 Error en carregar el fitxer')


# declara una constant amb el access token que llegeix de token.txt
TOKEN = open('token.txt').read().strip()

# crea objectes per treballar amb Telegram
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

# indica que quan el bot rebi la comanda /start s'executi la funció start
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('author', author))
dispatcher.add_handler(CommandHandler('help', get_help))
dispatcher.add_handler(CommandHandler('clean', clean_skylines))
dispatcher.add_handler(CommandHandler('lst', list_skylines))
dispatcher.add_handler(CommandHandler('save', save_skylines))
dispatcher.add_handler(CommandHandler('load', load_skylines))

dispatcher.add_handler(MessageHandler(Filters.all, get_skyline))
# engega el bot
updater.start_polling()
