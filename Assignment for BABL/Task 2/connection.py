import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

def insert_car_information(car_type, car_name, car_model, year, battery_capacity = None, fuel_efficiency = None):
    my_db = mysql.connector.connect(host='localhost',
                                    database='cars',
                                    user='root',
                                    password='1234')
    cursor = my_db.cursor()

    if car_type == 'Electric':
        query = "INSERT INTO cars (car_type, car_name, car_model, year, battery_capacity) " \
                "VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (car_type, car_name, car_model, year, battery_capacity))
        
    elif car_type == 'Gas':
        query = "INSERT INTO cars (car_type, car_name, car_model, year, fuel_efficiency) " \
                "VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (car_type, car_name, car_model, year, fuel_efficiency))

    my_db.commit()


    if my_db.is_connected():
        cursor.close()
        my_db.close()

@app.route('/connection', methods=['POST'])
def connection():
    car_type = request.form['car_type']
    car_name = request.form['car_name']
    car_model = request.form['car_model']
    year = int(request.form['year'])

    if car_type == 'Electric':
        battery_capacity = int(request.form['battery_capacity'])
        insert_car_information(car_type, car_name, car_model, year, battery_capacity=battery_capacity)
    elif car_type == 'Gas':
        fuel_efficiency = int(request.form['fuel_efficiency'])
        insert_car_information(car_type, car_name, car_model, year, fuel_efficiency=fuel_efficiency)


if __name__ == "__main__":
    app.run(debug=True)
