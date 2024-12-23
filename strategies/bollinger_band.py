def bollinger_band_strategy(close, window, std_dev):
    """
    Bollinger Band Strategy:
    Calculate buy and sell signals based on price crossing Bollinger Bands.

    Parameters:
    close (pd.Series): Series of closing prices.
    window (int): Lookback period for the moving average.
    std_dev (float): Number of standard deviations for band calculation.

    Returns:
    tuple: (entries, exits) where entries and exits are boolean Series indicating buy/sell signals.
    """
    mean = close.rolling(window).mean()
    std = close.rolling(window).std()
    upper_band = mean + std_dev * std
    lower_band = mean - std_dev * std

    entries = close > upper_band  # Signal to enter a long position
    exits = close < lower_band   # Signal to exit a long position
    return entries, exits
