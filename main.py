class Person:
    def __init__(self, name, lastname, phone_number):
        self._name = name
        self._lastname = lastname
        self._phone_number = phone_number

    @property
    def name(self):
        return self._name

    @property
    def lastname(self):
        return self._lastname

    @property
    def full_name(self):
        return f"{self._name} {self._lastname}"

    @property
    def phone_number(self):
        return self._phone_number

    def describe(self):
        return f"{self.full_name} | {self.phone_number}"



class Doctor(Person):
    def __init__(self, name, lastname, phone_number, specialty):
        super().__init__(name, lastname, phone_number)
        self._specialty = specialty

    @property
    def specialty(self):
        return self._specialty

    def describe(self):
        return f"{self.full_name} | {self.specialty} | {self.phone_number}"

    


class Patient(Person):
    def __init__(self, name, lastname, phone_number, symptom):
        super().__init__(name, lastname, phone_number)
        self._symptom = symptom

    @property
    def symptom(self):
        return self._symptom

    def describe(self):
        return f"{self.full_name} | {self.symptom} | {self.phone_number}"






def patient_intake():
    print("Patient Intake Form")
    name = input("First name: ")
    lastname = input("Last name: ")
    phone_number = input("Phone number: ")
    symptom = input("Symptom: ")
    patient = Patient(name, lastname, phone_number, symptom)

    
    return patient


def doctor_intake():
    print("Doctor Registration Form")
    name = input("First name: ")
    lastname = input("Last name: ")
    phone_number = input("Phone number: ")
    specialty = input("Specialty: ")
    return Doctor(name, lastname, phone_number, specialty)


def create_dummy_data():
    doctors = [
        Doctor("Sarah", "Miller", "555-0101", "Cardiology"),
        Doctor("James", "Brown", "555-0102", "Pediatrics"),
        Doctor("Emily", "Davis", "555-0103", "Dermatology"),
        Doctor("Robert", "Wilson", "555-0104", "Neurology"),
    ]

    patients = [
        Patient("John", "Smith", "555-0201", "Chest pain"),
        Patient("Anna", "Johnson", "555-0202", "Fever"),
        Patient("Michael", "Lee", "555-0203", "Headache"),
        Patient("Laura", "Clark", "555-0204", "Skin rash"),
    ]

    return doctors, patients


def list_people(title, people):
    print(title)
    for person in people:
        print("-", person.describe())


def show_menu():
    print()
    print("1. List doctors")
    print("2. List patients")
    print("3. Add doctor")
    print("4. Add patient")
    print("5. Exit")


if __name__ == "__main__":
    doctors, patients = create_dummy_data()

    while True:
        show_menu()
        choice = input("Choose an option: ")
        print()

        if choice == "1":
            list_people("Doctors:", doctors)
        elif choice == "2":
            list_people("Patients:", patients)
        elif choice == "3":
            doctors.append(doctor_intake())
            print("Doctor added.")
        elif choice == "4":
            patients.append(patient_intake())
            print("Patient added.")
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid option, try again.")
