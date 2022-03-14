# Arabic-Dialect-Classification

Predicting the Arabic Dialect of text. This project used Machine Learning and Deep Learning approaches in predicting 18 Arabic dialects.

## The Problem

Classifying Arabic text into 18 different dialects. Some dialects have more samples than others. The Egyptian dialect has the most number of data points while the Tunisian is the lowest.

I've built two approaches. The first is using Machine Learning Classifiers while the second is testing the data with a simple LSTM model.

## Data:
The dataset and the dialect identification problem were addressed by Qatar Computing Research Institute, moreover, they published a [paper](https://arxiv.org/pdf/2005.06557.pdf), feel free to get more insights from it.

### Machine Learning:
- Logistic Regression scored **52.8% validation accuracy**
- Naïve Bayes Classifier scored **47.81% validation accuracy**
- Random Forest Classifier scored **37.36% validation accuracy**

I used a TF-IDF vectorizer with (1-4) n-grams and Arabic stop words from the SpaCy library.

Then all three classifiers were merged into a Voting Classifier with soft voting which resulted in **55% Validation Accuracy** and **55.7% Testing Accuracy**.

### Deep Learning:
A simple architecture is used here:
- Embedding layer with uniform initializer and shape of output is 128
- LSTM with 128 units, 40% dropout and 40% Recurrent dropout
- RELU activation layer
- Sigmoid Layer

The model overfitted after the second epoch, so I replaced the Categorical Cross Entropy with [Sigmoid Focal Cross-Entropy](https://www.tensorflow.org/addons/api_docs/python/tfa/losses/SigmoidFocalCrossEntropy) which improved the overall accuracy and reduced overfitting slightly. It’s a good choice in case of unbalanced data such as ours here. Also, it improved the precision compared to the Categorical Cross Entropy. Though, we still need to investigate the overfitting here.

Validation Accuracy is ~90% while Testing Accuracy is ~50%. The model is overfitting badly, so we need to explore other architectures and use regularization methods to overcome this.


## License
[MIT](https://choosealicense.com/licenses/mit/)
