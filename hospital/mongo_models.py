from mongoengine import Document, StringField, ReferenceField, DateTimeField, BooleanField, ImageField
from django.contrib.auth.models import User
import datetime

class MongoDoctor(Document):
    user_id = StringField(required=True)  # Reference to Django User model
    profile_pic = StringField()  # Store the path to the image
    address = StringField(max_length=40)
    mobile = StringField(max_length=20)
    department = StringField(max_length=50)
    status = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.datetime.now)

    meta = {
        'collection': 'doctors',
        'indexes': ['user_id']
    }

class MongoPatient(Document):
    user_id = StringField(required=True)  # Reference to Django User model
    address = StringField(max_length=40)
    mobile = StringField(max_length=40)
    symptoms = StringField(max_length=100)
    assigned_doctor_id = StringField()
    admit_date = DateTimeField(default=datetime.datetime.now)
    status = BooleanField(default=False)
    
    meta = {
        'collection': 'patients',
        'indexes': ['user_id', 'assigned_doctor_id']
    }

class MongoAppointment(Document):
    patient_id = StringField(required=True)
    doctor_id = StringField(required=True)
    appointment_date = DateTimeField()
    description = StringField()
    status = BooleanField(default=False)
    
    meta = {
        'collection': 'appointments',
        'indexes': ['patient_id', 'doctor_id', 'appointment_date']
    } 