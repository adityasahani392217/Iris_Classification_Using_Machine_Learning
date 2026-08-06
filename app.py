import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

st.set_page_config(page_title="Iris Classification", layout="wide")

st.title("🌸 Iris Flower Classification")

# Upload CSV
uploaded_file = st.file_uploader("Upload iris.csv", type=["csv"])

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.header("Dataset")
    st.dataframe(df)

    st.header("Dataset Statistics")
    st.write(df.describe())

    st.header("Species Count")
    st.write(df["Species"].value_counts())

    # Pie Chart
    st.header("Species Distribution")

    fig, ax = plt.subplots()
    counts = df["Species"].value_counts()
    ax.pie(
        counts.values,
        labels=counts.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax.axis("equal")
    st.pyplot(fig)

    # Scatter Plot 1
    st.header("Sepal Length vs Sepal Width")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(
        data=df,
        x="Sepal.Length",
        y="Sepal.Width",
        hue="Species",
        ax=ax
    )
    st.pyplot(fig)

    # Scatter Plot 2
    st.header("Petal Length vs Petal Width")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(
        data=df,
        x="Petal.Length",
        y="Petal.Width",
        hue="Species",
        ax=ax
    )
    st.pyplot(fig)

    # Scatter Plot 3
    st.header("Sepal Length vs Petal Length")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(
        data=df,
        x="Sepal.Length",
        y="Petal.Length",
        hue="Species",
        ax=ax
    )
    st.pyplot(fig)

    # Scatter Plot 4
    st.header("Sepal Width vs Petal Width")

    fig, ax = plt.subplots(figsize=(6,4))
    sns.scatterplot(
        data=df,
        x="Sepal.Width",
        y="Petal.Width",
        hue="Species",
        ax=ax
    )
    st.pyplot(fig)

    # Heatmap
    st.header("Correlation Heatmap")

    temp = df.copy()

    le = LabelEncoder()
    temp["Species"] = le.fit_transform(temp["Species"])

    corr = temp.corr()

    fig, ax = plt.subplots(figsize=(6,4))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Model Training
    X = temp.drop("Species", axis=1)
    y = temp["Species"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.30,
        random_state=42
    )

    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)

    st.header("Model Accuracy")
    st.success(f"Accuracy: {accuracy:.2%}")

    st.header("Predict Iris Species")

    col1, col2 = st.columns(2)

    with col1:
        sepal_length = st.number_input(
            "Sepal Length",
            value=5.1
        )

        sepal_width = st.number_input(
            "Sepal Width",
            value=3.5
        )

    with col2:
        petal_length = st.number_input(
            "Petal Length",
            value=1.4
        )

        petal_width = st.number_input(
            "Petal Width",
            value=0.2
        )

    if st.button("Predict"):

        prediction = model.predict(
            [[
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            ]]
        )

        species = le.inverse_transform(prediction)

        st.success(f"Predicted Species: **{species[0]}**")

else:
    st.info("Please upload the iris.csv dataset to begin.")
