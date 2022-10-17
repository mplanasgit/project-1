def clean_na_dupl(df):
    '''This function drops rows with NaN in all columns as well as duplicated rows.
    '''
    print (f"Before cleaning shape is {df.shape}")
    df.dropna(axis=0, how="all", inplace = True)
    df.drop_duplicates(inplace = True)
    print (f"After cleaning shape is {df.shape}")



