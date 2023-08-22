from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("16102648"))
API_HASH = getenv("378a73e340eb634cf67c8c42bafa9f37")

BOT_TOKEN = getenv("BOT_TOKEN", 6144849731:AAGCFecE_S1i3BYB5wEtnPMZs70ypB53WGo)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6181182367"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/LbhfP48RAK1mHKvn7")
START_IMG = getenv("START_IMG", "https://images.app.goo.gl/azovyQQZ44g2s5TW8")

SESSION = getenv("SESSION", AgBBAwGPjEkCV-WUNsXHJQfv_SeroXM9zXbdhVrfqnqDRVYN5RbZY6zvgmafx7908wpKv8j-EIyF1B0YXMzcJVn7yn57g15PtDu3q8scfCCXzwyqCJZs2NEZnzjm0HmVvQKau92TLH_i-ueN6PvqlGFEcMrNOhyosaohie52pmLFBQpsy0ihjdoMbjFqBRuy6LJ9u2AjRy6KkaphKXedBJGHTbrADUZA1PFB8qJ3govOpRBsJxSETTDXUok1QwKFgV4wQ4_yN61kzObHUYxUfFoDfeE0zvYTTvi5NmS_ptUPubYJibfFHWVJFzuMMH4EYJjgs2uW-IepGP2ujEboTRd4AAAAAUiRuNYA)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/riyaddSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AyselProje")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5519651365").split()))


FAILED = "https://images.app.goo.gl/fwY1U1FQh9Qna55s8"
