
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(df, target):
    X = df.drop(columns=[target])
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model
