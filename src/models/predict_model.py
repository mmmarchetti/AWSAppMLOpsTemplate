import joblib
import boto3
import numpy as np
from io import BytesIO


def predict_model(features):
    """"
    Example Predict model
    :param house: HouseFeatures
    return: prediction
    """
    # Define model file
    bucket_name = 'ml-sample-trained-models'
    model_file_name = 'iris_model.pkl'

    # Download model from S3 to BytesIO object
    s3 = boto3.client('s3')
    model_file = BytesIO()
    s3.download_fileobj(bucket_name, model_file_name, model_file)
    model_file.seek(0)

    # Load model
    model = joblib.load(model_file)

    # Predict
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction