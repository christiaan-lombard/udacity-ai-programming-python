# Neural Network

- [Video 1 - What is a Neural Network?](https://youtu.be/hYB4ku0kmW8)
- [Video 2 - Gradient Descent](https://youtu.be/f8PYXDsSBpM)
- [Video 3 - Backpropagation](https://youtu.be/Wr5qCQ48t8E)
- [Video 4 - Backpropagation and Calculus](https://youtu.be/_d52fwoXXd4)



## Prediction

$$
\hat{y} = \sigma (Wx + b)
$$

- $\hat{y}$: The predicted value (y-hat)
- $\sigma(x)$: Sigmoid function
- $W$: Initial weights vector
- $x$: Input vector (vector of features)

## Error Function (Gradient Descent)

A measure of the error, of how badly, each

$$
E(W) = - \dfrac{1}{m} \sum_{i=1}^{m} \color{green}{ y_i \ln(\hat{y_i}) } + \color{red}{(1 - y_i) \ln(1 - \hat{y_i}) }
$$

- $E(W)$: Error in weights vector
- $\hat{y}$: The predicted value (y-hat)
