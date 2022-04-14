import pandas as pd
import pickle

X = pd.read_csv('C:/Users/mewtw/project03_2/record_df.csv')

#creatinine_phosphokinase의 max 값 outlier
data = X.drop(columns=['creatinine_phosphokinase'])
print(X.head())


from sklearn.model_selection import train_test_split
train, test = train_test_split(data, train_size=0.8, test_size=0.2)
print("train shape: ", train.shape)
print("test shape: ", test.shape)

target = 'DEATH_EVENT'
features = ["age", "ejection_fraction","serum_creatinine", "anaemia", "diabetes", "high_blood_pressure", "sex", "smoking", "platelets", "serum_sodium"]

X_train = train[features]
y_train = train[target]
X_test = test[features]
y_test = test[target]

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


model = RandomForestClassifier(max_features=0.5, max_depth=10, random_state=1)
model.fit(X_train, y_train)
model_pred = model.predict(X_test)
model_acc = accuracy_score(y_test, model_pred)


print("Accuracy of Random Forest Classifier is : ", "{:.2f}".format(100*model_acc))
# 배포를 위해 pickle파일로 만든다 
pickle.dump(model, open('model.pkl', 'wb'))
