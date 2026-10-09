
class Doctor:
    def treat(self):
        print("Мой метод лечения: общий")


class Surgeon(Doctor):
    def treat(self):
        print(f"Мой метод лечения: метод 1")


class Dentist(Doctor):
    def treat(self):
        print("Мой метод лечения: метод 2")


class Therapist(Doctor):
    def treat(self):
        print("Мой метод лечения: метод 3")

    def assign_doctor(self, patient):
        plan = patient.treatment_plan
        if plan == 1:
            patient.doctor = Surgeon()
        elif plan == 2:
            patient.doctor = Dentist()
        else:
            patient.doctor = Therapist()


class Patient:
    def __init__(self, treatment_plan):
        self.treatment_plan = treatment_plan



therapist = Therapist()

Ivan = Patient(3)


therapist.assign_doctor(Ivan)


Ivan.doctor.treat()

# без подсказок ИИ тоже не решила бы((( обращалась за наводящими вопросами