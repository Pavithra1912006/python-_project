import os
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
django.setup()

from mongoengine import connect, disconnect
from mongo_models import MongoDoctor, MongoPatient, MongoAppointment
import datetime

def test_mongodb_connection():
    try:
        # Connect to MongoDB
        connect('hospital_management', host='localhost', port=27017)
        print("Successfully connected to MongoDB!")

        # Create a test doctor
        test_doctor = MongoDoctor(
            user_id="test_user_1",
            address="123 Test Street",
            mobile="1234567890",
            department="Cardiologist",
            status=True
        )
        test_doctor.save()
        print("Successfully created test doctor!")

        # Create a test patient
        test_patient = MongoPatient(
            user_id="test_user_2",
            address="456 Test Avenue",
            mobile="9876543210",
            symptoms="Test symptoms",
            assigned_doctor_id="test_user_1",
            status=True
        )
        test_patient.save()
        print("Successfully created test patient!")

        # Create a test appointment
        test_appointment = MongoAppointment(
            patient_id="test_user_2",
            doctor_id="test_user_1",
            appointment_date=datetime.datetime.now(),
            description="Test appointment",
            status=True
        )
        test_appointment.save()
        print("Successfully created test appointment!")

        # Query and display the data
        print("\nDoctors in database:")
        for doctor in MongoDoctor.objects:
            print(f"Doctor: {doctor.user_id}, Department: {doctor.department}")

        print("\nPatients in database:")
        for patient in MongoPatient.objects:
            print(f"Patient: {patient.user_id}, Symptoms: {patient.symptoms}")

        print("\nAppointments in database:")
        for appointment in MongoAppointment.objects:
            print(f"Appointment: Doctor {appointment.doctor_id} with Patient {appointment.patient_id}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Clean up test data
        MongoDoctor.objects(user_id="test_user_1").delete()
        MongoPatient.objects(user_id="test_user_2").delete()
        MongoAppointment.objects(patient_id="test_user_2").delete()
        disconnect()

if __name__ == "__main__":
    test_mongodb_connection() 