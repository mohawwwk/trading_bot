from bot.client import BinanceClient
from bot.validators import validate_inputs
from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(symbol, side, order_type, quantity, price=None):

    # Step 1: Validate inputs
    errors = validate_inputs(symbol, side, order_type, quantity, price)
    if errors:
        for error in errors:
            logger.error(f"Validation error: {error}")
            print(f"❌ {error}")
        return

    # Step 2: Build order summary and print it
    print("\n--- Order Request Summary ---")
    print(f"  Symbol     : {symbol.upper()}")
    print(f"  Side       : {side.upper()}")
    print(f"  Order Type : {order_type.upper()}")
    print(f"  Quantity   : {quantity}")
    if price:
        print(f"  Price      : {price}")
    print("-----------------------------\n")

    # Step 3: Build the params for Binance
    client = BinanceClient()

    params = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }

    if order_type.upper() == "LIMIT":
        params["price"] = price
        params["timeInForce"] = "GTC"

    # Step 4: Send the order
    try:
        response = client.place_order(**params)

        if "orderId" in response:
            print("✅ Order placed successfully!")
            print("\n--- Order Response ---")
            print(f"  Order ID     : {response.get('orderId')}")
            print(f"  Status       : {response.get('status')}")
            print(f"  Executed Qty : {response.get('executedQty')}")
            print(f"  Avg Price    : {response.get('avgPrice', 'N/A')}")
            print("----------------------\n")
        else:
            print("❌ Order failed!")
            print(f"  Reason: {response.get('msg', 'Unknown error')}")
            logger.error(f"Order failed: {response}")

    except Exception as e:
        print(f"❌ Something went wrong: {e}")
        logger.error(f"Exception during order placement: {e}")