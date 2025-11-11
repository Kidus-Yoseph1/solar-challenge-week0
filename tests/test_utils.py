import pandas as pd
import numpy as np
from src.app.utils import flag_outliers_by_zscore

def test_flag_outliers_by_zscore():
    # Create a sample DataFrame with a clear outlier
    data = {'A': [1, 2, 3, 4, 5, 100], 'B': [10, 20, 30, 40, 50, 60]}
    df = pd.DataFrame(data)

    # Apply the function
    df_with_outliers = flag_outliers_by_zscore(df, columns=['A'], threshold=2)

    # Check that the outlier is correctly flagged
    assert df_with_outliers['is_outlier'].iloc[5] == True

    # Check that non-outliers are not flagged
    assert df_with_outliers['is_outlier'].iloc[0:5].all() == False
