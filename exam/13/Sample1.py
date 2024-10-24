from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

x, y = datasets.make_regression(n_samples=300, n_features=1, noise=20)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

e = linear_model.LinearRegression()
e.fit(x_train, y_train)

print("회귀계수는", e.coef_, "입니다.")
print("절편은", e.intercept_, "입니다.")

y_pred = e.predict(x_test)

print("학습 데이터에 의한 결정계수는", e.score(x_train, y_train), "입니다.")
print("테스트 데이터에 의한 결정계수는", e.score(x_test, y_test), "입니다.")

plt.scatter(x_train, y_train, label="train")
plt.scatter(x_test, y_test, label="test")
plt.plot(x_test, y_pred, color="magenta")
plt.legend()

plt.show()
