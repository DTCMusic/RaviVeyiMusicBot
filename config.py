from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("")
API_HASH = getenv("")

BOT_TOKEN = getenv("BOT_TOKEN", "6991778757:AAEcSoiTHCR8P3gx7qoNUi6rGcmNh1jOeps")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6634423600"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/LbhfP48RAK1mHKvn7")
START_IMG = getenv("START_IMG", "https://images.app.goo.gl/azovyQQZ44g2s5TW8")

SESSION = getenv("SESSION", "AgG2-QIANl-f1rn37GqyF6sdQoVtFI-GIovlXhsBfR-TRgJS91c6xNClvAfI6XhCAdkD-Iw9MCEIUptykA0gmfdcUdPO-mihl7LIi-muJl5FX8AGFjgxZsL1DfE_Fj_MoiBs7-chaPpHFOjzlCYJ5TKfkyABHoAkzwl5sAWIxxKrYtLaHYM4j9VuqsoxgiUjfehHflXrwPmKALppKjfvREmIBU8PAJCTlWnWpuSSNWovxjBHA9jYcsP9ZJXWf04UAAoAMPTjlpAkUMO_QxkCEvreRKYjkukscA6hkZb7CAFQ3KZa2fBbMdp1r7ulkebvZAhrbWiriE5a2TwclizTrl2uGg6QAAAAF2FQicAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/nezrinsupp")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/nezrinlogo")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6634423600").split()))


FAILED = "https://images.app.goo.gl/fwY1U1FQh9Qna55s8"
