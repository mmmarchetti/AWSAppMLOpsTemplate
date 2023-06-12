from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib
import boto3
from io import BytesIO


mlflow.set_tracking_uri("http://ec2-52-207-53-82.compute-1.amazonaws.com")


def load_data():
    """"
    Example Load data

    :return: X_train, X_test, y_train, y_test
    """
     # Load iris dataset
    iris = load_iris()

    # Split dataset into train and test

    return train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)


def train_model():
    """"
    Example Train model

    :return: score
    """
    X_train, X_test, y_train, y_test = load_data()

    # Define model
    model = LogisticRegression()

    # Train model
    model.fit(X_train, y_train)

    # Save model to BytesIO object
    model_file = BytesIO()
    joblib.dump(model, model_file)
    model_file.seek(0)

    # Upload model to S3
    s3 = boto3.client('s3')
    bucket_name = 'ml-sample-trained-models'
    s3.upload_fileobj(model_file, bucket_name, 'iris_model.pkl')

    return model.score(X_test, y_test)
