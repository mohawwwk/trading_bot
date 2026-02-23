# 🤖 Binance Futures Testnet Trading Bot

A Python CLI trading bot that places Market and Limit orders on Binance Futures Testnet (USDT-M).

---

## Project Structure
```
trading_bot/
  bot/
    __init__.py
    client.py          # Binance API client
    orders.py          # Order placement logic
    validators.py      # Input validation
    logging_config.py  # Logging setup
  cli.py               # CLI entry point (argparse)
  interactive.py       # Interactive menu UI (bonus)
  requirements.txt
  README.md
  .env                 # API keys (not committed to GitHub)
```

---

## Setup Steps

### 1. Clone the repository
```
git clone https://github.com/yourusername/trading_bot.git
cd trading_bot
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Create your `.env` file
```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_secret_key_here
```
Get your API keys from: https://testnet.binancefuture.com

---

## How to Run

### Option 1 — CLI mode (argparse)

**Market Order:**
```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

**Limit Order:**
```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 85000
```

### Option 2 — Interactive menu mode
```
python interactive.py
```
Use arrow keys to select options and confirm your order before placing.

---

## Logging

All API requests, responses, and errors are logged to:
```
logs/trading_bot.log
```

---

## Assumptions

- Only BTCUSDT, ETHUSDT, and BNBUSDT are supported as symbols
- Testnet only — no real money involved
- LIMIT orders require a price, MARKET orders do not
- Python 3.x required
```

---

### Step 3: Create a `.gitignore` file so your API keys never get uploaded to GitHub

In your terminal:
```
New-Item .gitignore
```

Open it and paste:
```
.env
logs/
__pycache__/
*.pyc
```

---

### Step 4: Push to GitHub

Run these commands one by one:
```
git init
git add .
git commit -m "Binance Futures Trading Bot - initial commit"
```

Then:
1. Go to github.com and create a **new public repository** called `trading_bot`
2. Copy the commands GitHub shows you under **"push an existing repository"** and run them — looks like:
```
git remote add origin https://github.com/yourusername/trading_bot.git
git branch -M main
git push -u origin main