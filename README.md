# Mechanic Shop API

Welcome to the **Mechanic Shop API**, a Flask-based RESTful API for managing customers, vehicles, mechanics, services, and service tickets in a mechanic shop.

## Features

- **Customers**: Manage customer information (CRUD operations).
- **Vehicles**: Manage vehicle details (CRUD operations).
- **Mechanics**: Manage mechanic profiles (CRUD operations).
- **Services**: Manage services offered by the shop (CRUD operations).
- **Service Tickets**: Create and retrieve service tickets for vehicles.

## Project Structure

```
/pthon-API/
├── app/
│   ├── __init__.py                # App initialization and blueprint registration
│   ├── routes/
│   │   ├── customers.py           # Customer routes
│   │   ├── vehicles.py            # Vehicle routes
│   │   ├── services.py            # Service routes
│   ├── mechanic/
│   │   ├── __init__.py            # Mechanic blueprint initialization
│   │   ├── routes.py              # Mechanic routes
│   │   ├── schemas.py             # Mechanic schema
│   ├── service_ticket/
│   │   ├── __init__.py            # Service ticket blueprint initialization
│   │   ├── routes.py              # Service ticket routes
│   │   ├── schemas.py             # Service ticket schema
├── main.py                        # Entry point for the application
├── README.md                      # Project documentation
```

## Setup Instructions

### Prerequisites

- Python 3.9 or higher
- `pip` (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd /Python/pthon-API
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask marshmallow
   ```

4. Run the application:
   ```bash
   python main.py
   ```

5. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Customers

- **GET /customers**: Retrieve all customers.
- **POST /customers**: Add a new customer.
- **GET /customers/<id>**: Retrieve a specific customer.
- **PUT /customers/<id>**: Update a specific customer.
- **DELETE /customers/<id>**: Delete a specific customer.

### Vehicles

- **GET /vehicles**: Retrieve all vehicles.
- **POST /vehicles**: Add a new vehicle.
- **GET /vehicles/<id>**: Retrieve a specific vehicle.
- **PUT /vehicles/<id>**: Update a specific vehicle.
- **DELETE /vehicles/<id>**: Delete a specific vehicle.

### Mechanics

- **GET /mechanics**: Retrieve all mechanics.
- **POST /mechanics**: Add a new mechanic.
- **PUT /mechanics/<id>**: Update a specific mechanic.
- **DELETE /mechanics/<id>**: Delete a specific mechanic.

### Services

- **GET /services**: Retrieve all services.
- **POST /services**: Add a new service.
- **GET /services/<id>**: Retrieve a specific service.
- **PUT /services/<id>**: Update a specific service.
- **DELETE /services/<id>**: Delete a specific service.

### Service Tickets

- **GET /service-tickets**: Retrieve all service tickets.
- **POST /service-tickets**: Create a new service ticket.

## Testing with Postman

1. Import the API endpoints into Postman.
2. Use the following headers for POST and PUT requests:
   ```
   Content-Type: application/json
   ```
3. Example JSON payloads:
   - **POST /customers**:
     ```json
     {
       "id": 3,
       "name": "Alice Doe",
       "email": "alice.doe@example.com"
     }
     ```
   - **POST /vehicles**:
     ```json
     {
       "id": 3,
       "make": "Ford",
       "model": "Focus",
       "year": 2021,
       "owner_id": 3
     }
     ```

## Simulated Data

The API comes preloaded with simulated data for testing. You can retrieve this data using the `GET` endpoints.

## Future Enhancements

- Add database integration (e.g., SQLite or PostgreSQL).
- Implement authentication and authorization.
- Add pagination for large datasets.
- Improve input validation with Marshmallow schemas.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy using the Mechanic Shop API! If you have any questions or need further assistance, feel free to reach out.
