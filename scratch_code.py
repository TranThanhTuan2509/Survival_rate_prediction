import pandas as pd
from tabulate import tabulate
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv(filepath_or_buffer="train.csv", header=0)
df = df[['PassengerId',"Survived", "Pclass", "Sex", "Age", "SibSp","Parch", "Fare"]]

def preprocessing(df):
    # Remove NaN values
    # print("Original length of Dataframe: {}".format(len(df)))
    df.dropna(inplace=True)
    # print("Length of Dataframe after removing NaN value: {}".format(len(df)))

    # Attribute Construction
    df['num_family_member'] = df['SibSp'] + df['Parch']
    df.drop(['SibSp', 'Parch'], axis=1, inplace=True)

    # Convert gender to number
    df.replace("male","1", inplace=True)
    df.replace("female","0", inplace=True)
    # print(tabulate(df, headers="keys", tablefmt="psql"))


def Visualization(df):
    sns.histplot(data=df['Age'])
    plt.title("Age of Passengers")
    plt.xlabel("Age", fontsize=30)
    plt.ylabel("Count", fontsize=30)
    plt.show()


def Training_process(df):
    feature_variable = df[["Pclass","Sex","Age","Fare","num_family_member"]]
    output_variable = df["Survived"]

    # Training set
    X_train = feature_variable[:int(0.8*len(df))]
    y_train = output_variable[:int(0.8*len(df))]

    # Test set
    X_test = feature_variable[int(0.8*len(df)):]
    Y_test = output_variable[int(0.8*len(df)):]

# tieu chuan hoa du lieu
#     print(tabulate(df, headers="keys", tablefmt="psql"))
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    # print(tabulate(feature_variable, headers="keys", tablefmt="psql"))


    # Khai bao su dung ML model (KNN)
    knn = KNeighborsClassifier(n_neighbors=5)

    # Huan luyen model
    knn.fit(X=X_train, y=y_train)

    # Kiem tra model
    y_prediction = knn.predict(X=X_test)
    accuracy = accuracy_score(y_true=Y_test,y_pred=y_prediction)
    # print("Accuracy of model: {}%".format(accuracy*100))

    # tao ra 1 hanh khach gia tuong
    # passengerID = 403
    pclass = 1
    sex = 1
    age = 19
    fare = 78
    num_family_member = 0


    hanhkhach = [pclass,sex,age,fare,num_family_member]
    print(knn.predict_proba([hanhkhach]))
    print(knn.predict([hanhkhach]))

preprocessing(df)
Training_process(df)