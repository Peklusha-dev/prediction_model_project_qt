import pandas as pd


def get_unique_departments(file_path):
    """
    Возвращает уникальные отделы из файла.
    :param file_path: Путь к файлу Excel
    :return: Список уникальных отделов
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl', usecols=["Отдел"], dtype=str)
        return sorted(df["Отдел"].dropna().unique())
    except Exception as e:
        raise ValueError(f"Ошибка при извлечении отделов: {str(e)}")


def get_employees_by_department(file_path, department):
    """
    Возвращает список сотрудников для указанного отдела.
    :param file_path: Путь к файлу Excel
    :param department: Название отдела
    :return: Список сотрудников
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl', usecols=["ФИО", "Отдел"], dtype=str)
        filtered_df = df[df["Отдел"] == department]
        return filtered_df["ФИО"].dropna().tolist()
    except Exception as e:
        raise ValueError(f"Ошибка при извлечении сотрудников: {str(e)}")


def get_employee_by_fio_department(file_path, department, fio):
    """
    Чтение информации о сотруднике по ФИО и отделу.
    :param file_path: Путь к файлу для чтения.
    :param department: Название отдела.
    :param fio: ФИО сотрудника.
    :return: Информация о сотруднике в формате:
             {
                 "ФИО": str,
                 "Должность": str,
                 "Отдел": str,
                 "Результаты": [
                     {
                         "Год тестирования": str,
                         "Критерии": {"Критерий1": баллы, "Критерий2": баллы, ...},
                         "Сумма баллов": float
                     },
                     ...
                 ]
             }
    """
    try:
        # Проверяем входные аргументы
        if not all(isinstance(arg, str) and arg.strip() for arg in [file_path, department, fio]):
            raise ValueError("Некорректные аргументы. Убедитесь, что путь к файлу, отдел и ФИО указаны корректно.")

        # Читаем данные из файла Excel
        df = pd.read_excel(file_path, engine="openpyxl", dtype=str)

        # Удаляем лишние пробелы из столбцов ФИО и Отдел
        df["ФИО"] = df["ФИО"].str.strip()
        df["Отдел"] = df["Отдел"].str.strip()

        # Фильтруем строки по ФИО и Отделу
        fio = fio.strip()
        department = department.strip()
        candidate_rows = df[(df["ФИО"] == fio) & (df["Отдел"] == department)]

        # Проверяем, есть ли результаты после фильтрации
        if candidate_rows.empty:
            print(f"Сотрудник с ФИО '{fio}' в отделе '{department}' не найден.")
            return None

        # Формируем результат
        results = []
        for _, row in candidate_rows.iterrows():
            year = row.get("Год тестирования", "Не указан")
            criteria_columns = [col for col in row.index if col.isdigit()]
            criteria_data = {col: float(row[col].replace(",", ".") if isinstance(row[col], str) else row[col])
                             for col in criteria_columns}

            # Вычисляем сумму баллов
            total_score = sum(criteria_data.values())

            results.append({
                "Год тестирования": year,
                "Критерии": criteria_data,
                "Сумма баллов": total_score,
            })

        # Составляем итоговый результат
        result = {
            "ФИО": fio,
            "Должность": candidate_rows.iloc[0].get("Должность", "Не указана"),
            "Отдел": department,
            "Результаты": results,
        }

        return result
    except Exception as e:
        print(f"Ошибка при чтении данных: {str(e)}")
        return None

#ПЕРЕНЕСТИ В ОТДЕЛЬНЫЙ ФАЙЛ. ДОДЕЛАТЬ.
#это просто пример, который нагенерил gpt
class EmployeeIterator:
    def __init__(self, file_path, department=None):
        """
        Инициализация итератора.

        :param file_path: Путь к файлу Excel.
        :param department: Фильтр по отделу (None для всех отделов).
        """
        self.file_path = file_path
        self.department = department
        self.workbook = load_workbook(file_path, read_only=True)
        self.sheet = self.workbook.active
        self.headers = [cell.value for cell in next(self.sheet.iter_rows(values_only=True))]
        self.department_index = self.headers.index('Отдел') if 'Отдел' in self.headers else None
        self.unique_id_index = self.headers.index('ФИО') if 'ФИО' in self.headers else None
        self.employee_data = defaultdict(list)
        self.processed_keys = set()  # Множество для отслеживания обработанных сотрудников

    def __iter__(self):
        return self

    def __next__(self):
        """
        Возвращает данные об одном сотруднике за итерацию.
        """
        # Построчное чтение и группировка данных
        for row in self.sheet.iter_rows(values_only=True):
            if row[self.unique_id_index] is None:
                continue  # Пропускаем пустые строки

            # Преобразование строки в словарь
            row_data = dict(zip(self.headers, row))

            # Проверка фильтра по отделу
            if self.department is None or row_data['Отдел'] == self.department:
                # Группируем данные по ФИО (или другому уникальному ключу)
                key = row_data['ФИО']
                if key not in self.processed_keys:
                    self.employee_data[key].append(row_data)

        # Возврат следующего сотрудника
        if self.employee_data:
            key, records = self.employee_data.popitem()
            self.processed_keys.add(key)
            return self._combine_employee_data(records)
        else:
            self.workbook.close()
            raise StopIteration

    def _combine_employee_data(self, records):
        """
        Объединяет строки данных о сотруднике.

        :param records: Список записей о сотруднике.
        :return: Объединенные данные.
        """
        combined = records[0].copy()  # Используем первую запись как основу
        for record in records[1:]:
            for key, value in record.items():
                if value and not combined.get(key):  # Заполняем только пустые поля
                    combined[key] = value
        return combined



