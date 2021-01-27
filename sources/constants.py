# -*- coding: utf-8 -*-

'''
Script:
    constants.py
Description:
    Constants values for join_captcha_bot.py
Author:
    Jose Rios Rubio
Creation date:
    09/09/2018
Last modified date:
    26/01/2021
Version:
    1.15.6
'''

###############################################################################
### Imported modules ###

from os import path as os_path
from os import getenv as os_getenv
from settings import SETTINGS

###############################################################################
### Constants ###

# Actual constants.py full path directory name
SCRIPT_PATH = os_path.dirname(os_path.realpath(__file__))

# General Bots Parameters
CONST = {

    # Bot Public or Private
    "BOT_PRIVATE": \
        bool(int(os_getenv("CAPTCHABOT_PRIVATE", \
            SETTINGS["CAPTCHABOT_PRIVATE"]))),

    # Bot Token (get it from @BotFather)
    "TOKEN": \
        os_getenv("CAPTCHABOT_TOKEN", SETTINGS["CAPTCHABOT_TOKEN"]),

    # Bot Owner (i.e. "@JoseTLG" or "123456789")
    "BOT_OWNER": \
        os_getenv("CAPTCHABOT_OWNER", SETTINGS["CAPTCHABOT_OWNER"]),

    # Bot Webhook Host addres (keep in None for Polling or set to a
    # valid address for Webhook)
    "WEBHOOK_HOST": \
        os_getenv("CAPTCHABOT_WEBHOOK_HOST", \
            SETTINGS["CAPTCHABOT_WEBHOOK_HOST"]),

    # Bot Webhook Host Port (this is not used if WEBHOOK_HOST is None)
    "WEBHOOK_PORT": \
        int(os_getenv("CAPTCHABOT_WEBHOOK_PORT", \
            SETTINGS["CAPTCHABOT_WEBHOOK_PORT"])),

    # Bot Webhook Certificate file path (this is not used if
    # WEBHOOK_HOST is None)
    "WEBHOOK_CERT": \
        os_getenv("CAPTCHABOT_WEBHOOK_CERT", \
            SETTINGS["CAPTCHABOT_WEBHOOK_CERT"]),

    # Bot Webhook Certificate private key file path (this is not used
    # if WEBHOOK_HOST is None)
    "WEBHOOK_CERT_PRIV_KEY": \
        os_getenv("CAPTCHABOT_WEBHOOK_CERT_PRIV_KEY", \
            SETTINGS["CAPTCHABOT_WEBHOOK_CERT_PRIV_KEY"]),

    # Chats directory path
    "CHATS_DIR": \
        os_getenv("CAPTCHABOT_CHATS_DIR", SETTINGS["CAPTCHABOT_CHATS_DIR"]),

    # Directory where create/generate temporary captchas
    "CAPTCHAS_DIR": \
        os_getenv("CAPTCHABOT_CAPTCHAS_DIR", \
            SETTINGS["CAPTCHABOT_CAPTCHAS_DIR"]),

    # Global whitelist file path (to allow whitelist blind users in
    # all groups)
    "F_WHITE_LIST": \
        os_getenv("CAPTCHABOT_F_WHITE_LIST", \
            SETTINGS["CAPTCHABOT_F_WHITE_LIST"]),

    # Global whitelist file path (to allow whitelist blind users in
    # all groups)
    "F_ALLOWED_GROUPS": \
        os_getenv("CAPTCHABOT_F_ALLOWED_GROUPS", \
            SETTINGS["CAPTCHABOT_F_ALLOWED_GROUPS"]),

    # Initial enable/disable status at Bot start
    "INIT_ENABLE": \
        bool(int(os_getenv("CAPTCHABOT_INIT_ENABLE", \
            SETTINGS["CAPTCHABOT_INIT_ENABLE"]))),

    # Initial captcha solve time (in minutes)
    "INIT_CAPTCHA_TIME_MIN": \
        int(os_getenv("CAPTCHABOT_INIT_CAPTCHA_TIME_MIN", \
            SETTINGS["CAPTCHABOT_INIT_CAPTCHA_TIME_MIN"])),

    # Initial captcha difficult level
    "INIT_CAPTCHA_DIFFICULTY_LEVEL": \
        int(os_getenv("CAPTCHABOT_INIT_CAPTCHA_DIFFICULTY_LEVEL", \
            SETTINGS["CAPTCHABOT_INIT_CAPTCHA_DIFFICULTY_LEVEL"])),

    # Initial captcha characters mode (ascii, hex, nums, or button)
    "INIT_CAPTCHA_CHARS_MODE": \
        os_getenv("CAPTCHABOT_INIT_CAPTCHA_CHARS_MODE", \
            SETTINGS["CAPTCHABOT_INIT_CAPTCHA_CHARS_MODE"]),

    # Default time (in mins) to remove self-destruct sent messages
    # from the Bot
    "T_DEL_MSG": \
        int(os_getenv("CAPTCHABOT_T_DEL_MSG", \
            SETTINGS["CAPTCHABOT_T_DEL_MSG"])),

    # Auto-remove custom welcome message timeout
    "T_DEL_WELCOME_MSG": \
        int(os_getenv("CAPTCHABOT_T_DEL_WELCOME_MSG", \
            SETTINGS["CAPTCHABOT_T_DEL_WELCOME_MSG"])),

    # Maximum number of users allowed in each chat ignore list
    "IGNORE_LIST_MAX": \
        int(os_getenv("CAPTCHABOT_IGNORE_LIST_MAX", \
            SETTINGS["CAPTCHABOT_IGNORE_LIST_MAX"])),

    # Initial new users just allow to send text messages
    "INIT_RESTRICT_NON_TEXT_MSG": \
        int(os_getenv("CAPTCHABOT_INIT_RESTRICT_NON_TEXT_MSG", \
            SETTINGS["CAPTCHABOT_INIT_RESTRICT_NON_TEXT_MSG"])),

    # Custom Welcome message max length
    "MAX_WELCOME_MSG_LENGTH": \
        int(os_getenv("CAPTCHABOT_MAX_WELCOME_MSG_LENGTH", \
            SETTINGS["CAPTCHABOT_MAX_WELCOME_MSG_LENGTH"])),

    # Languages texts files directory path
    "LANG_DIR": SCRIPT_PATH + "/language",

    # Chat configurations JSON files
    "F_CONF": "configs.json",

    # Initial chat title at Bot start
    "INIT_TITLE": "Unknown Chat",

    # Initial chat link at Bot start
    "INIT_LINK": "Unknown",

    # Initial language at Bot start
    "INIT_LANG": "EN",

    # Number of seconds in a day (60s x 60m x 24h)
    "T_SECONDS_IN_A_DAY": 86400,

    # Command don't allow in private chat text (just english due in
    # private chats we don't have language configuration)
    "CMD_NOT_ALLOW_PRIVATE": "Can't use this command in the current chat.",

    # Command just allow for Bot owner
    "CMD_JUST_ALLOW_OWNER": "This command just can be use by the Bot Owner",

    # Whitelist usage
    "WHITELIST_USAGE": "Command usage (user ID or Alias):\n" \
        "/whitelist add @peter123\n" \
        "/whitelist rm 123456789",

    # Allowgroup usage
    "ALLOWGROUP_USAGE": "Command usage (group ID):\n" \
        "/allowgroup add -1001142817523\n" \
        "/allowgroup rm -1001142817523",

    # Allowgroup usage
    "NOT_ALLOW_GROUP": "Hi, this Bot account is private and is not allowed " \
        "to be used here. Contact to Bot account owner ({}) if you want to " \
        "use the Bot in this group.\n" \
        "\n" \
        "Actual chat ID (Bot owner needs this to allow this group):\n" \
        "{}\n" \
        "\n" \
        "Also, remember that you can create your own Bot account for " \
        "free:\n" \
        "{}",

    # IANA Top-Level-Domain List
    # https://data.iana.org/TLD/tlds-alpha-by-domain.txt
    "F_TLDS": "tlds-alpha-by-domain.txt",

    # Regular expression to detect URLs in a string
    "REGEX_URLS": \
        r"((?<=[^a-zA-Z0-9])*(?:https\:\/\/|[a-zA-Z0-9]{{1,}}\.{{1}}|\b)" \
        r"(?:\w{{1,}}\.{{1}}){{1,5}}(?:{})\b/?(?!@))",

    # List string of supported languages commands shows in invalid
    # language set
    "SUPPORTED_LANGS_CMDS": \
        "\nArabic / Arabic\n/language ar\n" \
        "\nBasque / Euskal\n/language eu\n" \
        "\nCatalan / Català\n/language ca\n" \
        "\nChinese-Simplified / 中文\n/language zh_cn\n" \
        "\nDutch / Nederlands\n/language nl\n" \
        "\nEnglish / English\n/language en\n" \
        "\nEsperanto\n/language eo\n" \
        "\nFrench / Francais\n/language fr\n" \
        "\nGalician / Galego\n/language gl\n" \
        "\nGerman / Deutsch\n/language de\n" \
        "\nIndonesian / Indonesia\n/language id\n" \
        "\nItalian / Italiano\n/language it\n" \
        "\nKannada / Kannada\n/language kn\n" \
        "\nPolish / Polskie\n/language pl\n" \
        "\nPortuguese-Brazil / Português-Brasil\n/language pt_br\n" \
        "\nRussian / Pусский\n/language ru\n" \
        "\nSlovak / Slovenčine\n/language sk\n" \
        "\nSpanish / Español\n/language es\n" \
        "\nTurkish / Türkçe\n/language tr\n" \
        "\nUkrainian / Українську\n/language uk\n",

    # Bot developer
    "DEVELOPER": "@JoseTLG",

    # Bot code repository
    "REPOSITORY": "https://github.com/J-Rios/TLG_JoinCaptchaBot",

    # Developer Paypal address
    "DEV_PAYPAL": "https://www.buymeacoffee.com/joincaptchabot",

    # Developer Bitcoin address
    "DEV_BTC": "3N9wf3FunR6YNXonquBeWammaBZVzTXTyR",

    # Bot version
    "VERSION": "1.15.6 (26/01/2021)"
}


# Supported languages list
TEXT = {
    "AR": {}, # Arabic
    "CA": {}, # Catalan
    "DE": {}, # German
    "EN": {}, # English
    "EO": {}, # Esperanto
    "ES": {}, # Spanish
    "EU": {}, # Basque
    "FR": {}, # French
    "GL": {}, # Galician
    "ID": {}, # Indonesian
    "IT": {}, # Italian
    "KN": {}, # Kannada
    "NL": {}, # Dutch
    "PL": {}, # Polish
    "PT_BR": {}, # Portuguese (Brasil)
    "RU": {}, # Rusian
    "SK": {}, # Slovak
    "TR": {}, # Turkish
    "UK": {}, # Ukrainian
    "ZH_CN": {} # Chinese (Mainland)
}
