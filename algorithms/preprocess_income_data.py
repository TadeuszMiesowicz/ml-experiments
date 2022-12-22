import pandas as pd
import re
from get_val_size import get_val_size
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer


def create_train_test_df():
    with open('../ds/adult.names') as fp:
        cols = [sre.group('colname') for line in fp
                if (sre := re.match(r'(?P<colname>[a-z\-]+):.*\.', line))]
        cols.append('label')

    options = {'header': None, 'names': cols, 'skipinitialspace': True}

    train_df = pd.read_csv('../ds/adult.data', **options)

    test_df = pd.read_csv('../ds/adult.test', skiprows=1, **options)
    test_df['label'] = test_df['label'].str.rstrip('.')

    return train_df, test_df


def preprocess_data():
    train_df, test_df = create_train_test_df()

    VAL_SET_SIZE = get_val_size(test_df)

    le = LabelEncoder()

    y_train_str = train_df["label"]

    le.fit(y_train_str)

    y_train = le.transform(y_train_str)

    y_test_str = test_df.iloc[:VAL_SET_SIZE, :]["label"]

    y_val_str = test_df.iloc[VAL_SET_SIZE:, :]["label"]

    y_test = le.transform(y_test_str)

    y_val = le.transform(y_val_str)

    X_train = train_df.drop("label", axis=1)
    X_test = test_df.iloc[:VAL_SET_SIZE, :].drop('label', axis=1)
    X_val = test_df.iloc[VAL_SET_SIZE:, :].drop('label', axis=1)

    categorical_features = [
        'workclass',
        'education',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'native-country'
    ]
    continuous_features = [
        'age',
        'fnlwgt',
        'education-num',  # according to dataset description this is continuous
        'capital-gain',
        'capital-loss',
        'hours-per-week'
    ]

    ohe = OneHotEncoder(handle_unknown='ignore', sparse=False)
    scaler = StandardScaler()

    ct = ColumnTransformer([
        ('ohe_ct', ohe, categorical_features),
        ('scaler_ct', scaler, continuous_features)

    ], remainder='passthrough')

    ct.fit(X_train)

    X_train = ct.transform(X_train)
    X_test = ct.transform(X_test)
    X_val = ct.transform(X_val)

    return X_train, X_test, X_val, y_train, y_val, y_test
