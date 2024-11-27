# README

## TODO:
- [ ] Excel sheet for number of layers per block
- [ ] Excel sheet for sample architecture
- [ ] Satyajit target 6 epochs, 99.4% accuracy under 3.6K params


### Model Summary
```
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 10, 26, 26]              90
       BatchNorm2d-2           [-1, 10, 26, 26]              20
           Dropout-3           [-1, 10, 26, 26]               0
            Conv2d-4           [-1, 10, 24, 24]             900
       BatchNorm2d-5           [-1, 10, 24, 24]              20
           Dropout-6           [-1, 10, 24, 24]               0
            Conv2d-7           [-1, 10, 22, 22]             900
       BatchNorm2d-8           [-1, 10, 22, 22]              20
           Dropout-9           [-1, 10, 22, 22]               0
           Conv2d-10           [-1, 10, 20, 20]             900
      BatchNorm2d-11           [-1, 10, 20, 20]              20
           Conv2d-12           [-1, 10, 20, 20]             100
      BatchNorm2d-13           [-1, 10, 20, 20]              20
        MaxPool2d-14           [-1, 10, 10, 10]               0
           Conv2d-15             [-1, 14, 8, 8]           1,260
      BatchNorm2d-16             [-1, 14, 8, 8]              28
          Dropout-17             [-1, 14, 8, 8]               0
           Conv2d-18             [-1, 14, 6, 6]           1,764
      BatchNorm2d-19             [-1, 14, 6, 6]              28
          Dropout-20             [-1, 14, 6, 6]               0
           Conv2d-21             [-1, 13, 4, 4]           1,638
      BatchNorm2d-22             [-1, 13, 4, 4]              26
AdaptiveAvgPool2d-23             [-1, 13, 1, 1]               0
           Conv2d-24             [-1, 10, 1, 1]             130
      BatchNorm2d-25             [-1, 10, 1, 1]              20
================================================================
Total params: 7,884
Trainable params: 7,884
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 0.56
Params size (MB): 0.03
Estimated Total Size (MB): 0.60
----------------------------------------------------------------
```

### Training Logs
```
Epoch 1:
    Loss=0.2085336595773697 batch_id=468: 100%|██████████| 469/469 [01:03<00:00,  7.43it/s] 
    Test set: Average loss: 0.0904, Accuracy: 9825/10000 (98.25%)

Epoch 2:
    Loss=0.12635397911071777 batch_id=468: 100%|██████████| 469/469 [00:59<00:00,  7.84it/s] 
    Test set: Average loss: 0.0552, Accuracy: 9873/10000 (98.73%)

Epoch 3:
    Loss=0.08278200030326843 batch_id=468: 100%|██████████| 469/469 [01:03<00:00,  7.37it/s] 
    Test set: Average loss: 0.0436, Accuracy: 9882/10000 (98.82%)

Epoch 4:
    Loss=0.06628762185573578 batch_id=468: 100%|██████████| 469/469 [00:59<00:00,  7.85it/s] 
    Test set: Average loss: 0.0358, Accuracy: 9913/10000 (99.13%)

Epoch 5:
    Loss=0.04646427556872368 batch_id=468: 100%|██████████| 469/469 [01:00<00:00,  7.71it/s] 
    Test set: Average loss: 0.0403, Accuracy: 9891/10000 (98.91%)

Epoch 6:
    Loss=0.0820210725069046 batch_id=468: 100%|██████████| 469/469 [01:01<00:00,  7.64it/s]  
    Test set: Average loss: 0.0318, Accuracy: 9910/10000 (99.10%)

Epoch 7:
    Loss=0.0731586217880249 batch_id=468: 100%|██████████| 469/469 [01:07<00:00,  6.98it/s]  
    Test set: Average loss: 0.0336, Accuracy: 9907/10000 (99.07%)

Epoch 8:
    Loss=0.10490330308675766 batch_id=468: 100%|██████████| 469/469 [01:05<00:00,  7.12it/s] 
    Test set: Average loss: 0.0271, Accuracy: 9930/10000 (99.30%)

Epoch 9:
    Loss=0.05066375061869621 batch_id=468: 100%|██████████| 469/469 [01:05<00:00,  7.18it/s] 
    Test set: Average loss: 0.0316, Accuracy: 9911/10000 (99.11%)

Epoch 10:
    Loss=0.05262778699398041 batch_id=468: 100%|██████████| 469/469 [01:07<00:00,  6.94it/s] 
    Test set: Average loss: 0.0260, Accuracy: 9930/10000 (99.30%)

Epoch 11:
    Loss=0.011290161870419979 batch_id=468: 100%|██████████| 469/469 [01:06<00:00,  7.10it/s]
    Test set: Average loss: 0.0242, Accuracy: 9936/10000 (99.36%)

Epoch 12:
    Loss=0.11191428452730179 batch_id=468: 100%|██████████| 469/469 [01:06<00:00,  7.02it/s] 
    Test set: Average loss: 0.0286, Accuracy: 9922/10000 (99.22%)

Epoch 13:
    Loss=0.07382076978683472 batch_id=468: 100%|██████████| 469/469 [01:06<00:00,  7.04it/s] 
    Test set: Average loss: 0.0256, Accuracy: 9929/10000 (99.29%)

Epoch 14:
    Loss=0.03881983086466789 batch_id=468: 100%|██████████| 469/469 [01:05<00:00,  7.14it/s] 
    Test set: Average loss: 0.0242, Accuracy: 9926/10000 (99.26%)

Epoch 15:
    Loss=0.013535715639591217 batch_id=468: 100%|██████████| 469/469 [01:07<00:00,  6.92it/s]
    Test set: Average loss: 0.0264, Accuracy: 9927/10000 (99.27%)

Epoch 16:
    Loss=0.03432683274149895 batch_id=468: 100%|██████████| 469/469 [01:02<00:00,  7.48it/s] 
    Test set: Average loss: 0.0251, Accuracy: 9924/10000 (99.24%)

Epoch 17:
    Loss=0.032912593334913254 batch_id=468: 100%|██████████| 469/469 [01:04<00:00,  7.26it/s]
    Test set: Average loss: 0.0226, Accuracy: 9939/10000 (99.39%)

Epoch 18:
    Loss=0.05373332276940346 batch_id=468: 100%|██████████| 469/469 [01:07<00:00,  6.93it/s] 
    Test set: Average loss: 0.0256, Accuracy: 9916/10000 (99.16%)

Epoch 19:
    Loss=0.06821335107088089 batch_id=468: 100%|██████████| 469/469 [01:07<00:00,  6.98it/s] 
    Test set: Average loss: 0.0208, Accuracy: 9940/10000 (99.40%)

Epoch 20:
    Loss=0.06556873023509979 batch_id=468: 100%|██████████| 469/469 [01:06<00:00,  7.03it/s] 
    Test set: Average loss: 0.0239, Accuracy: 9938/10000 (99.38%)
```
