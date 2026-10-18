##### Experiment 1

1. label smoothing 0.1
2. class weights used
3. learning rate 0.001
4. weight decay 0.01
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW 
![alt text](./graphs/experiment-1-accuracy.png)
![alt text](./graphs/experiment-1-loss.png)

##### Experiment 2 (metric didnot improve)

we'll use same setup for 5 more because accuracy increased each epoch consistently 

1. label smoothing 0.1
2. class weights used
3. learning rate 0.001
4. weight decay 0.01
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW 

![alt text](./graphs/experiment-2-accuracy.png)
![alt text](./graphs/experiment-2-loss.png)


##### Experiment 3 (metric improved)
chnage learning rate schedular from CosineAnnealingWarmRestarts to ReduceLROnPlateau and removed class weights in loss function

1. label smoothing 0.1 
2. class weights not used
3. learning rate 0.001
4. weight decay 0.01
4. lr schedular ReduceLROnPlateau
5. optimizer AdamW 

![alt text](./graphs/experiment-3-accuracy.png)
![alt text](./graphs/experiment-3-loss.png)


##### Experiment 4 (early stopping - metric not improved)
we'll use same setup of eperiment 3 for 10 more epochs because accuracy increased each epoch consistently

1. label smoothing 0.1
2. class weights not used
3. learning rate 0.001
4. weight decay 0.01
4. lr schedular ReduceLROnPlateau
5. optimizer AdamW 

![alt text](./graphs/experiment-4-accuracy.png)
![alt text](./graphs/experiment-4-loss.png)


##### Experiment 5
just changed learning rate to 0.1 and rest use same setup of eperiment 3, 4 

1. label smoothing 0.1
2. class weights not used
3. learning rate 0.01
4. weight decay 0.01
4. lr schedular ReduceLROnPlateau
5. optimizer AdamW

![alt text](./graphs/experiment-5-accuracy.png)
![alt text](./graphs/experiment-5-loss.png)


##### Experiment 6

randugument with batch size 64 -- increase augumentation. use `torchsampler` for class balancing

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

- epochs given 20
- epochs completed - 9
- model final accuracy -  0.67205

![alt text](./graphs/experiment-6-accuracy.png)
![alt text](./graphs/experiment-6-loss.png)


##### Experiment 7

batch size 64 -- make augumentation lighter. use `torchsampler` for class balancing

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

- epochs given 20
- epochs completed - 10
- model final accuracy - 0.6748397

![alt text](./graphs/experiment-7-accuracy.png)
![alt text](./graphs/experiment-7-loss.png)


##### Experiment 8

batch size 64 -- use `train_transform` (augumentation given at top). use `torchsampler` for class balancing

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingWarmRestarts
5. optimizer AdamW

- epochs given 20
- epochs completed - 11
- model final accuracy - 0.68932

![alt text](./graphs/experiment-8-accuracy.png)
![alt text](./graphs/experiment-8-loss.png)
