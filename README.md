## End to End Machine Learning Project

Project: Predicting Math Scores Using Machine Learning

This project focuses on building a machine learning model to predict a student's math score based on other academic performance indicators.

Here's a breakdown of the key components:

- Data: The project likely uses a dataset containing student information, including features like writing score, reading score, parental level of education, test preparation course enrollment (categorical), and the target variable: math score.
- Data Preprocessing: The data_transformation.py file handles missing values and encodes categorical features for compatibility with machine learning models.
- Model Building: While there's no explicit model selection script, the code suggests training two potential models:
A linear regression model (model_training.py) likely leverages the linear relationship between features and math scores.
A pipeline (model_training_pipeline.py) might explore building and evaluating other models (the specific model type isn't immediately evident from the code).
- Evaluation: The project might involve calculating metrics like mean squared error (MSE) to assess the performance of the models in predicting math scores. However, there's no explicit evaluation script present in the public repository.
