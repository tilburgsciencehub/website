---
title: "Extreme gradient boosting with XGBoost in Python"
description: "Explanation and usage of XGBoost in Python"
keywords: "XGBoost, Extreme Gradient Boosting, Machine Learning, python, decision tree, model, Python "
draft: true
weight: 3
author: "Niels Rahder, Kheiry Sohooli"
---

## Using XGBoost in Python 

To use XGBoost for classification or regression tasks in Python, you'll need to install and import the `xgboost` package. 


{{% codeblock %}}

```Python
# install XGBoost 
pip install xgboost 

# import XGBoost
import xgboost as xgb
```
{{% /codeblock %}}

You can load Diamond dataset from Seaborn package to implement XGBoost with the following codes:

{{% codeblock %}}

```Python
# import Seaborn 
import seaborn as sns

# loading dataset
diamonds = sns.load_dataset("diamonds")
```
{{% /codeblock %}}

After loading and inspecting your data, you should define your X and y variables. In this case, for example, if you're predicting the price of a diamond based on its various characteristics, you would set "price" as your y variable and the diamond's characteristics as your predictors (X).

{{% codeblock %}}

```Python
# selecting all column except 'price' as predictors
X= diamonds.loc[:, diamonds.columns != 'price']

# specify 'price' column to 'y'
y = diamonds[['price']]
```
{{% /codeblock %}}

Now, let's divide the data into training and testing sets using the `sklearn.model_selection` module and then check the shape of the data.

{{% codeblock %}}

```Python
# importing train_test_split 
from sklearn.model_selection import train_test_split
# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# check the shapes
import os 
print('X-train shape:',X_train.shape,
     'X-test shape:' , X_test.shape,
     'y_train shape:' ,y_train.shape,
     'y_test shape:' ,y_test.shape,sep=os.linesep )
```
{{% /codeblock %}}

Before training the dataset using the XGBoost algorithm, we need to complete two essential steps: storing the dataset in a `DMatrix` and setting the algorithm's parameters. 
XGBoost uses the `DMatrix` class to efficiently store the dataset, enabling you to run XGBoost optimally.

{{% codeblock %}}

```Python
# import xgboost package
import xgboost as xgb

# train train and test data which automaticaly create regression matrices
train = xgb.DMatrix(X_train, y_train, enable_categorical=True)
test= xgb.DMatrix(X_test, y_test, enable_categorical=True)
```
{{% /codeblock %}}

{{% tip %}}
You can also import XGBoost from Scikit-learn but native API of XGBoost has more capabilities.
{{% /tip %}}

Use dictionary or list of tuples to specify both `Booster parameters` and `evaluation parameter`. 

{{% codeblock %}}

```Python
# Define Parameters
param = {"objective": "reg:squarederror"}

# set evaluation 
evallist = [(train, 'train'), (test, 'eval')]
```
{{% /codeblock %}}
 
You also need to decide on the number of boosting rounds, which determines how many rounds the XGBoost algorithm will use to minimize the loss function. For now, let's set it to 10, but it's important to note that this is one of the parameters that should be tuned.

{{% codeblock %}}

```Python
# train the model 
num_round = 10
model = xgb.train(param, train, num_round, evallist)
```
{{% /codeblock %}}

The output displays the model's performance (RMSE) on both the training and validation sets. As mentioned earlier, the number of boosting rounds is a crucial tuning parameter. In fact, more rounds mean more attempts to minimize the loss. However, it's important to be careful to prevent overfitting. Sometimes, the model may stop improving after a certain number of rounds. To address this, you can use the following code. We increase the number of rounds to 1000 and introduce the `early_stopping_rounds` parameter to the code above. This ensures that training stops after 50 rounds if there is no improvement in the results. 

{{% codeblock %}}

```Python
# increase number of boosting rounds 
num_round = 1000
model = xgb.train(param, train, num_round, evallist,
   # enabeling early stopping
   early_stopping_rounds=50)
```
{{% /codeblock %}}

### Visualization in python 

Use the following code to visualize the feature importance when using the XGBoost algorithm to predict the outcome variable. Furthermore, you can also see the trees that have been created.

{{% codeblock %}}

```Python
import matplotlib.pyplot as plt 
# visualize the importance of predictors
xgb.plot_importance(model)
```
{{% /codeblock %}}

To visualize the trees:

{{% codeblock %}}

```Python

xgb.plot_tree(model)
plt.show()
```
{{% /codeblock %}}

{{% tip %}}
Note that to visualize the trees you need `graphviz`.
{{% /tip %}}


  
- **Implementing of XGBoost in Python:**
  - Training the model and evaluation 
  - visualization of important features and created tree by XGBoost 




### How does XGBoost work?

