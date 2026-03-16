CREATE DATABASE IF NOT EXISTS flight_booking_2232;
USE flight_booking_2232;

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    date DATE,
    source VARCHAR(100),
    destination VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20),
    departure_city VARCHAR(100),
    destination_city VARCHAR(100),
    departure_time VARCHAR(50),
    arrival_time VARCHAR(50),
    available_seats INT
);

-- Sample flight data
INSERT INTO flights (flight_number, departure_city, destination_city, departure_time, arrival_time, available_seats) VALUES
('AI101', 'Delhi', 'Mumbai', '06:00 AM', '08:00 AM', 120),
('AI202', 'Mumbai', 'Bangalore', '10:00 AM', '12:00 PM', 85),
('AI303', 'Delhi', 'Kolkata', '02:00 PM', '04:30 PM', 60),
('AI404', 'Chennai', 'Hyderabad', '05:00 PM', '06:30 PM', 95),
('AI505', 'Bangalore', 'Delhi', '08:00 PM', '10:30 PM', 110);
