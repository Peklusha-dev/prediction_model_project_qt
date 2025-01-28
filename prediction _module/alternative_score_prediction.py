def score_predict_exp_smooth(years_scores_dict: dict,
                             alpha: float = 0.5) -> dict:
    """
    Функция предсказания на основе экспоненциального сглаживания
    :param years_scores_dict: словарь {год: балл, ...}
    :param alpha: параметр сглаживания (0 < alpha < 1)
    :return: словарь с прогнозом на следующий год {год: балл, ...}
    """
    result = dict()

    sorted_items = sorted(years_scores_dict.items(), key=lambda x: x[0])
    years = [item[0] for item in sorted_items]
    scores = [item[1] for item in sorted_items]

    for year, score in zip(years, scores):
        result[year] = score

    forecast = scores[0]

    for score in scores[1:]:
        forecast = alpha * score + (1 - alpha) * forecast

    result[max(years)+1] = forecast

    return result
