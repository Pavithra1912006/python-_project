import os
import django
from django.conf import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hospitalmanagement.settings')
django.setup()

from mongoengine import connect
from hospital.mongo_models import MongoDoctor
from django.contrib.auth.models import User
from hospital.models import Doctor

def test_doctor_storage():
    try:
        # Connect to MongoDB
        connect('hospital_management', host='localhost', port=27017)
        print("Successfully connected to MongoDB!")

        # Create a test user
        test_user = User.objects.create_user(
            username='testdoctor',
            password='testpass123',
            first_name='Test',
            last_name='Doctor'
        )

        # Create a test doctor in Django
        test_doctor = Doctor.objects.create(
            user=test_user,
            address='123 Test St',
            mobile='1234567890',
            department='Cardiologist',
            status=True
        )

        # Create the same doctor in MongoDB
        mongo_doctor = MongoDoctor(
            user_id=str(test_user.id),
            address='123 Test St',
            mobile='1234567890',
            department='Cardiologist',
            status=True
        )
        mongo_doctor.save()
        print("Successfully created test doctor in MongoDB!")

        # Verify the doctor exists in MongoDB
        found_doctor = MongoDoctor.objects(user_id=str(test_user.id)).first()
        if found_doctor:
            print(f"Found doctor in MongoDB: {found_doctor.department}")
        else:
            print("Doctor not found in MongoDB!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Clean up test data
        try:
            MongoDoctor.objects(user_id=str(test_user.id)).delete()
            test_user.delete()
            print("Test data cleaned up successfully")
        except Exception as e:
            print(f"Error during cleanup: {str(e)}")

if __name__ == "__main__":
    test_doctor_storage() 