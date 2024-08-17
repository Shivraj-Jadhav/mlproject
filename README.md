## End to End Machine Learning Project

Project: Predicting Math Scores Using Machine Learning

This project focuses on building a machine learning model to predict a student's math score based on other academic performance indicators.

Here's a breakdown of the key components:

- Data: The project uses a dataset containing student information, including features like writing score, reading score, parental level of education, test preparation course enrollment (categorical), and the target variable: math score.
- Data Preprocessing: The data_transformation.py file handles missing values and encodes categorical features for compatibility with machine learning models.
- Model Building: After training multiple models and evaluating them, using a linear regression model (model_training.py) which leverages the linear relationship between features and math scores was selected to keep the model simple yet having great accuracy./n
A pipeline (model_training_pipeline.py) explore building and evaluating other models.
- Evaluation: The project involved calculating metrics like mean squared error (MSE) to assess the performance of the models in predicting math scores.
