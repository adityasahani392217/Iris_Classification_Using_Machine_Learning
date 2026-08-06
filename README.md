# 🌸 Iris Classification Using Machine Learning

A web-based machine learning application built with **Streamlit** that classifies Iris flowers into their respective species using the **K-Nearest Neighbors (KNN)** algorithm. The application also provides interactive data visualizations and exploratory data analysis (EDA).

---

## 📌 Features

- 📂 Upload the Iris dataset (`iris.csv`)
- 📊 Display the dataset in tabular format
- 📈 View descriptive statistics
- 🌺 Show species distribution
- 📉 Interactive data visualizations
  - Species Distribution Pie Chart
  - Sepal Length vs Sepal Width
  - Petal Length vs Petal Width
  - Sepal Length vs Petal Length
  - Sepal Width vs Petal Width
  - Correlation Heatmap
- 🤖 Train a K-Nearest Neighbors (KNN) classification model
- ✅ Display model accuracy
- 🔍 Predict Iris flower species from user input

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## 📁 Project Structure

```
Iris_Classification_Using_Machine_Learning/
│── app.py
│── requirement.txt
│── iris.csv
└── README.md
```

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/adityasahani392217/Iris_Classification_Using_Machine_Learning.git
```

### Move to the project folder

```bash
cd Iris_Classification_Using_Machine_Learning
```

### Install dependencies

```bash
pip install -r requirement.txt
```

### Run the Streamlit application

```bash
streamlit run app.py
```

---

## 📊 Dataset

This project uses the famous **Iris Dataset**, which contains **150 flower samples** belonging to three species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

### Dataset Features

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

**Target Variable**

- Species

---

## 🤖 Machine Learning Model

The application uses the **K-Nearest Neighbors (KNN)** algorithm.

### Workflow

1. Upload the Iris dataset.
2. Encode species labels.
3. Split the dataset into training and testing sets.
4. Train the KNN model.
5. Evaluate model accuracy.
6. Predict the Iris species based on user inputs.

---

## 📈 Visualizations

The application includes:

- Species Distribution Pie Chart
- Sepal Length vs Sepal Width Scatter Plot
- Petal Length vs Petal Width Scatter Plot
- Sepal Length vs Petal Length Scatter Plot
- Sepal Width vs Petal Width Scatter Plot
- Correlation Heatmap

---

## 📷 Application Preview

After launching the application:

- Upload the Iris dataset.
- Explore the dataset statistics.
- View interactive charts.
- Check model accuracy.
- Enter flower measurements.
- Predict the Iris flower species.

---

## 📋 Requirements

```
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
```

Install them using:

```bash
pip install -r requirement.txt
```

---

## 🚀 Future Improvements

- Support multiple machine learning algorithms
- Confusion Matrix
- Classification Report
- Hyperparameter tuning
- Cross-validation
- Model comparison
- Deploy on Streamlit Community Cloud

---

## 👨‍💻 Author

**Aditya Sahani**

GitHub: https://github.com/adityasahani392217

Repository: https://github.com/adityasahani392217/Iris_Classification_Using_Machine_Learning

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.
