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
    # 원래 컬럼 = high,AATN 이런식 첫번째 인덱스만 불러옴
    df.columns = df.columns.get_level_values(0)
    
    # Ensure necessary columns exist
    if not {'High', 'Low', 'Close'}.issubset(df.columns):
        raise ValueError("Input DataFrame must contain 'High', 'Low', and 'Close' columns.")
    
    # RSI calculation
    delta = df['Close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=rsi_period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=rsi_period).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # MACD calculation
    ema_fast = df['Close'].ewm(span=macd_fast, adjust=False).mean()
    ema_slow = df['Close'].ewm(span=macd_slow, adjust=False).mean()
    df['MACD'] = ema_fast - ema_slow
    df['MACD_Signal'] = df['MACD'].ewm(span=macd_signal, adjust=False).mean()

    # Stochastic calculation
    df['%K'] = 100 * ((df['Close'] - df['Low'].rolling(window=stochastic_k).min()) / (df['High'].rolling(window=stochastic_k).max() - df['Low'].rolling(window=stochastic_k).min()))
    df['%D'] = df['%K'].rolling(window=stochastic_d).mean()

    # Buy Signal: Stochastic < 20, RSI crosses above 50, MACD > Signal
    entries = (df['%K'] < 20) & (df['RSI'] > 50) & (df['RSI'].shift(1) <= 50) & (df['MACD'] > df['MACD_Signal'])

    # Sell Signal: Stochastic > 80, RSI crosses below 50, MACD < Signal
    exits = (df['%K'] > 80) & (df['RSI'] < 50) & (df['RSI'].shift(1) >= 50) & (df['MACD'] < df['MACD_Signal'])

    # Drop intermediate columns to clean up
    df.drop(columns=['RSI', 'MACD', 'MACD_Signal', '%K', '%D'], inplace=True)

    return entries, exits