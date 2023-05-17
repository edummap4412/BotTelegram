
# Bot Telegram para Pesquisa e Download de Vídeos do YouTube

Este é um bot do Telegram desenvolvido em Python que permite pesquisar e baixar vídeos do YouTube. O bot possui os seguintes recursos:

- `/start`: Inicia o bot e exibe uma mensagem de boas-vindas.
- `/ajuda`: Exibe uma mensagem de ajuda com os comandos disponíveis.
- `/p (nome do vídeo)`: Pesquisa vídeos no YouTube com base no nome fornecido.
- `/baixar (link do vídeo)`: Baixa vídeos do YouTube para o seu dispositivo.
- Responde a mensagens de texto enviadas ao bot.

## Configuração

Antes de executar o bot, você precisa realizar as seguintes etapas de configuração:

1. Instale as bibliotecas necessárias: `telegram`, `google-api-python-client`, `pytube`.

   ```shell
   pip install python-telegram-bot google-api-python-client pytube
   ```

2. Obtenha as chaves de API necessárias:

   - Chave de API do Telegram: Para obter a chave de API do Telegram, você precisa criar um bot no BotFather e obter o token do bot.
   - Chave de API do YouTube: Para obter a chave de API do YouTube, siga as instruções na documentação oficial do YouTube para criar um projeto e habilitar a API do YouTube. Em seguida, crie uma chave de API e anote-a.

3. Substitua as chaves de API no código:

   - Substitua `'Key_YOUTUBE'` pela sua chave de API do YouTube.
   - Substitua `'key_telegram'` pelo token do seu bot Telegram.

## Uso

Após concluir as etapas de configuração, você pode executar o bot com o seguinte comando:

```shell
python nome_do_arquivo.py
```

Certifique-se de substituir `nome_do_arquivo.py` pelo nome do arquivo em que você salvou o código.

## Comandos disponíveis

- `/start`: Inicia o bot e exibe uma mensagem de boas-vindas.
- `/ajuda`: Exibe uma mensagem de ajuda com os comandos disponíveis.
- `/p (nome do vídeo)`: Pesquisa vídeos no YouTube com base no nome fornecido.
- `/baixar (link do vídeo)`: Baixa vídeos do YouTube para o seu dispositivo.

Além dos comandos, o bot também responde a mensagens de texto enviadas a ele.

**Observação**: Certifique-se de que o bot tenha permissão para ler e enviar mensagens no grupo ou conversa em que ele está sendo usado.
