from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database Connection using .env
mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
mycursor = mydb.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/flights')
def flights():
    mycursor.execute("SELECT * FROM flights")
    all_flights = mycursor.fetchall()
    return render_template('flights.html', flights=all_flights)

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        source = request.form['source']
        destination = request.form['destination']

        query = "INSERT INTO bookings (name, email, date, source, destination) VALUES (%s, %s, %s, %s, %s)"
        values = (name, email, date, source, destination)
        mycursor.execute(query, values)
        mydb.commit()

        return redirect('/confirmation')
    return render_template('index.html')

@app.route('/book-flight', methods=['POST'])
def book_flight():
    data = request.get_json()
    flight_number = data['flight_number']
    num_seats = int(data['num_seats'])

    mycursor.execute("SELECT available_seats FROM flights WHERE flight_number = %s", (flight_number,))
    flight = mycursor.fetchone()

    if not flight:
        return jsonify({"message": "Flight not found!"}), 404

    if flight['available_seats'] < num_seats:
        return jsonify({"message": "Not enough seats available!"}), 400

    new_seats = flight['available_seats'] - num_seats
    mycursor.execute("UPDATE flights SET available_seats = %s WHERE flight_number = %s", (new_seats, flight_number))
    mydb.commit()

    return jsonify({"message": "Flight booked successfully!", "updated_seats": new_seats})

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)
