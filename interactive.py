import questionary
from bot.orders import place_order

def run_interactive():
    print("\n🤖 Welcome to Binance Futures Trading Bot\n")

    symbol = questionary.select(
        "Select trading pair:",
        choices=["BTCUSDT", "ETHUSDT", "BNBUSDT"]
    ).ask()

    side = questionary.select(
        "Select side:",
        choices=["BUY", "SELL"]
    ).ask()

    order_type = questionary.select(
        "Select order type:",
        choices=["MARKET", "LIMIT"]
    ).ask()

    quantity = questionary.text(
        "Enter quantity (e.g. 0.01):",
        validate=lambda val: True if float(val) > 0 else "Must be greater than 0"
    ).ask()

    price = None
    if order_type == "LIMIT":
        price = questionary.text(
            "Enter price (e.g. 85000):",
            validate=lambda val: True if float(val) > 0 else "Must be greater than 0"
        ).ask()

    # Confirm before placing
    confirm = questionary.confirm(
        f"\nPlace {order_type} {side} order for {quantity} {symbol}?"
    ).ask()

    if confirm:
        place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=float(quantity),
            price=float(price) if price else None
        )
    else:
        print("❌ Order cancelled.")

if __name__ == "__main__":
    run_interactive()