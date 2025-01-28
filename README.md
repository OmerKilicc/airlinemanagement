# Airline Management System

A Django REST API-based airline management system that handles airplanes, flights, and reservations.

## Features

- **Airplane Management**
  - Create, read, update, and delete airplane records
  - Track airplane details (tail number, model, capacity, production year)
  - Monitor airplane status
  - View all flights associated with an airplane

- **Flight Management**
  - Manage flight schedules and details
  - Track departure and arrival locations
  - Handle flight timings
  - Associate flights with specific airplanes
  - View all reservations for a specific flight
  - Advanced filtering by date, location, and price range
  - Search flights by departure and destination cities

- **Reservation System**
  - Create and manage passenger reservations
  - Automatic reservation code generation
  - Email notification system
    - Booking confirmation emails
  - Prevent overbooking with capacity checks

## API Endpoints

### Airplanes
- `GET /api/airplanes/` - List all airplanes
- `POST /api/airplanes/` - Create a new airplane
- `GET /api/airplanes/{id}/` - Retrieve airplane details
- `PATCH /api/airplanes/{id}/` - Update airplane details
- `DELETE /api/airplanes/{id}/` - Delete an airplane
- `GET /api/airplanes/{id}/flights/` - List all flights for an airplane

### Flights
- `GET /api/flights/` - List all flights
  - Query Parameters:
    - `departure`: Filter by departure city
    - `destination`: Filter by destination city
    - `date_from`: Filter flights after this date
    - `date_to`: Filter flights before this date

- `POST /api/flights/` - Create a new flight
- `GET /api/flights/{id}/` - Retrieve flight details
- `PATCH /api/flights/{id}/` - Update flight details
- `DELETE /api/flights/{id}/` - Delete a flight
- `GET /api/flights/{id}/reservations/` - List all reservations for a flight

### Reservations
- `GET /api/reservations/` - List all reservations
- `POST /api/reservations/` - Create a new reservation
- `GET /api/reservations/{id}/` - Retrieve reservation details
- `PATCH /api/reservations/{id}/` - Update reservation details

## Technology Stack

- Python 3.13
- Django 5.1.5
- Django REST Framework
- Django Filters
- SQLite (Database)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd airlinemanagement
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Apply migrations:
```bash
python manage.py migrate
```

5. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`

## Models

### Airplane
- `tail_number` (CharField): Unique identifier for the airplane
- `model` (CharField): Aircraft model
- `capacity` (IntegerField): Passenger capacity
- `production_year` (IntegerField): Year of manufacture
- `status` (BooleanField): Current operational status

### Flight
- `flight_number` (CharField): Unique flight identifier
- `departure` (CharField): Departure location
- `destination` (CharField): Arrival location
- `departure_time` (DateTimeField): Scheduled departure time
- `arrival_time` (DateTimeField): Scheduled arrival time
- `airplane` (ForeignKey): Associated aircraft

### Reservation
- `passenger_name` (CharField): Name of the passenger
- `passenger_email` (EmailField): Contact email
- `reservation_code` (CharField): Unique reservation identifier
- `flight` (ForeignKey): Associated flight
- `status` (BooleanField): Reservation status

## Error Handling

- The system includes validation for:
  - Preventing overbooking beyond airplane capacity
  - Ensuring unique reservation codes
  - Validating email addresses
  - Checking flight availability
