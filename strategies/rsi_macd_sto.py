# RSI & MACD & STOCHASTIC 돌파 전략 (단기용)
def rsi_macd_stochastic_strategy(df, rsi_period=14, macd_fast=12, macd_slow=26, macd_signal=9, stochastic_k=14, stochastic_d=3):
    """
    Calculate buy/sell signals based on RSI, MACD, and Stochastic indicators.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'High', 'Low', and 'Close' price columns.
    rsi_period (int): Period for RSI calculation.
    macd_fast (int): Fast EMA period for MACD.
    macd_slow (int): Slow EMA period for MACD.
    macd_signal (int): Signal line EMA period for MACD.
    stochastic_k (int): Stochastic %K period.
    stochastic_d (int): Stochastic %D period.

    Returns:
    tuple: (entries, exits) where entries and exits are boolean Series indicating buy/sell signals.
    """
    
    # RSI calculation
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)
    avg_gain = gain.rolling(window=rsi_period, min_periods=1).mean()
    avg_loss = loss.rolling(window=rsi_period, min_periods=1).mean()
    rs = avg_gain / avg_loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # MACD calculation
    ema_fast = df['Close'].ewm(span=macd_fast, adjust=False).mean()
    ema_slow = df['Close'].ewm(span=macd_slow, adjust=False).mean()
    df['MACD'] = ema_fast - ema_slow
    df['MACD_Signal'] = df['MACD'].ewm(span=macd_signal, adjust=False).mean()

    # Stochastic Oscillator calculation
    lowest_low = df['Low'].rolling(window=stochastic_k, min_periods=1).min()
    highest_high = df['High'].rolling(window=stochastic_k, min_periods=1).max()
    df['%K'] = 100 * ((df['Close'] - lowest_low) / (highest_high - lowest_low))
    df['%D'] = df['%K'].rolling(window=stochastic_d, min_periods=1).mean()

    # Buy Signal: MACD line crosses above Signal line, RSI > 50, and %K > 50
    entries = (
        (df['MACD'] > df['MACD_Signal']) & 
        (df['MACD'].shift(1) <= df['MACD_Signal'].shift(1)) & 
        (df['RSI'] > 50) & 
        (df['%K'] > 50)
    )

    # Sell Signal: MACD line crosses below Signal line, RSI < 50, and %K < 50
    exits = (
        (df['MACD'] < df['MACD_Signal']) & 
        (df['MACD'].shift(1) >= df['MACD_Signal'].shift(1)) & 
        (df['RSI'] < 50) & 
        (df['%K'] < 50)
    )

    # Drop intermediate columns to clean up
    df.drop(columns=['RSI', 'MACD', 'MACD_Signal', '%K', '%D'], inplace=True)

    return entries, exits
