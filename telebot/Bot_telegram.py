import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googleapiclient.discovery import build
from pytube import YouTube
from string import  Template
import time

# Função para o comando /start
def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Eu sou um bot TEST telegram.")

# Função para responder a mensagens de texto
def echo(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def help_command(update:Update, context: CallbackContext):
    help_message=   "Olá! Eu sou um bot do Telegram.\n\n" \
                    "Posso ajudar com os seguintes comandos:\n" \
                    "/start - Iniciar o bot\n" \
                    "/ajuda - Exibir esta mensagem de ajuda\n"\
                    "/p (nome do video) - Pesquisa videos no YouTube\n"\
                    "/baixar (link do video) - Baixa os videos do Youtube para seu dispositivo"

    context.bot.send_message(chat_id=update.effective_chat.id, text=help_message)


def search_videos_command_two(update: Update, context: CallbackContext):
    query = ' '.join(context.args)  # Obtém a consulta de pesquisa dos argumentos do comando

    api_key = 'Key_YOUTUBE'
    youtube = build('youtube', 'v3', developerKey=api_key)
    #search_videos = youtube.search().list(**search_params).execute()

    videos = youtube.search().list(query).execute()   # Chama a função search_videos() para pesquisar vídeos


    if videos:
        for video in videos:
            message = f"Title: {video['title']}\nVideo ID: {video['video_id']}\nThumbnail: {video['thumbnail']}\n\n"
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Nenhum vídeo encontrado.")


def search_videos_command(update: Update, context: CallbackContext):
    # Chave da API do YouTube
    api_key = 'Key_YOUTUBE'

    # Criação de um objeto de serviço do YouTube
    youtube = build('youtube', 'v3', developerKey=api_key)

    query = ' '.join(context.args)
    # Parâmetros da pesquisa de vídeos
    search_params = {
        'q': query,            # Consulta de pesquisa
        'part': 'snippet',     # Partes dos recursos a serem incluídas na resposta
        'maxResults': 5       # Número máximo de resultados a serem retornados
    }

    # Executa a pesquisa de vídeos
    response = youtube.search().list(**search_params).execute()

    # Extrai informações relevantes dos resultados
    videos = []

    for item in response['items']:
        templ = Template("Titulo: ${title}, Link:${video_id}, ${thumbnails} Download_link:${download_link}")
        video = {
            'title': item['snippet']['title'].encode('utf-8'),     # Título do vídeo
            'video_id': f"https://www.youtube.com/results?search_query={query.replace(' ','+')}",     # ID do vídeo
            'thumbnails':  item['snippet']['thumbnails']['default']['url'],
            'download_link': item['id'].get('videoId',' ')

        }
        videos.append(templ.substitute(video))
        time.sleep(.5)
        context.bot.send_message(chat_id=update.effective_chat.id, text=videos)
        videos.clear()


def download_video_command(update: Update, context: CallbackContext):
    # Obtém o link do vídeo a ser baixado
    video_link = context.args[0]

    try:
        # Cria uma instância do objeto YouTube com o link do vídeo
        yt = YouTube(video_link if video_link.startswith("https://") else f"https://www.youtube.com/watch?v={video_link}")

        # Seleciona a melhor qualidade disponível
        video = yt.streams.get_highest_resolution()

        # Faz o download do vídeo para o diretório atual
        video.download()

        context.bot.send_message(chat_id=update.effective_chat.id, text="Download concluído com sucesso!")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Ocorreu um erro durante o download: {str(e)}")


def main():
    # Token do seu bot
    token = "key_telegram"

    # Criação do objeto updater
    updater = Updater(token=token, use_context=True)

    # Registro dos handlers
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('ajuda', help_command))
    dispatcher.add_handler(CommandHandler('p', search_videos_command))
    dispatcher.add_handler(CommandHandler('baixar', download_video_command))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))

    # Inicia o bot
    updater.start_polling()

    # Mantém o bot em execução
    updater.idle()

if __name__ == '__main__':
    main()

