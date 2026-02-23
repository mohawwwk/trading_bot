VALID_SYMBOLS = ["BTCUSDT", "ETHUSDT", "BNBUSDT"]
VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]

def validate_inputs(symbol, side, order_type, quantity, price=None):
    errors = []

    if symbol.upper() not in VALID_SYMBOLS:
        errors.append(f"Invalid symbol '{symbol}'. Choose from: {VALID_SYMBOLS}")

    if side.upper() not in VALID_SIDES:
        errors.append(f"Invalid side '{side}'. Choose BUY or SELL.")

    if order_type.upper() not in VALID_ORDER_TYPES:
        errors.append(f"Invalid order type '{order_type}'. Choose MARKET or LIMIT.")

    try:
        qty = float(quantity)
        if qty <= 0:
            errors.append("Quantity must be greater than 0.")
    except ValueError:
        errors.append("Quantity must be a number.")

    if order_type.upper() == "LIMIT":
        if price is None:
            errors.append("Price is required for LIMIT orders.")
        else:
            try:
                p = float(price)
                if p <= 0:
                    errors.append("Price must be greater than 0.")
            except ValueError:
                errors.append("Price must be a number.")

    return errors