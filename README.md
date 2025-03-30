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

🚙 **Vehicle Management**
- Comprehensive vehicle tracking
- Service history logging
- Multiple vehicles per customer

👨‍🔧 **Mechanic Management**
- Skill tracking and specializations
- Work schedule management
- Performance monitoring

🛠️ **Service Management**
- Customizable service catalog
- Pricing management
- Service categorization

📋 **Service Tickets**
- Real-time status tracking
- Detailed service records
- Automated notifications

## 📁 Project Structure

```bash
📦 pthon-API
 ┣ 📂 app
 ┃ ┣ 📂 auth                  # Authentication module
 ┃ ┣ 📂 customers            # Customer management
 ┃ ┃ ┣ 📜 models.py
 ┃ ┃ ┣ 📜 routes.py
 ┃ ┃ ┗ 📜 schemas.py
 ┃ ┣ 📂 vehicles             # Vehicle management
 ┃ ┃ ┣ 📜 models.py
 ┃ ┃ ┣ 📜 routes.py
 ┃ ┃ ┗ 📜 schemas.py
 ┃ ┣ 📂 services             # Service catalog
 ┃ ┃ ┣ 📜 models.py
 ┃ ┃ ┣ 📜 routes.py
 ┃ ┃ ┗ 📜 schemas.py
 ┃ ┣ 📂 mechanic             # Mechanic management
 ┃ ┃ ┣ 📜 models.py
 ┃ ┃ ┣ 📜 routes.py
 ┃ ┃ ┗ 📜 schemas.py
 ┃ ┣ 📂 service_ticket       # Service tickets
 ┃ ┃ ┣ 📜 models.py
 ┃ ┃ ┣ 📜 routes.py
 ┃ ┃ ┗ 📜 schemas.py
 ┃ ┣ 📜 extensions.py        # Flask extensions
 ┃ ┗ 📜 __init__.py          # App initialization
 ┣ 📜 main.py                # Application entry point
 ┣ 📜 requirements.txt       # Dependencies
 ┗ 📜 README.md              # Documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Virtual environment (recommended)

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

4. Set up environment variables
```bash
# Copy the example .env file
cp .env.example .env

# Edit .env with your settings
# Make sure to change JWT_SECRET_KEY in production!
```

### Development
Run the development server:
```bash
python main.py
```

### Production Deployment
For production, use gunicorn:
```bash
gunicorn wsgi:app
```

## 🔐 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection URL | `sqlite:///mechanic_shop.db` |
| `JWT_SECRET_KEY` | Secret key for JWT tokens | `CHANGE_THIS_IN_PRODUCTION` |
| `JWT_ACCESS_TOKEN_EXPIRES` | Token expiration in seconds | `3600` |
| `CACHE_TYPE` | Type of cache to use | `SimpleCache` |
| `CACHE_TIMEOUT` | Cache timeout in seconds | `300` |
| `REDIS_URL` | Redis URL for rate limiting | `memory://` |

## 🔌 API Endpoints

### 🧑‍💼 Customer Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/customers` | List all customers | ✅ |
| `POST` | `/customers` | Create new customer | ✅ |
| `GET` | `/customers/<id>` | Get customer details | ✅ |
| `PUT` | `/customers/<id>` | Update customer | ✅ |
| `DELETE` | `/customers/<id>` | Delete customer | ✅ |

### 🚗 Vehicle Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/vehicles` | List all vehicles | ✅ |
| `POST` | `/vehicles` | Register new vehicle | ✅ |
| `GET` | `/vehicles/<id>` | Get vehicle details | ✅ |
| `PUT` | `/vehicles/<id>` | Update vehicle | ✅ |
| `DELETE` | `/vehicles/<id>` | Delete vehicle | ✅ |

### 👨‍🔧 Mechanic Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/mechanics` | List all mechanics | ✅ |
| `POST` | `/mechanics` | Add new mechanic | ✅ |
| `GET` | `/mechanics/<id>` | Get mechanic details | ✅ |
| `PUT` | `/mechanics/<id>` | Update mechanic | ✅ |
| `DELETE` | `/mechanics/<id>` | Delete mechanic | ✅ |

### 🛠️ Service Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/services` | List all services | ✅ |
| `POST` | `/services` | Add new service | ✅ |
| `GET` | `/services/<id>` | Get service details | ✅ |
| `PUT` | `/services/<id>` | Update service | ✅ |
| `DELETE` | `/services/<id>` | Delete service | ✅ |

### 📋 Service Ticket Endpoints
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/service-tickets` | List all tickets | ✅ |
| `POST` | `/service-tickets` | Create new ticket | ✅ |
| `GET` | `/service-tickets/<id>` | Get ticket details | ✅ |
| `PUT` | `/service-tickets/<id>` | Update ticket | ✅ |
| `DELETE` | `/service-tickets/<id>` | Delete ticket | ✅ |

## 🔒 Security Features

- **JWT Authentication**: Secure endpoint access
- **Rate Limiting**: Prevent API abuse
- **Input Validation**: Schema-based validation
- **SQL Injection Protection**: Using SQLAlchemy ORM
- **Password Hashing**: Secure credential storage
- **CORS Protection**: Configurable origins

## 📈 Performance Features

- **Response Caching**: Optimized data retrieval
- **Database Connection Pooling**: Efficient DB connections
- **Lazy Loading**: Smart relationship loading
- **Query Optimization**: Efficient database queries
- **Async Support**: Non-blocking operations

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
