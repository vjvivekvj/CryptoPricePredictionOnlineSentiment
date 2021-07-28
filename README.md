# Crypto Price Prediction using Online Sentiments

Project to predict Crypto currency Price from analyzing sentiments dataset of crypto related online texts, this includes tweets and news articles related to bitcoin.

### Pipeline
1. Data Collection and Transformation
2. Discretization
3. Rule generation using Decision Tree
4. Defuzzification using Fuzzy Inference System

### Optimizations
Genetic Algorithm has been applied to optimize
  1. Number of bins and type of binning in the discretization phase.
  2. Selection of features to give to the decision tree. 
  
#### Dataset:
[SentiCrypt](https://senticrypt.com/) API provides the bitcoin prices for a 1 hour window and also the mean, median of sentiment scores of the crypto related texts.

### Workflow:
1. Collect data from the [SentiCrypt](https://senticrypt.com/) API. 
2. Discretize it, either using equifrequency binning or equiwidth binning.
3. Pass the discretized data to the decision tree. The target variable is the BTCPrice
4. Pass the rules generated from the decision tree to the FIS.
5. The FIS then can be used to predict the values based on given input. 
6. Testing
