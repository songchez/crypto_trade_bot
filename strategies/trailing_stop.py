def trailing_stop_strategy(close, atr_window, atr_mult):
    """
    Trailing Stop Strategy:
    Generates buy and sell signals based on a trailing stop loss using ATR.

    Parameters:
    close (pd.Series): Series of closing prices.
    atr_window (int): Lookback period for ATR calculation.
    atr_mult (float): Multiplier for ATR to determine trailing stop distance.

    Returns:
    tuple: (entries, exits) where entries and exits are boolean Series indicating buy/sell signals.
    """
    # Calculate ATR as a proxy for volatility
    atr = close.rolling(atr_window).std() * atr_mult
    trailing_stop = close - atr

    # Buy when price is above trailing stop, sell when price is below trailing stop
    entries = close > trailing_stop
    exits = close < trailing_stop
    return entries, exits
