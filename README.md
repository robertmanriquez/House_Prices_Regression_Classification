# House_Prices_Regression_Classification

Machine Learning models for predicting housing prices and classifying sale type (Ames, Iowa dataset).  Using the dataset available from [Kaggle](https://www.kaggle.com/c/house-prices-advanced-regression-techniques), I built several basic linear regression models, evaluated their performance, and chose which to fine tune and optimize.

The Ames, Iowa housing dataset is a quite robust documentation of thousands of homes old in Ames, containing over 80 features per housing sale, including everything from square footage, condition, and neighborhood all the way to the nitty gritty (type of masonry veneer finishing, basement ceiling height, fence quality).  The documentation can be read [here](https://ww2.amstat.org/publications/jse/v19n3/decock/datadocumentation.txt)

# Below is a description of what's inside:

```
* Ames_Cleaner.ipynb

This file contains the functions I used to handle null values, impute missing values, and engineer features.  Also has dictionary maps for each ordinal and nominal category.
```
```
* Housing_EDA_LinearRegression.ipynb

After using the cleaned/processed data, I implemented a basic linear regression using a few variables I intuitively chose based on my knowledge of how houses are sold, backed up by Exploratory Data Analysis (EDA) and how they relate to the target variables.
```
```
* Housing_Ridge_Regression.ipynb

Lastly, in this notebook I tested other LR models using Lasso, Ridge, and ElasticNet style regularization to gain an understanding of which features mattered the most.  Selecting the best of the three, I built a final Ridge regression model incorporating scaled features, polynomial fitting, and using only the top ~70 most important features.  This yielded a model with Train/Test accuracies of 97.6% and 92.3%, respectively.  
```
```
* Housing_Classification.ipynb

In process of uploading, please check back soon!
```

I invite you to take a look, and thank you for visiting!

**Robert Manriquez**


## Acknowledgments

* Data used was supplied from Kaggle.
* Modeling built using SciKit-Learn libraries.
