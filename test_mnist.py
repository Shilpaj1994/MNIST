#! /usr/bin/env python3
"""
Test for the model
"""
import torch.nn as nn
from model import Net


def count_parameters(model):
    """
    Helper function to count the total parameters in the model
    """
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


def has_batchnorm(model):
    """
    Helper function to check if model uses batch normalization
    """
    for module in model.modules():
        if isinstance(module, (nn.BatchNorm1d, nn.BatchNorm2d, nn.BatchNorm3d)):
            return True
    return False


def has_dropout(model):
    """
    Helper function to check if model uses dropout
    """
    for module in model.modules():
        if isinstance(module, nn.Dropout) or isinstance(module, nn.Dropout2d):
            return True
    return False


def has_fc_or_gap(model):
    """
    Helper function to check if model uses FC layer or Global Average Pooling
    """
    has_fc = any(isinstance(module, nn.Linear) for module in model.modules())
    # Check for GAP-like operations in forward method
    has_gap = hasattr(model, 'forward') and 'AdaptiveAvgPool2d' in str(model.forward)
    return has_fc or has_gap


def test_parameter_count():
    """
    Test that model has less than 20k parameters
    """
    model = Net()
    param_count = count_parameters(model)
    assert param_count < 20000, f"Model has {param_count} parameters, which exceeds the limit of 20,000"


def test_batch_normalization():
    """
    Test that model uses batch normalization
    """
    model = Net()
    assert has_batchnorm(model), "Model does not use batch normalization"


def test_dropout():
    """
    Test that model uses dropout
    """
    model = Net()
    assert has_dropout(model), "Model does not use dropout"


def test_fc_or_gap():
    """
    Test that model uses either fully connected layer or global average pooling
    """
    model = Net()
    assert has_fc_or_gap(model), "Model does not use either fully connected layer or global average pooling"