The algorithm starts by calculating the residual values for each data point based on an initial estimate. For instance, given the variables `age` and `degree`, we compute the residual values relative to `salary`(target variable), for which the value `49` will serve as our initial estimation:


  
 | **age** | **degree** |**Salary** | **Residual** |
 | ------- | --------- | -----------| ------------
 |     20  |    yes    |    40      |  -9          |
 |    28   |    yes    |    46      |  -3          |
 |    31   |    no     |    50      |   1          | 
 |   34    |    yes    |    54      |  5           |
 |   38    |    no     |    61      |  12          |
  

Next, the algorithm calculates the similarity score for the entire tree and the individual splits, especially focusing on an arbitrarily chosen mean value of 24 (the mean between the first two age values) using the following formula:  

 
<div style="text-align: center;">
{{<katex>}}
\text{Similarity score} = \frac{{(\sum \text{Residual})^2}}{{\text{\# of Residual} + \lambda}}
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score root node} (\lambda = 1) = \frac{(-9 - 3 + 1 + 5 + 12)^2}{6} = \frac {36}{6} = 6 
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score left node} (\lambda = 1) = \frac{(-9 )^2}{2} = 40.5 
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score right node} (\lambda = 1) = \frac{(- 3 + 1 + 5 + 12 )^2}{5} = 112.5
{{</katex>}}
</div>

<br>

{{% warning %}}
λ is a regularization parameter which is used to prune the tree. In practice, the optimal value for λ is best determined through cross-validation or a similar technique where various values of the parameter are tested to see which gives the best performance on a validation set. For now, we set it to the default value of 1.
{{% /warning %}}

Following the calculation of the individual similarity scores, the gain is calculated as:

<div style="text-align: center;">
{{<katex>}}
\text{Gain} = \text{sim(left node)} + \text{sim(right node)} - \text{sim(root node)}
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Gain} = 40.5 + 112.5 - 6 = 147
{{</katex>}}
</div>

<br>
 
The algorithm then compares this value to gain-values generated by other split options within the dataset to determine which division optimally enhances the separation of classes. For example, when we choose the split value of 29.5 (the mean value between the second and third ages), the similarity score of the root node remains unchanged, while the similarity scores of the left and right nodes change to:

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score left node} ( \lambda = 1) = \frac{(-9 -3)^2}{3} = 72
{{</katex>}}
</div>

<br>

<div style="text-align: center;">
{{<katex>}}
\text{Similarity score right node} ( \lambda = 1) = \frac{(1  + 5 + 12)^2}{4} = 162
{{</katex>}}
</div>




<br>


The gain-value therefore becomes:
<br> 

<div style="text-align: center;">
{{<katex>}}
\text{Gain} = {72 +  162 - 6 } =228
{{</katex>}}
</div>

<br> 

Which is a higher value than that of the split based on our initial values, and is therefore used as the more favorable option. The same process is then repeated for all possible split combinations in order to find the best option. After this process is completed for all possible split options the final tree (with the residual values) becomes:

<p align = "center">
<img src = "../img/tree_structure.png" width="400">
</p>

The ouput value for each data point is then calculated via the following formula: 

<div style="text-align: center;">
{{<katex>}}
\text{Output value} = {\text{initial estimate} +  \alpha * \text{output of tree} } 
{{</katex>}}
</div>




<br> 

<div style="text-align: center;">
{{<katex>}}
\text{Output value (age = 20)} = {49 +  0.3 * -6 } = 47.2
{{</katex>}}
</div>

{{% warning %}}
ɑ is the learning rate of the model, for now we set it to the default value of 0.3 
{{% /warning %}}


From this we can see that our output value for the average salary of a 20 year old has decreased from the initial prediction of 49 to our new prediction of 47.2, which is closer to the true value of 40! An overview of all output values can be found below, from these output values the new residual values `Res2` are constructed. Therefore we can conclude that the average residual has decreased! 

This process is then repeated until the model cannot improve anymore  


| **Salary**  | **age** | **degree** | **Residual** | **Output** | **Residual 2** |
| --------- | ---------- | --------- | --------- |  --------- | --------- |
|     40   | 20   | yes |  -9   | 47.2 | -7.2 |
|   46   |  28    | yes |  -3   | 47.2 | -7.2 |
|   50   |  31    | no |  1   | 50.95 | -0.95 |
|    54   |  34   | yes |  5   | 50.5 | 3.5 |
|   61   |  38    | no |  12   | 50.95 | 10.05 |

<br> 

An additional factor we need to take into account is gamma (γ), which is an arbitrary regularization parameter that controls the complexity of individual trees in the boosting process. It is a measure of how much an additional split will need to reduce loss in order to be added to the collection. 
A higher gamma value encourages simpler trees with fewer splits, which helps to prevent overfitting and lead to a more generalized model. A lower gamma, on the other hand, allows for more splits and potentially more complex trees which may lead to better fit on the training data but could increase the risk of overfitting.  

The tree is pruned when: 

<div style="text-align: center;">
{{<katex>}}
\text{gain-value - }\gamma < 0
{{</katex>}}
</div>
<br>

In this case the branch is removed. In other words the gain-value always needs to be higher than gamma in order for a split to be used. 

<br> 

