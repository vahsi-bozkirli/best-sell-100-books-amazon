# Determination / estimation of evaluation scores based on the comments and features of the top 100 bestsellers in the Amazon web store
Data Source: [https://www.kaggle.com/datasets/anshtanwar/top-200-trending-books-with-reviews]

During the evaluation of the books of Amazon users, I designed the model that automatically validates in the range of 1-5, taking into account the comments they made without having to specify a value manually, the time they commented (year and season) and the price they bought

As a model, I used AdaBoost Regressor, Decision Tree Regressor, SVR and Random Forest Regressor models, metric mean squared error metric.

best results: Random Forest Regressor

disadvantage of the model: the advantage of the model that cannot perform low evaluation due to the fact that I use only highly evaluated books during training: it offers objective and scientifically automatic evaluation

