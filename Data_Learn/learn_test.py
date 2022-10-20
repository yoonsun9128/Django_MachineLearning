import joblib

model = joblib.load('./Django_MachineLearning/titanic_LR_model.pkl')

test_x = [[1, 0, 10.0000, 1, 1, 1, 1]]
test_test = model.predict(test_x)
print(test_test)