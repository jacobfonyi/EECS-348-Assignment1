from maxheap import MaxHeap
from patient import Patient
class Inbox:
    def __init__(self):
        self.heap = MaxHeap()
        self.arrival_count = 0

    def arrive(self, first_name, last_name, age, illness, severity):
        self.arrival_count += 1
        patient = Patient(first_name, last_name, age, illness, severity, self.arrival_count)
        self.heap.insert(patient)

    def next_patient(self):
        patient = self.heap.peek_max()
        if patient:
            print(f"Next patient:\n{patient}")
        else:
            print("No patients waiting.")

    def treat(self):
        patient = self.heap.extract_max()
        if patient:
            print(f"Treating patient:\n{patient}")
        else:
            print("No patients to treat.")

    def count(self):
        count = self.heap.size()
        print(f"There {'is' if count == 1 else 'are'} {count} patient{'s' if count != 1 else ''} waiting.\n")
