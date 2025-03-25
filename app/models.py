from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, Date
from sqlalchemy.orm import relationship
from app.extensions import db

class Customer(db.Model):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('customer.id'), nullable=False)

class Service(db.Model):
    __tablename__ = 'service'
    id = Column(Integer, primary_key=True)
    description = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)

class Mechanic(db.Model):
    __tablename__ = 'mechanic'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    specialization = Column(String(100), nullable=False)

service_ticket_mechanic = Table(
    'service_ticket_mechanic',
    db.metadata,
    Column('service_ticket_id', Integer, ForeignKey('service_ticket.id'), primary_key=True),
    Column('mechanic_id', Integer, ForeignKey('mechanic.id'), primary_key=True)
)

class ServiceTicket(db.Model):
    __tablename__ = 'service_ticket'
    id = Column(Integer, primary_key=True)
    VIN = Column(String(17), nullable=False)
    service_date = Column(Date, nullable=False)
    service_description = Column(String(200), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    mechanics = relationship('Mechanic', secondary=service_ticket_mechanic, back_populates='service_tickets')

Mechanic.service_tickets = relationship(
    'ServiceTicket', secondary=service_ticket_mechanic, back_populates='mechanics'
)
