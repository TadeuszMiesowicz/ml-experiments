from const import TEST_VAL_SPLIT

def get_val_size(test_df):
    """Get size of validation set from test dataset size

    Args:
        test_df (DataFrame): test dataset

    Returns:
        Int
    """    
    return int(len(test_df) * TEST_VAL_SPLIT)