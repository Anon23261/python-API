<div align="center">

# 🔧 Mechanic Shop API 🚗

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.0.2-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)

🏎️ A modern, high-performance RESTful API for managing your auto repair shop operations. Built with Flask and love! 💝

</div>

## ✨ Features

🧑‍💼 **Customer Management**
- Track customer details and history
- Seamless CRUD operations
- Secure data handling
- Preferred mechanics selection
- Vehicle ownership tracking

🚙 **Vehicle Management**
- Comprehensive vehicle tracking
- Service history logging
- Multiple vehicles per customer
- Detailed service records
- Mileage tracking

👨‍🔧 **Mechanic Management**
- Skill tracking and specializations
- Work schedule management
- Performance monitoring
- Tool certifications
- Customer preferences tracking

🛠️ **Service Management**
- Customizable service catalog
- Dynamic pricing with parts
- Service categorization
- Required tools tracking
- Parts inventory management

📋 **Service Tickets**
- Real-time status tracking
- Detailed service records
- Automated notifications
- Cost estimation and tracking
- Service history integration

## 📁 Project Structure

```bash
📦 pthon-API
 ┣ 📂 app
 ┃ ┣ 📂 auth                  # Authentication module
 ┃ ┣ 📂 blueprints           # API blueprints
 ┃ ┃ ┣ 📂 customers          # Customer management
 ┃ ┃ ┣ 📂 vehicles           # Vehicle management
 ┃ ┃ ┣ 📂 services           # Service catalog
 ┃ ┃ ┣ 📂 mechanics          # Mechanic management
 ┃ ┃ ┣ 📂 service_tickets    # Service tickets
 ┃ ┃ ┣ 📂 models             # Common models
 ┃ ┃ ┗ 📜 associations.py    # Many-to-many relationships
 ┃ ┣ 📂 common               # Common utilities
 ┃ ┃ ┣ 📜 models.py         # Base model class
 ┃ ┃ ┗ 📜 utils.py          # Utility functions
 ┃ ┣ 📜 extensions.py        # Flask extensions
 ┃ ┗ 📜 __init__.py         # App initialization
 ┣ 📜 wsgi.py               # Application entry point
 ┣ 📜 config.py             # Configuration
 ┣ 📜 requirements.txt      # Dependencies
 ┗ 📜 README.md             # Documentation
```

## 🔄 Database Relationships

### Many-to-Many Relationships
- **Mechanic-Specialization**: Mechanics can have multiple specializations
- **Service-Parts**: Services require multiple parts with quantities
- **Vehicle-Service History**: Tracks services performed on vehicles
- **Customer-Preferred Mechanics**: Customers can have preferred mechanics
- **Service-Required Tools**: Services require specific tools
- **Mechanic-Tool Certifications**: Mechanics are certified for specific tools

### One-to-Many Relationships
- Customer -> Vehicles
- Customer -> Service Tickets
- Vehicle -> Service Tickets
- Mechanic -> Service Tickets
- Service -> Service Tickets

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Virtual environment (recommended)
- SQLite (default) or PostgreSQL

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/mechanic-shop-api.git
cd mechanic-shop-api
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables in `.env`:
```bash
FLASK_APP=wsgi.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///app.db
JWT_SECRET_KEY=your-jwt-secret
```

5. Initialize the database
```bash
flask db init
flask db migrate
flask db upgrade
```

6. Run the application
```bash
flask run
```

## 🔐 Authentication

The API uses JWT (JSON Web Token) authentication. To access protected endpoints:

1. Register a new user or login
2. Use the returned JWT token in the Authorization header:
```
Authorization: Bearer <your-jwt-token>
```

## 📚 API Documentation

### Customer Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/auth/register` | Register new customer | ❌ |
| `POST` | `/auth/login` | Login customer | ❌ |
| `GET` | `/customers` | List all customers | ✅ |
| `GET` | `/customers/<id>` | Get customer details | ✅ |
| `PUT` | `/customers/<id>` | Update customer | ✅ |
| `DELETE` | `/customers/<id>` | Delete customer | ✅ |
| `POST` | `/customers/<id>/preferred-mechanics` | Add preferred mechanic | ✅ |

