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
    Loss=0.28947052359580994 batch_id=937: 100%|██████████| 938/938 [01:08<00:00, 13.63it/s]
    Test set: Average loss: 0.0776, Accuracy: 9803/10000 (98.03%)

Epoch 2:
    Loss=0.07014646381139755 batch_id=937: 100%|██████████| 938/938 [01:09<00:00, 13.43it/s] 
    Test set: Average loss: 0.0489, Accuracy: 9872/10000 (98.72%)

Epoch 3:
    Loss=0.2854246497154236 batch_id=937: 100%|██████████| 938/938 [01:09<00:00, 13.48it/s]  
    Test set: Average loss: 0.0375, Accuracy: 9897/10000 (98.97%)

Epoch 4:
    Loss=0.0366009958088398 batch_id=937: 100%|██████████| 938/938 [01:09<00:00, 13.46it/s]  
    Test set: Average loss: 0.0330, Accuracy: 9901/10000 (99.01%)

Epoch 5:
    Loss=0.06880800426006317 batch_id=937: 100%|██████████| 938/938 [01:09<00:00, 13.59it/s] 
    Test set: Average loss: 0.0305, Accuracy: 9909/10000 (99.09%)

Epoch 6:
    Loss=0.03607328608632088 batch_id=937: 100%|██████████| 938/938 [01:10<00:00, 13.39it/s] 
    Test set: Average loss: 0.0343, Accuracy: 9912/10000 (99.12%)

Epoch 7:
    Loss=0.057786960154771805 batch_id=937: 100%|██████████| 938/938 [01:09<00:00, 13.44it/s] 
    Test set: Average loss: 0.0282, Accuracy: 9916/10000 (99.16%)

Epoch 8:
    Loss=0.07292156666517258 batch_id=937: 100%|██████████| 938/938 [01:11<00:00, 13.20it/s]  
    Test set: Average loss: 0.0259, Accuracy: 9925/10000 (99.25%)

Epoch 9:
    Loss=0.04495275393128395 batch_id=937: 100%|██████████| 938/938 [01:11<00:00, 13.06it/s]  
    Test set: Average loss: 0.0261, Accuracy: 9918/10000 (99.18%)

Epoch 10:
    Loss=0.14885707199573517 batch_id=937: 100%|██████████| 938/938 [01:10<00:00, 13.31it/s]  
    Test set: Average loss: 0.0248, Accuracy: 9921/10000 (99.21%)

Epoch 11:
    Loss=0.24523553252220154 batch_id=937: 100%|██████████| 938/938 [01:08<00:00, 13.62it/s]  
    Test set: Average loss: 0.0246, Accuracy: 9923/10000 (99.23%)

Epoch 12:
    Loss=0.11862791329622269 batch_id=937: 100%|██████████| 938/938 [01:07<00:00, 13.88it/s]  
    Test set: Average loss: 0.0264, Accuracy: 9922/10000 (99.22%)

Epoch 13:
    Loss=0.01858886145055294 batch_id=937: 100%|██████████| 938/938 [01:05<00:00, 14.37it/s]  
    Test set: Average loss: 0.0224, Accuracy: 9920/10000 (99.20%)

Epoch 14:
    Loss=0.0641234964132309 batch_id=937: 100%|██████████| 938/938 [01:01<00:00, 15.20it/s]   
    Test set: Average loss: 0.0205, Accuracy: 9932/10000 (99.32%)

Epoch 15:
    Loss=0.031853724271059036 batch_id=937: 100%|██████████| 938/938 [01:03<00:00, 14.80it/s] 
    Test set: Average loss: 0.0230, Accuracy: 9924/10000 (99.24%)

Epoch 16:
    Loss=0.09746672958135605 batch_id=937: 100%|██████████| 938/938 [01:05<00:00, 14.26it/s]  
    Test set: Average loss: 0.0219, Accuracy: 9932/10000 (99.32%)

Epoch 17:
    Loss=0.06531140208244324 batch_id=937: 100%|██████████| 938/938 [01:01<00:00, 15.27it/s]  
    Test set: Average loss: 0.0200, Accuracy: 9941/10000 (99.41%)

Epoch 18:
    Loss=0.05266764760017395 batch_id=937: 100%|██████████| 938/938 [01:01<00:00, 15.37it/s]  
    Test set: Average loss: 0.0241, Accuracy: 9922/10000 (99.22%)

Epoch 19:
    Loss=0.02180585078895092 batch_id=937: 100%|██████████| 938/938 [01:00<00:00, 15.46it/s]  
    Test set: Average loss: 0.0220, Accuracy: 9938/10000 (99.38%)

Epoch 20:
    Loss=0.0489509217441082 batch_id=937: 100%|██████████| 938/938 [01:00<00:00, 15.49it/s]   
    Test set: Average loss: 0.0196, Accuracy: 9943/10000 (99.43%)