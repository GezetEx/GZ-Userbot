from os import getenv

API_ID = int(getenv("API_ID", "6435225")) #optional
API_HASH = getenv("API_HASH", "4e984ea35f854762dcde906dce426c2d") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1902442454").split()))
OWNER_ID = int(getenv("OWNER_ID", "1902442454"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://varen:varen@varenz.uxs7ib2.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5969049243:AAHw4jSudeH64NaIaSNHkOECVCXAPumI2n8")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/GezetEx/GZ-Userbot")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAXFNd2fMPzUoF4awXA-kLjIdqO_XhguKdzY-VPI6HM7hrREGErqFM6QdzEOSllRPQH3g-Fm13jSIkHFdyWNKannJBH_CxW4i2VDl7W6bzw6hA_PetsFc7he4qn15YdQ7RI4NqsgqnHM5NdJMvCnokApuiAdvw0Qt0YpgtiOvweim7clno3PqYLefjzsk6vK6Un_4jxXyD-jZqy4abRmWAtlu4ZG8OBYkkpZNji_hHxF1jH7S9NIYUtUejpPPNiVxbeM6LccEPugoctsymKEa0yie5RmNWhMvsVUnwdFSYxv9iR0X9aH4FPoRgX1c6rC7tUdk43MkM-LoWJzkvHiNcHQAAAABxZPfWAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
