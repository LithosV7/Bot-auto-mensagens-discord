import discord
import asyncio

# Token do bot do Discord (substitua pelo seu próprio token)
TOKEN = 'XXX'
# ID do canal onde as mensagens serão enviadas (substitua pelo ID do seu canal)
CHANNEL_ID = XXX

# Mensagem a ser enviada
message = "Teste"

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        channel = self.get_channel(CHANNEL_ID)
        if channel is None:
            print("Não consegui encontrar o canal. Verifique o ID do canal.")
            return

        while True:  # Loop infinito para enviar a mensagem repetidamente
            await channel.send(message)
            await asyncio.sleep(10)  # Espera 10 segundos antes de enviar a próxima mensagem

client = MyClient(intents=discord.Intents.default())
client.run(TOKEN)
