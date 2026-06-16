import aiohttp

class TelegramNotifier:

    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    async def send(self, chat_id, message):

        async with aiohttp.ClientSession() as session:

            await session.post(
                self.webhook_url,
                json={
                    "content": message
                }
            )

        print("Discord alert sent")
