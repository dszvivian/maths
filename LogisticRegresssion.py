from dataset_loader import DatasetLoader

from LinearRegression import LinearRegression


class LogisticRegression:
    pass


if __name__ == "__main__":
    obese_not_obese_dataset = DatasetLoader()
    obese_not_obese_dataset.csv_to_array(path="./datasets/obesity-classification-dataset.csv")
    obese_not_obese_dataset.visualize_dataset()
    

    # Trying out Linear Regression for Logistic Regression 

    regressor = LinearRegression()
    regressor.train(obese_not_obese_dataset.X,obese_not_obese_dataset.Y)
    regressor.plot()
    print(f"Actual value = {obese_not_obese_dataset.Y[-1]} Predicted Value = {regressor.predict(obese_not_obese_dataset.X[-1])}")