import requests
from funcionesscrap import scraper_guardian

# PON TU TOKEN y CHAT_ID directamente
BOT_TOKEN = "8204875540:AAGoSRVg1vAQedtsWkNz0XAulVofEkSHSPc"
CHAT_ID = "8054433476"

def telegram_bot_sendtext(bot_message):
    """
    Envía un mensaje a Telegram usando un bot con parse_mode HTML.
    """
    send_text = (
        f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
        f'?chat_id={CHAT_ID}'
        f'&parse_mode=HTML'
        f'&text={bot_message}'
    )
    try:
        response = requests.get(send_text, timeout=10)
        return response.json()
    except requests.RequestException as e:
        print(f"Error al enviar mensaje: {e}")
        return None

if __name__ == "__main__":
    ultimo_post = scraper_guardian()
    print("DEBUG: Último post ->", ultimo_post)

    if ultimo_post:
        # Usando HTML para el mensaje
        mensaje = f"📰 <b>Nuevo post en PokéGuardian</b>\n<a href='{ultimo_post}'>Ver artículo</a>"
        resultado = telegram_bot_sendtext(mensaje)
        print("DEBUG: Telegram ->", resultado)
    else:
        print("No se encontró ningún post.")