### Vehicle Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/vehicles` | List all vehicles | ✅ |
| `POST` | `/vehicles` | Add new vehicle | ✅ |
| `GET` | `/vehicles/<id>` | Get vehicle details | ✅ |
| `PUT` | `/vehicles/<id>` | Update vehicle | ✅ |
| `DELETE` | `/vehicles/<id>` | Delete vehicle | ✅ |
| `GET` | `/vehicles/<id>/service-history` | Get service history | ✅ |

### Mechanic Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/mechanics` | List all mechanics | ✅ |
| `POST` | `/mechanics` | Add new mechanic | ✅ |
| `GET` | `/mechanics/<id>` | Get mechanic details | ✅ |
| `PUT` | `/mechanics/<id>` | Update mechanic | ✅ |
| `DELETE` | `/mechanics/<id>` | Delete mechanic | ✅ |
| `GET` | `/mechanics/<id>/specializations` | Get specializations | ✅ |
| `POST` | `/mechanics/<id>/certifications` | Add tool certification | ✅ |

### Service Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/services` | List all services | ✅ |
| `POST` | `/services` | Add new service | ✅ |
| `GET` | `/services/<id>` | Get service details | ✅ |
| `PUT` | `/services/<id>` | Update service | ✅ |
| `DELETE` | `/services/<id>` | Delete service | ✅ |
| `GET` | `/services/<id>/required-parts` | Get required parts | ✅ |
| `GET` | `/services/<id>/required-tools` | Get required tools | ✅ |

### Service Ticket Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/service-tickets` | List all tickets | ✅ |
| `POST` | `/service-tickets` | Create ticket | ✅ |
| `GET` | `/service-tickets/<id>` | Get ticket details | ✅ |
| `PUT` | `/service-tickets/<id>` | Update ticket | ✅ |
| `DELETE` | `/service-tickets/<id>` | Delete ticket | ✅ |
| `PUT` | `/service-tickets/<id>/status` | Update status | ✅ |

## 📦 Models

### Customer
- id: Integer (Primary Key)
- name: String
- email: String (Unique)
- phone: String
- address: String
- preferred_mechanics: Relationship (Many-to-Many with Mechanic)
- vehicles: Relationship (One-to-Many with Vehicle)
- service_tickets: Relationship (One-to-Many with ServiceTicket)

### Vehicle
- id: Integer (Primary Key)
- make: String
- model: String
- year: Integer
- vin: String (Unique)
- license_plate: String
- color: String
- mileage: Integer
- last_service_date: DateTime
- owner: Relationship (Many-to-One with Customer)
- service_history: Relationship (Many-to-Many with Service)

### Mechanic
- id: Integer (Primary Key)
- name: String
- email: String (Unique)
- phone: String
- hourly_rate: Float
- years_of_experience: Integer
- specializations: Relationship (Many-to-Many with Specialization)
- certified_tools: Relationship (Many-to-Many with Tool)
- service_tickets: Relationship (One-to-Many with ServiceTicket)

### Service
- id: Integer (Primary Key)
- name: String
- description: Text
- base_price: Float
- estimated_hours: Float
- complexity_level: Integer
- is_diagnostic: Boolean
- required_parts: Relationship (Many-to-Many with Part)
- required_tools: Relationship (Many-to-Many with Tool)

### ServiceTicket
- id: Integer (Primary Key)
- description: Text
- status: String
- scheduled_date: DateTime
- completion_date: DateTime
- estimated_cost: Float
- final_cost: Float
- diagnostic_notes: Text
- completion_notes: Text
- priority: Integer
- customer: Relationship (Many-to-One with Customer)
- vehicle: Relationship (Many-to-One with Vehicle)
- mechanic: Relationship (Many-to-One with Mechanic)
- service: Relationship (Many-to-One with Service)

## 🛠️ Development

### Running Tests
```bash
pytest
```

### Code Style
The project follows the Black code style. Format your code with:
```bash
black .
```

### Database Migrations
After model changes:
```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
