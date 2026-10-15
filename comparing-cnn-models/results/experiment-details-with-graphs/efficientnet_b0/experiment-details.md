##### Experiment 1

1. label smoothing 0.1
2. class weights used
3. learning rate 0.001
4. weight decay 0.01
5. lr schedular CosineAnnealingWarmRestarts
6. optimizer AdamW

- epochs given - 20
- epochs completed - 13
- model final accuracy - 0.707021

![alt text](./graphs/experiment-1-accuracy.png)
![alt text](./graphs/experiment-1-loss.png)


##### Experiment 2 (metric decreased)

Increase the learning rate to 0.01 

1. label smoothing 0.1
2. class weights used
3. learning rate 0.01 -- changed
4. weight decay 0.01
5. lr schedular ReduceLROnPlateau
6. optimizer AdamW

- epochs given - 20
- epochs completed 8
- model final accuracy - 0.68138

![alt text](./graphs/experiment-2-accuracy.png)
![alt text](./graphs/experiment-2-loss.png)


##### experiment 3

changed optimizer to ReduceLROnPlateau

1. label smoothing 0.1
2. class weights used
3. learning rate 0.001
4. weight decay 0.01
5. lr schedular ReduceLROnPlateau -- changed
6. optimizer AdamW

- epochs given - 20
- epochs completed 5
- model final accuracy - 0.67679

![alt text](./graphs/experiment-3-accuracy.png)
![alt text](./graphs/experiment-3-loss.png)


##### Experiment 4

decrease the learning rate to 0.0005, schedular changed to CosineAnnealingWarmRestarts as in experiment 1

1. label smoothing 0.1
2. class weights used
3. learning rate 0.0005 -- changed
4. weight decay 0.01
5. lr schedular CosineAnnealingWarmRestarts
6. optimizer AdamW

- epochs given - 20
- epochs completed 6
- model final accuracy - 0.6985

![alt text](./graphs/experiment-4-accuracy.png)
![alt text](./graphs/experiment-4-loss.png)


##### Experiment 5

try timm RandAugment. In the default `train_transform` at top added this:

rand_augment_transform(
    config_str='rand-m4-mstd0.25',
    # hparams={'translate_const': 117, 'img_mean': (124, 116, 104)}
    )

see timm implementation here
https://timm.fast.ai/RandAugment#rand_augment_transform

transform pipeline
[transform pipeline](comparing-cnn-models/results/experiment-details-with-graphs/efficientnet_b0/transforms/experiment-5.py)

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
5. lr schedular CosineAnnealingLR
6. optimizer AdamW

- epochs given - 20
- epochs completed - 14
- model final accuracy - 0.6990

![alt text](./graphs/experiment-5-accuracy.png)
![alt text](./graphs/experiment-5-loss.png)


##### Experiment 6

try timm AutoAugment and RandomResizedCropAndInterpolation augumentation pipeline

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
5. lr schedular CosineAnnealingLR
6. optimizer AdamW

transform pipeline
[transform pipeline](comparing-cnn-models/results/experiment-details-with-graphs/efficientnet_b0/transforms/experiment-6.py)

- epochs given - 20
- epochs completed - 5
- model final accuracy - 0.7085

![alt text](./graphs/experiment-6-accuracy.png)
![alt text](./graphs/experiment-6-loss.png)


##### Experiment 7

randugument with batch size 64

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
5. lr schedular CosineAnnealingLR
6. optimizer AdamW


transform pipeline
[transform pipeline](comparing-cnn-models/results/experiment-details-with-graphs/efficientnet_b0/transforms/experiment-7.py)

- epochs given - 20
- epochs completed - 5
- model final accuracy - 0.7120

![alt text](./graphs/experiment-7-accuracy.png)
![alt text](./graphs/experiment-7-loss.png)


##### Experiment 8

randugument with batch size 64 -- increase the magnitude of random augumentation

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
5. lr schedular CosineAnnealingLR
6. optimizer AdamW

transform pipeline
[transform pipeline](comparing-cnn-models/results/experiment-details-with-graphs/efficientnet_b0/transforms/experiment-8.py)

- epochs given - 20
- epochs completed - 6
- model final accuracy -  0.718584

![alt text](./graphs/experiment-8-accuracy.png)
![alt text](./graphs/experiment-8-loss.png)


##### Experiment 9

keep the batch size 64 and use another custom transform

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
5. lr schedular CosineAnnealingWarmRestarts
6. optimizer AdamW

transform pipeline
[transform pipeline](comparing-cnn-models/results/experiment-details-with-graphs/efficientnet_b0/transforms/experiment-9.py)

- epochs given - 20
- epochs completed - 8
- model final accuracy -  0.7063248

![alt text](./graphs/experiment-9-accuracy.png)
![alt text](./graphs/experiment-9-loss.png)


##### Experiment 10

keep the batch size 64 and use another more stronger custom transform

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
5. lr schedular CosineAnnealingWarmRestarts
6. optimizer AdamW

transform pipeline
[transform pipeline](comparing-cnn-models/results/experiment-details-with-graphs/efficientnet_b0/transforms/experiment-10.py)

- epochs given - 20
- epochs completed - 8
- model final accuracy -  0.7167734

![alt text](./graphs/experiment-10-accuracy.png)
![alt text](./graphs/experiment-10-loss.png)


##### Experiment 11

Use light variant of transform `train_transform_aug_6` and use class balancing
keep the batch size 64

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
5. lr schedular CosineAnnealingWarmRestarts
6. optimizer AdamW

well use `torchsampler` for class balancing

- epochs given - 20
- epochs completed - 9
- model final accuracy -  0.713151

![alt text](./graphs/experiment-11-accuracy.png)
![alt text](./graphs/experiment-11-loss.png)






