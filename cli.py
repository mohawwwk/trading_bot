import argparse
from bot.orders import place_order

def main():
    parser = argparse.ArgumentParser(
        description="🤖 Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        type=str,
        required=True,
        help="Trading pair e.g. BTCUSDT"
    )

    parser.add_argument(
        "--side",
        type=str,
        required=True,
        choices=["BUY", "SELL"],
        help="Order side: BUY or SELL"
    )

    parser.add_argument(
        "--type",
        type=str,
        required=True,
        choices=["MARKET", "LIMIT"],
        dest="order_type",
        help="Order type: MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True,
        help="Quantity to buy/sell e.g. 0.01"
    )

    parser.add_argument(
        "--price",
        type=float,
        required=False,
        help="Price (only required for LIMIT orders)"
    )

    args = parser.parse_args()

    place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.order_type,
        quantity=args.quantity,
        price=args.price
    )

if __name__ == "__main__":
    main()