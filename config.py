from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("28768514"))
API_HASH = getenv("40761fd256d71926ac455e55fcb71ae1")

BOT_TOKEN = getenv("BOT_TOKEN", 7047765713:AAE_2l_YhoK7Qq_HNBa97wfULydSi_pO_UU))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6634423600"))

PING_IMG = getenv("PING_IMG", "https://images.app.goo.gl/LbhfP48RAK1mHKvn7")
START_IMG = getenv("START_IMG", "https://images.app.goo.gl/azovyQQZ44g2s5TW8")

SESSION = getenv("SESSION", AgBBAwGPjEkCV-WUNsXHJQfv_SeroXM9zXbdhVrfqnqDRVYN5RbZY6zvgmafx7908wpKv8j-EIyF1B0YXMzcJVn7yn57g15PtDu3q8scfCCXzwyqCJZs2NEZnzjm0HmVvQKau92TLH_i-ueN6PvqlGFEcMrNOhyosaohie52pmLFBQpsy0ihjdoMbjFqBRuy6LJ9u2AjRy6KkaphKXedBJGHTbrADUZA1PFB8qJ3govOpRBsJxSETTDXUok1QwKFgV4wQ4_yN61kzObHUYxUfFoDfeE0zvYTTvi5NmS_ptUPubYJibfFHWVJFzuMMH4EYJjgs2uW-IepGP2ujEboTRd4AAAAAUiRuNYA)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/riyaddSupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AyselProje")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5519651365").split()))


FAILED = "https://images.app.goo.gl/fwY1U1FQh9Qna55s8"
