import csv
from faker import Faker
import random
from google.colab import auth
# Initialize Faker
fake = Faker()

FILENAME = "employees_10.csv"
NUM_RECORDS = 10000

def generate_large_dataset():
    print(f"Generating {NUM_RECORDS} records... please wait.")

    with open(FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Header
        writer.writerow(["first_name", "last_name", "salary", "location", "department_id", "password"])

        for i in range(1, NUM_RECORDS + 1):
            # Generating realistic synthetic data
            first_name = fake.first_name()
            last_name = fake.last_name()
            # Generate location as a single city name without commas or special characters
            location = fake.city()

            # Salary: Randomized between 40k and 180k
            salary = random.randint(40000, 180000)

            # Department ID: Randomly assigned from a pool of 20 departments
            dept_id = random.randint(100, 120)

            # Generate an alphanumeric password
            password = fake.password(special_chars=False)

            writer.writerow([first_name, last_name, salary, location, dept_id, password])

            # Progress print every 2000 records
            if i % 2000 == 0:
                print(f"Status: {i} records written...")

    print(f"\nDone! Created '{FILENAME}'.")

auth.authenticate_user()
project_id = 'keen-phalanx-491113-c1'
!gcloud config set project keen-phalanx-491113-c1
bucket_name = "etlproj1-employeerawdata"

!gcloud storage cp employees_10.csv gs://etlproj1-employeerawdata/



if __name__ == "__main__":
    generate_large_dataset()
