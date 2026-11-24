#### Experiment 0


1. label smoothing 0.1
2. class weights not used
3. learning rate 0.001
4. weight decay
4. lr schedular CosineAnnealingLR
5. optimizer AdamW
6. standard transform (32 batch size)

- epochs given - 20
- epochs completed 9
- model final accuracy - 0.700055725

![alt text](./graphs/experiment-0-accuracy.png)
![alt text](./graphs/experiment-0-loss.png)


#### Experiment 1

stronger augumentation, batch size 128

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingLR
5. optimizer AdamW
6. 6. standard transform (32 batch size)

- epochs given - 20
- epochs completed 12
- model final accuracy - 0.713708

![alt text](./graphs/experiment-1-accuracy.png)
![alt text](./graphs/experiment-1-loss.png)


#### Experiment 2

stronger augumentation, batch size 96 with torchsampler for clas balancing

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingLR
5. optimizer AdamW
6.  strong transform 

- epochs given - 20
- epochs completed 9
- model final accuracy - 0.713708

![alt text](./graphs/experiment-2-accuracy.png)
![alt text](./graphs/experiment-2-loss.png)


#### Experiment 3

repeat experiment 2

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingLR
5. optimizer AdamW
6.  strong transform 

Run the train function twice 

- epochs given - 20 + 20
- epochs completed 6 + 6
- model final accuracy - 0.713708

![alt text](./graphs/experiment-3-accuracy.png)
![alt text](./graphs/experiment-3-loss.png)


#### Experiment 4

batch size 128

1. label smoothing 0.1
2. class weights not used
3. learning rate 3e-4
4. weight decay 1e-4
4. lr schedular CosineAnnealingLR
5. optimizer AdamW
6.  strong transform 

- epochs given - 20 
- epochs completed 8
- model final accuracy - 0.700473

![alt text](./graphs/experiment-4-accuracy.png)
![alt text](./graphs/experiment-4-loss.png)


#### Experiment 5

batch size 192, oneCycleLR schedular

1. label smoothing 0.1
2. class weights not used
4. lr schedular oneCycleLR
5. optimizer AdamW
6.  strong transform 

- epochs given - 20 
- epochs completed 19
- model final accuracy - 0.71593758

![alt text](./graphs/experiment-5-accuracy.png)
![alt text](./graphs/experiment-5-loss.png)


#### Experiment 6

 Use light transform and batch size 128

1. label smoothing 0.1
2. class weights not used
4. lr schedular oneCycleLR
5. optimizer AdamW
6. light transform 

- epochs given - 20 
- epochs completed - 19
- model final accuracy - 0.72666

![alt text](./graphs/experiment-6-accuracy.png)
![alt text](./graphs/experiment-6-loss.png)


#### Experiment 7

repeat experiment 6

1. label smoothing 0.1
2. class weights not used
4. lr schedular oneCycleLR
5. optimizer AdamW
6. light transform 

- epochs given - 20 
- epochs completed - 19
- model final accuracy - 0.7293117

![alt text](./graphs/experiment-7-accuracy.png)
![alt text](./graphs/experiment-7-loss.png)


#### Experiment 8

1. label smoothing 0.1
2. class weights not used
4. lr schedular oneCycleLR
5. optimizer AdamW
6. batch size 192
7. light transform 

- epochs given - 20 
- epochs completed - 19
- model final accuracy -0.731540

![alt text](./graphs/experiment-8-accuracy.png)
![alt text](./graphs/experiment-8-loss.png)


#### Experiment 9

batch size 512

1. label smoothing 0.1
2. class weights not used
4. lr schedular oneCycleLR
5. optimizer AdamW
7. light transform 

- epochs given - 20 
- epochs completed - 19
- model final accuracy - 0.7304

![alt text](./graphs/experiment-9-accuracy.png)
![alt text](./graphs/experiment-9-loss.png)
