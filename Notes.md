## Regularization

### Label Smoothing: 

Solves: overfitting/overconfidence, 

```
y_ls = (1 - α) * y_hot + α / K
K - n_classes, α - smoothing coef.
```

* model outputs - softmax 
* cross entropy loss 

*Example:* 

*y_true=[1, 0, 0]* 

*logits=[10, 0, 0] -> **softmax** -> outputs=[0.99, 0, 0]*

***α=0.1** -> outputs=[0.93, 0.03, 0.03]*