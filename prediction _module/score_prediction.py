from typing import Iterator
import numpy as np
from sklearn.linear_model import LinearRegression


def aggregate_scores(data_iterator: Iterator) -> dict:
    """
    Функция для агрегирования данных итератора
    :param data_iterator: итератор по записям с сотрудниками
    :return: словарь с данными вида {год: балл, ...}
    """
    years_scores = dict()

    for record in data_iterator:
        for results in record["Результаты"]:
            year = results["Год тестирования"]
            score = results["Сумма баллов"]
            if year not in years_scores:
                years_scores[year] = score
            else:
                years_scores[year] += score
    return years_scores


def score_predict_linear_regression(years_scores_dict: dict) -> dict:
    """
    Функция предсказания на основе линейной регрессии
    :param years_scores_dict: словарь вида {год: балл, ...}
    :return: новый словарь с прогнозом вида {год: балл, ...}
    """
    result = dict()

    sorted_items = sorted(years_scores_dict.items(), key=lambda x: x[0])
    years = [item[0] for item in sorted_items]
    scores = [item[1] for item in sorted_items]

    # создаем новый словарь на основе исходного
    for year, score in zip(years, scores):
        result[year] = score

    years = np.array(years).reshape(-1, 1)
    scores = np.array(scores)

    model = LinearRegression()
    model.fit(years, scores)

    next_year = np.array([[years.max()+1]])
    predicted_score = model.predict(next_year).item()
    next_year = next_year.item()

    result[next_year] = round(predicted_score, 3)

    return result
