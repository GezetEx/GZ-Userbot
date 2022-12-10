from os import getenv

API_ID = int(getenv("API_ID", "26653586")) #optional
API_HASH = getenv("API_HASH", "89556c81a82b5aee3666d5347adacda0") #optional

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
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQBiMZkAXzzwxLVTzq0CxrAP9awH2ay3RJ8Z79m2lVpjKjMWnlzbi0QraDDcAoFr1lHoRps5pxPqIJpOAVhpTwhM2OLKZsxEg4BDvyR81LamHU3Oxk0DYherCTHsiNiEudVB7NTwhSCPG1sAwYwgZaxxuI4px3t817cB52_nThXDrilhUIixvLaZ6fkWbcuc2_jmE0IptltX2k5UDETvjdn2l41MvNiCuRqYF9WzbekHX6KD207x3ikSiD5zYV5JACGH6GMW0XdiKZ2kb_z9c-VZ1HKrndxzLUwS51q9k-jjHWCRihCmJWYtZWhu4uXiWOxonUP6kQUuKz7XBD9GDsgi3BlpLgAAAABxZPfWAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
