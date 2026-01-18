import requests
from funcionesscrap import scraper_guardian


def telegram_bot_sendtext(bot_message):
    bot_token = 'VuestroToken'
    bot_chatID = 'VuestroChatId'

    send_text = (
        f'https://api.telegram.org/bot{bot_token}/sendMessage'
        f'?chat_id={bot_chatID}'
        f'&parse_mode=Markdown'
        f'&text={bot_message}'
    )

    response = requests.get(send_text)
    return response.json()


if __name__ == "__main__":
    ultimo_post = scraper_guardian()

    if ultimo_post:
        mensaje = f"📰 *Nuevo post en PokéGuardian*\n{ultimo_post}"
        telegram_bot_sendtext(mensaje)
