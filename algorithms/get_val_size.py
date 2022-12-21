from const import TEST_VAL_SPLIT

def get_val_size(test_df):
    return int(len(test_df) * TEST_VAL_SPLIT)