class Email:
    def __init__(self, sender_category, subject_line, date,):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.illness = illness
        self.severity = severity
        self.arrival_order = arrival_order

    def __str__(self):
        return (f"ame: {self.last_name}, {self.first_name}\n"
                f"Age: {self.age}\n"
                f"Suffers from: {self.illness}\n"
                f"Illness severity: {self.severity}\n"
                f"Arrival order: {self.arrival_order}\n")
