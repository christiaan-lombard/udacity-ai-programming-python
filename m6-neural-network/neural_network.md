# Neural Network

- [Video 1 - What is a Neural Network?](https://youtu.be/hYB4ku0kmW8)
- [Video 2 - Gradient Descent](https://youtu.be/f8PYXDsSBpM)
- [Video 3 - Backpropagation](https://youtu.be/Wr5qCQ48t8E)
- [Video 4 - Backpropagation and Calculus](https://youtu.be/_d52fwoXXd4)

![Neural Network](https://www.researchgate.net/publication/329216193/figure/fig3/AS:697582816870406@1543328112943/Architecture-of-multilayer-artificial-neural-network-with-error-backpropagation.png)

## Neurons

Each neuron simply holds a value.
 - Input neurons hold the input values
 - Every other neuron holds the value of the activation function with respect to the previous layer.

$$
A^{(1)} = \begin{bmatrix}
a^{(1)}_1 \\ a^{(1)}_2 \\ a^{(1)}_3 \\ \vdots \\ a^{(1)}_n
\end{bmatrix}
$$

Where:
 - $A^{(1)}$: Values of the 1st layer
 - eg. $a^{(1)}_2$ is the value of the 2nd neuron in the 1st layer

### Weights

Each hidden and output neuron also holds a weight with respect to each input neuron. Weights can be organised as a matrix where each row represents the weights of a particular neuron with respect to the previous layer:

$$
W = \begin{bmatrix}
w_{1,1} & w_{1,2} & w_{1,2} & \cdots & w_{1,n} \\
w_{2,1} & w_{2,2} & w_{2,3} & \cdots & w_{2,n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
w_{k,1} & w_{k,2} & w_{k,3} & \cdots & w_{k,n}
\end{bmatrix}
$$

Where:
 - $W$: Weights of the current layer
 - eg. $w_{1,3}$: The weight of the 1st neuron in the current layer with respect to the 3rd neuron in the previous layer.
 - $k$: The neuron # in current layer
 - $n$: The neuron # in previous layer

Shape and size of the weight matrix for a given layer can be determined by the number of neurons in the previous layer times the number of neurons in the current layer:

$$
Size = (inputs \times outputs)
$$

### Bias

Each neuron's bias can be represented as a single column matrix:

$$
B = \begin{bmatrix}
b_1 \\ b_2 \\ b_3 \\ \vdots \\ b_k
\end{bmatrix}
$$

## Feedforward (Activation)

The activation function determines the value of the neuron.

$$
\hat{y} = \sigma (WA + B)
$$

$$
\hat{y} = \sigma (w_1a_1 + w_2a_2 + w_3a_3 + \cdots + w_na_n + b)
$$

- $\hat{y}$: The predicted/output value (y-hat)
- $\sigma(x)$: Sigmoid activation function
- $W$: Weights vector
- $A$: Input vector (vector of features) from previous layer
- $B$: Bias vector


### Sigmoid

$$
\sigma(x) = \dfrac{1}{1 + e^{-x}}
$$

Sigmoid Derivative:

$$
\dfrac{d \sigma(x)}{d(x)} = \sigma(x) \cdot (1 - \sigma(x))
$$

See [deivative of sigmoid function](https://math.stackexchange.com/questions/78575/derivative-of-sigmoid-function-sigma-x-frac11e-x)

## Backpropogation

Backpropagation computes the gradient of the loss function with respect to the weights of the network for a single input–output example, and does so efficiently, unlike a naive direct computation of the gradient with respect to each weight individually. This efficiency makes it feasible to use gradient methods for training multilayer networks, updating weights to minimize loss; gradient descent, or variants such as stochastic gradient descent, are commonly used. The backpropagation algorithm works by computing the gradient of the loss function with respect to each weight by the chain rule, computing the gradient one layer at a time, iterating backward from the last layer to avoid redundant calculations of intermediate terms in the chain rule.

### Calculate Error: Loss Function / Cost Function

Where:
- $E$: Total error
- $E(W)$: Error in weights vector
- $\hat{y}$: The predicted value (y-hat)
- $y$: The true (target) value

#### Sum of Errors (SE)

$$
E = \hat{Y} - Y
$$

#### Sum of Squared Errors (SSE)

$$
E = (\hat{Y} - Y)^2
$$

$$
E = \dfrac{1}{2} \sum_{\mu} \sum_{j}[y^{\mu}_j - \hat{y}^{\mu}_j]^2
$$

#### Mean Square Error (MSE)

$$
E = \dfrac{1}{N} (\hat{Y} - Y)^2
$$

$$
E = \dfrac{1}{2m} \sum_{\mu} [y^{\mu} - \hat{y}^{\mu}]^2
$$

#### Log Loss / Cross-Entropy

Cross-entropy loss, or log loss, measures the performance of a classification model whose output is a probability value between 0 and 1. Cross-entropy loss increases as the predicted probability diverges from the actual label.

$$
E(W) = - \dfrac{1}{m} \sum_{i=1}^{m} \color{green}{ y_i \ln(\hat{y_i}) } + \color{red}{(1 - y_i) \ln(1 - \hat{y_i}) }
$$





### Gradiant Descent (Weight Update)

A weight update:
$$
w_i = w_i + \Delta{w_i}
$$

Where change in weight is calculated as:

$$
\Delta{w_i} = \eta \delta x_i
$$

Where:
 - $\Delta{w_i}$ = Change in weight
 - $w_i$ = Current weight
 - $\eta$ = Learning rate
 - $\delta$ = Error term

#### **Error Term**

$$
\delta = (y - \hat{y}) f'(h)
$$
$$
\delta = (u - \hat{y}) f'(\sum{w_ix_i})
$$

Where:
 - $f'(h)$ = derivative of the activation function $f(h)$