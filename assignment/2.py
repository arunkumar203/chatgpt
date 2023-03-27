import unittest
from datetime import datetime
from booking import validate_booking

class TestBookingSystem(unittest.TestCase):

    def test_validate_booking_with_valid_details(self):
        name = 'John'
        email = 'john@example.com'
        event = 'Concert'
        date = '2022-05-15'
        quantity = '2'

        errors = validate_booking(name, email, event, date, quantity)

        if len(errors) > 0:
            print(f"Error in test_validate_booking_with_valid_details: {errors}")
        self.assertEqual(len(errors), 0)

    def test_validate_booking_with_empty_name(self):
        name = ''
        email = 'john@example.com'
        event = 'Concert'
        date = '2022-05-15'
        quantity = '2'

        errors = validate_booking(name, email, event, date, quantity)

        if len(errors) > 0:
            print(f"Error in test_validate_booking_with_empty_name: {errors}")
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Name cannot be empty')

    def test_validate_booking_with_invalid_email(self):
        name = 'John'
        email = 'johnexample.com'
        event = 'Concert'
        date = '2022-05-15'
        quantity = '2'

        errors = validate_booking(name, email, event, date, quantity)

        if len(errors) > 0:
            print(f"Error in test_validate_booking_with_invalid_email: {errors}")
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Invalid email')

    def test_validate_booking_with_empty_event(self):
        name = 'John'
        email = 'john@example.com'
        event = ''
        date = '2022-05-15'
        quantity = '2'

        errors = validate_booking(name, email, event, date, quantity)

        if len(errors) > 0:
            print(f"Error in test_validate_booking_with_empty_event: {errors}")
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Event cannot be empty')

    def test_validate_booking_with_empty_date(self):
        name = 'John'
        email = 'john@example.com'
        event = 'Concert'
        date = ''
        quantity = '2'

        errors = validate_booking(name, email, event, date, quantity)

        if len(errors) > 0:
            print(f"Error in test_validate_booking_with_empty_date: {errors}")
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Date cannot be empty')

    def test_validate_booking_with_invalid_date_format(self):
        name = 'John'
        email = 'john@example.com'
        event = 'Concert'
        date = '2022/05/15'
        quantity = '2'

        errors = validate_booking(name, email, event, date, quantity)

        if len(errors) > 0:
            print(f"Error in test_validate_booking_with_invalid_date_format: {errors}")
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0], 'Invalid date format. Must be YYYY-MM-DD')



if __name__ == '__main__':
    unittest.main()
