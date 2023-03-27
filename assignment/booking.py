import mysql.connector
from datetime import datetime

# Define the database connection details
config = {
    'user': 'root',
    'password': 'samsam',
    'host': 'localhost',
    'database': 'booking'
}

# Create a new database connection
def get_db():
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name TEXT,
    email TEXT(255) ,
    event TEXT,
    date DATE,
    quantity INTEGER
);


    ''')
    return db

# Create a new booking
def create_booking(name, email, event, date, quantity):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO bookings (name, email, event, date, quantity) VALUES (%s, %s, %s, %s, %s)',
                   (name, email, event, date, quantity))
    db.commit()
    db.close()

# Get all bookings for a particular event
def get_bookings(event):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM bookings WHERE event = %s', (event,))
    bookings = cursor.fetchall()
    db.close()
    return bookings

# Check if a booking already exists for the given email and event
def booking_exists(email, event, date):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT COUNT(*) FROM bookings WHERE email = %s AND event = %s AND date = %s',(email, event, date))
    result = cursor.fetchone()
    db.close()
    return result[0] > 0

# Validate the booking details
def validate_booking(name, email, event, date, quantity):
    errors = []
    # Check if name is not empty
    if not name:
        errors.append('Name cannot be empty')
    # Check if email is valid
    if not email:
        errors.append('Email cannot be empty')
    elif not '@' in email or not '.' in email:
        errors.append('Invalid email')
    # Check if event is not empty
    if not event:
        errors.append('Event cannot be empty')
    # Check if date is not empty and is in the correct format
    if not date:
        errors.append('Date cannot be empty')
    else:
        try:
            datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            errors.append('Invalid date format. Must be YYYY-MM-DD')
    # Check if quantity is not empty and is greater than 0
    if not quantity or int(quantity) < 1:
        errors.append('Quantity must be greater than 0')
    return errors

# Main function to create a new booking
def main():
    print('Welcome to the online booking system.')
    print('Please enter your details below.')
    # Get the user's details
    name = input('Name: ')
    email = input('Email: ')
    event = input('Event: ')
    date = input('Date (YYYY-MM-DD): ')
    quantity = input('Quantity: ')
    # Validate the details
    errors = validate_booking(name, email, event, date, quantity)
    if errors:
        print('The following errors were found:')
        for error in errors:
            print('- ' + error)
        return
    # Check if a booking already exists
    if booking_exists(email, event, date):
        print('A booking already exists for this email address and event on this date.')
        return
    # Create the booking
    create_booking(name, email, event, date, quantity)
    print('Booking created successfully.')
    bookings = get_bookings(event)
    print('Bookings for ' + event + ':')
    for booking in bookings:
        print(booking)

if __name__ == '__main__':
    main()
