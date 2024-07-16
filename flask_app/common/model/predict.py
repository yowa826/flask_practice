import torch

def preprocessing(data):
    return data


def get_prediction(data):
    outputs = model.forward(data)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]
