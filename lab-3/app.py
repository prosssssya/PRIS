import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import csv

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
STATIC_FOLDER = 'static'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(STATIC_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/train', methods=['POST'])
def train():
    df = pd.read_csv('last_uploaded.csv')

    x_columns = request.form.getlist('x_columns')
    y_column = request.form['y_column']

    if not x_columns or y_column not in df.columns:
        return "Некорректный выбор признаков"

    df = df.dropna(subset=x_columns + [y_column])

    X = df[x_columns]
    y = df[y_column]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.xlabel('Фактические значения')
    plt.ylabel('Предсказанные значения')
    plt.title('Факт vs Прогноз')
    plt.grid(True)
    scatter_path = os.path.join(STATIC_FOLDER, 'prediction.png')
    plt.savefig(scatter_path)
    plt.close()

    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    corr_path = os.path.join(STATIC_FOLDER, 'correlation.png')
    plt.savefig(corr_path)
    plt.close()

    return render_template('result.html',
                           mse=round(mse, 4),
                           r2=round(r2, 4),
                           scatter_url=scatter_path,
                           corr_url=corr_path)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return "Файл не выбран"

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        MAX_ROWS = 100_000

        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)

        chunks = pd.read_csv(filepath, chunksize=20_000)

        df_chunks = []
        total_rows = 0

        for chunk in chunks:
            df_chunks.append(chunk)
            total_rows += len(chunk)
            if total_rows >= MAX_ROWS:
                break

        df = pd.concat(df_chunks, ignore_index=True)
    except Exception as e:
        return f"Ошибка при чтении CSV: {e}"

    df.to_csv('last_uploaded.csv', index=False)

    columns = df.select_dtypes(include='number').columns.tolist()
    preview_html = df.head(10).to_html(classes="table table-bordered", index=False)

    return render_template('select_columns.html', preview_table=preview_html, columns=columns)

if __name__ == '__main__':
    app.run(debug=True)
