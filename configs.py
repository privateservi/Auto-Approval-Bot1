# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "28185220"))
    API_HASH = getenv("API_HASH", "7775088403abbe110d5a38cfc75addce")
    BOT_TOKEN = getenv("BOT_TOKEN", "6186689074:AAHiYqcLENWGvUpaEAy1ei8rLnFAkt081IY")
    FSUB = getenv("FSUB", "QTVS_BOT_X_CLOUD")
    CHID = int(getenv("CHID", "-1001931700058"))
    SUDO = list(map(int, getenv("SUDO", "885675538").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://hillsking1222:kuraman1@kumaran1.d6ahc05.mongodb.net/?retryWrites=true&w=majority")
    PORT = getenv("PORT", "8080") 

cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
