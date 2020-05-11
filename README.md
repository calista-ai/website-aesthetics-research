# Deep Learning models to evaluate Website Aesthetics

Website aesthetics play an important role in attracting users and customers as
well as in enhancing user experience.

In this repository, we develop deep learning models that can evaluate the aesthetics of a website achieving high correlation with the human perception.

## Table of Contents

1. [Datasets](#datasets)

2. [Rating-Based models](#rating-based-models)

    2.1. [Rating-based approach I](#rating-based-approach-i)

    2.2. [Rating-based approach II](#rating-based-approach-ii)

    2.3. [Rating-based approach III](#rating-based-approach-iii)

3. [Comparison-Based models](#comparison-based-models)

    3.1. [Comparison-based approach I](#comparison-based-approach-i)

4. [Requirements](#requirements)

## Datasets

For the training process, we rely on 2 different datasets.

* **Rating-based dataset**: The users were asked to rate a webpage screenshot by providing an explicit numerical value on a scale

* **Comparison-based dataset**: The users were asked to compare 2 different webpage screenshots at a time and choose which of the two is preferable

You can find more about these datasets [here](https://github.com/calista-ai/website-aesthetics-datasets).

## Rating-based models

Models trained and evaluated using the **[Rating-based dataset](https://github.com/calista-ai/website-aesthetics-datasets)**.

Evaluation method: Training set (75.4%) - Test set (24.6%)

Results synopsis:

| Rating-based Model | Pearson Correlation Coefficient | RMSE | Accuracy (2 classes) |
|:------------------:|:-------------------------------:|:----:|:--------------------:|
| Approach I | 0.78 [0.69, 0.85] | 0.616 | 88.78 % |
| Approach II | 0.76 [0.66, 0.83] | 0.662 | 84.69 % |
| Approach III | 0.78 [0.68, 0.85] | 0.628 | 83.67 % |

### Rating-based approach I

**Description**: In this approach, the model was trained using the mean value of the user ratings for each website. The model's output is an aesthetics score on the scale 1-9.

### Rating-based approach II

**Description**: In this approach, the model was trained using the distribution of the user ratings for each website expressed as an empirical probability mass function. The model's output is a predicted distribution of the aesthetics scores. The final score is calculated by the mean value of the predicted distribution (scale 1-9).

### Rating-based approach III

**Description**: In this approach, the model was trained using all the pairs webpage - user rating. The model's output is an aesthetics score on the scale 1-9.

## Comparison-based models

Models trained and evaluated using the **[Comparison-based dataset](https://github.com/calista-ai/website-aesthetics-datasets)**.

Evaluation method: Leave-one-out Cross Validation

Results synopsis:

| Comparison-based Model | Pearson Correlation Coefficient | RMSE |
|:----------------------:|:-------------------------------:|:----:|
| Approach I | 0.70 [0.58, 0.79] | 1.353 |

### Comparison-based approach I

## Requirements