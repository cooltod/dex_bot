# Dex Bot

A Python bot to analyze and trade cryptocurrencies using Dexscreener and Telegram.

## Features
- Analyze and parse coin data.
- Filter coins based on blacklist and fake volume.
- Verify contracts using rugcheck.xyz.
- Trade using Toxi Solana Bot.
- Send Telegram notifications for buy/sell events.

## How to Run
1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Set up your Telegram bot token and other API keys in `config.py`.
4. Run the bot using `python bot.py`.

## Requirements
- Python 3.8+
- Libraries: `requests`, `telebot`, `pandas`