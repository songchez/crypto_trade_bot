import numpy as np
import pandas as pd

# 수퍼트렌드 전략
def supertrend(df, atr_period=10, multiplier=3):
    """
    Calculate the SuperTrend indicator.

    Parameters:
    df (pd.DataFrame): DataFrame containing 'High', 'Low', and 'Close' price columns.
    atr_period (int): Period for ATR calculation.
    multiplier (float): Multiplier for ATR to set the bands.

    Returns:
    tuple: (entries, exits) where entries and exits are boolean Series indicating buy/sell signals.
    """
    # 원래 컬럼 = high,AATN 이런식 첫번째 인덱스만 불러옴
    df.columns = df.columns.get_level_values(0)

    if not {'High', 'Low', 'Close'}.issubset(df.columns):
        raise ValueError("Input DataFrame must contain 'High', 'Low', and 'Close' columns.")
    
    # Calculate ATR
    df['TR'] = np.maximum(
        df['High'] - df['Low'],
        np.maximum(
            abs(df['High'] - df['Close'].shift(1)),
            abs(df['Low'] - df['Close'].shift(1))
        )
    )
    df['ATR'] = df['TR'].rolling(atr_period).mean()

    # Calculate upper and lower bands
    hl2 = (df['High'] + df['Low']) / 2
    df['Upper Band'] = hl2 + (multiplier * df['ATR'])
    df['Lower Band'] = hl2 - (multiplier * df['ATR'])

    # Initialize SuperTrend direction and values
    direction = pd.Series(0, index=df.index)  # 1 for uptrend, -1 for downtrend

    for i in range(1, len(df)):
        # Adjust bands based on direction
        if df['Close'].iloc[i] > df['Upper Band'].iloc[i-1]:
            direction.iloc[i] = 1  # Uptrend
        elif df['Close'].iloc[i] < df['Lower Band'].iloc[i-1]:
            direction.iloc[i] = -1  # Downtrend
        else:
            direction.iloc[i] = direction.iloc[i-1]

    # Generate entries and exits based on direction changes
    entries = (direction.shift(1) == -1) & (direction == 1)
    exits = (direction.shift(1) == 1) & (direction == -1)

    # Drop intermediate columns to clean up
    df.drop(columns=['TR', 'ATR', 'Upper Band', 'Lower Band'], inplace=True)

    return entries, exits