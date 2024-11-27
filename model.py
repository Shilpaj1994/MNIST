#! /usr/bin/env python3
"""
Model for MNIST classification
"""

import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    """
    Model for MNIST classification
    """
    def __init__(self):
        """
        Initialize the model
        """
        super(Net, self).__init__()

        # Convolutional Block 1 Layers
        self.conv1 = nn.Conv2d(1, 10, 3, padding=0, bias=False)       # 28 > 26 | 3
        self.batch_norm1 = nn.BatchNorm2d(10)
        self.conv2 = nn.Conv2d(10, 10, 3, padding=0, bias=False)      # 26 > 24 | 5
        self.batch_norm2 = nn.BatchNorm2d(10)
        self.conv3 = nn.Conv2d(10, 10, 3, padding=0, bias=False)      # 24 > 22 | 7
        self.batch_norm3 = nn.BatchNorm2d(10)
        self.conv4 = nn.Conv2d(10, 10, 3, padding=0, bias=False)      # 22 > 20 | 9
        self.batch_norm4 = nn.BatchNorm2d(10)

        # Transition Block Layers
        self.point1 = nn.Conv2d(10, 10, 1, padding=0, bias=False)     # 20 > 20 | 9
        self.batch_normp1 = nn.BatchNorm2d(10)
        self.pool1 = nn.MaxPool2d(2, 2)                               # 20 > 10 | 10

        # Convolutional Block 2 Layers
        self.conv5 = nn.Conv2d(10, 14, 3, padding=0, bias=False)      # 10 > 8 | 14
        self.batch_norm5 = nn.BatchNorm2d(14)
        self.conv6 = nn.Conv2d(14, 14, 3, padding=0, bias=False)      #  8 > 6 | 18
        self.batch_norm6 = nn.BatchNorm2d(14)
        self.conv7 = nn.Conv2d(14, 13, 3, padding=0, bias=False)      #  6 > 4 | 22
        self.batch_norm7 = nn.BatchNorm2d(13)

        # Global Average Pooling Layer
        self.gap = nn.AdaptiveAvgPool2d(1)                            # 4 > 1 | 28

        # Transition Block 2 Layers
        self.point2 = nn.Conv2d(13, 10, 1, padding=0, bias=False)     # 1 > 1 | 28
        self.batch_normp2 = nn.BatchNorm2d(10)

        # Dropout Layer
        self.dropout = nn.Dropout(0.05)

    def forward(self, x):
        """
        Forward pass
        """
        # Convolutional Block 1
        x = self.dropout(F.relu(self.batch_norm1(self.conv1(x))))
        x = self.dropout(F.relu(self.batch_norm2(self.conv2(x))))
        x = self.dropout(F.relu(self.batch_norm3(self.conv3(x))))
        x = self.batch_norm4(self.conv4(x))

        # Transition Block 1
        x = self.pool1(self.batch_normp1(self.point1(x)))

        # Convolutional Block 2
        x = self.dropout(F.relu(self.batch_norm5(self.conv5(x))))
        x = self.dropout(F.relu(self.batch_norm6(self.conv6(x))))
        x = self.batch_norm7(self.conv7(x))

        # Global Average Pooling
        x = self.gap(x)

        # Transition Block 2
        x = self.batch_normp2(self.point2(x))

        # Flatten
        x = x.view(-1, 10)                                             # 1x1x10 > 10

        # Softmax
        return F.log_softmax(x, dim=-1)