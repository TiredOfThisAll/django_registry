import csv
from django.apps import apps
from .connection import create_connection

def import_csv_data(file_path):
    model = apps.get_model('phone_form', 'Registry')
    with open(file_path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)

        for row in reader:
            data = {
                'abc': row[0],
                'start': row[1],
                'end': row[2],
                'capacity': int(row[3]),
                'operator': row[4],
                'region': row[5],
                'GAR_territory': row[6],
                'TIN': row[7],
            }
            try:
                model.objects.create(**data)
            except Exception as e:
                print(file_path, data)



def truncate_table():
    with create_connection() as connection:
        cursor = connection.cursor()
        sql = f"TRUNCATE phone_form_registry"
        cursor.execute(sql)
        connection.commit()
