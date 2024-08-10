from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24548143"))
API_HASH = getenv("6cba049c135a0393615878ea1e3c9443")

BOT_TOKEN = getenv("BOT_TOKEN", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6634423600"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/LbhfP48RAK1mHKvn7")
START_IMG = getenv("START_IMG", "https://images.app.goo.gl/azovyQQZ44g2s5TW8")

SESSION = getenv("SESSION", AgG2-QIAHwh9cL2kectPPgIU57z0vHpYWQFSlq-CsO_DBbrrnuZ6MM_zH7d7mEU5qFzNpFcZyT3NT0Zy4lcG8uI63iUyqKdMmSe3_I8b7Yv4MeLJs_-ZMJW-xNS9f0QZioe8nruwqEWiFm80tb3JY9q9UVWQwFfkvxZYvMD6Twgj5vq5z3VPxPqSQ-WwchUSkiAcUN2rtkZuYimeOT-KCdqAWv22AdKw2eVHunFshMEgjBHtAgFvLhhhUaTr-VUB8u0wSMmjqEh848xR0YIbpdpMdY9TQIM91_h_SUkgVwLahlWg86JP4LupFckgVSI2x0U4Oc9S5ERz3kbOZ9EKFM8KpZwQAAAAF2FQicAA)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/riyaddSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AyselProje")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6634423600").split()))


FAILED = "https://images.app.goo.gl/fwY1U1FQh9Qna55s8"
