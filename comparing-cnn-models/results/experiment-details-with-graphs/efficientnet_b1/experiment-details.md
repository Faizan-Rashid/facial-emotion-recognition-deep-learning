##### Experiment 1

1. label smoothing 0.1
2. class weights used
3. learning rate 0.001
4. weight decay 0.01
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

- epochs given 20
- epochs completed - 11
- model final accuracy - 0.70897 

![alt text](./graphs/experiment-1-accuracy.png)
![alt text](./graphs/experiment-1-loss.png)


##### Experiment 2

deccrease the learning rate to 0.0005

1. label smoothing 0.1
2. class weights used
3. learning rate 0.0005 -- changed
4. weight decay 0.01
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

- epochs given 20
- epochs completed - 5
- model final accuracy - 0.675675

![alt text](./graphs/experiment-2-accuracy.png)
![alt text](./graphs/experiment-2-loss.png)


##### experiment 3

changed optimizer to ReduceLROnPlateau

1. label smoothing 0.1
2. class weights used
3. learning rate 0.001
4. weight decay 0.01
4. lr schedular ReduceLROnPlateau -- changed
5. optimizer AdamW

- epochs given 20
- epochs completed - 6
- model final accuracy - 0.700195

![alt text](./graphs/experiment-3-accuracy.png)
![alt text](./graphs/experiment-3-loss.png)


##### experiment 4

remove class weights and change label smoothing

1. label smoothing 0.15 -- changed
2. class weights not used -- changed
3. learning rate 0.0005 -- changed
4. weight decay 0.001 -- changed
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

- epochs given 20
- epochs completed - 7
- model final accuracy - 0.7144051 

![alt text](./graphs/experiment-4-accuracy.png)
![alt text](./graphs/experiment-4-loss.png)


##### experiment 5

we'll repeat the experiment 4

1. label smoothing 0.15 -- changed
2. class weights not used -- changed
3. learning rate 0.0005 -- changed
4. weight decay 0.001 -- changed
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

- epochs given 20
- epochs completed - 4
- model final accuracy - 0.72387

![alt text](./graphs/experiment-5-accuracy.png)
![alt text](./graphs/experiment-5-loss.png)


##### Experiment 6

randugument with batch size 64 -- increase the magnitude of random augumentation

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingLR
5. optimizer AdamW

- epochs given 20
- epochs completed - 12
- model final accuracy - 0.7100

![alt text](./graphs/experiment-6-accuracy.png)
![alt text](./graphs/experiment-6-loss.png)


##### Experiment 7

Use class balancing via `torchsampler` along with `train_transform_aug_1` data loader 
keep the batch size 64

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

well use `torchsampler` for class balancing

- epochs given 20
- epochs completed - 11
- model final accuracy - 0.70674

![alt text](./graphs/experiment-7-accuracy.png)
![alt text](./graphs/experiment-7-loss.png)


##### Experiment 8

Add class weights

1. label smoothing 0.1
2. class weights used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

well use `torchsampler` for class balancing

- epochs given 20
- epochs completed - 7
- model final accuracy - 0.6996377

![alt text](./graphs/experiment-8-accuracy.png)
![alt text](./graphs/experiment-8-loss.png)


##### Experiment 9

change the scheduler to ReduceLROnPleatue
1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular ReduceLROnPleatue
5. optimizer AdamW

- epochs given 20
- epochs completed - 13
- model final accuracy - 0.709807

![alt text](./graphs/experiment-9-accuracy.png)
![alt text](./graphs/experiment-9-loss.png)