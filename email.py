class Email:
    def sender_priority():
        return {
            "Boss": 5,
            "Subordinate": 4,
            "Peer": 3,
            "ImportantPerson": 2,
            "OtherPerson": 1
            }
    
    def __init__(self, sender_category, subject_line, date):
        self.sender_category = sender_category 
        self.subject_line = subject_line
        self.date = self.process_date(date)
        self.priority = self.sender_priority()[sender_category]

    
    def process_date(self, date_str): #chatgpt
        month, day, year = map(int, date_str.split('-'))
        return year * 10000 + month * 100 + day
    
    def __lt__(self, other):
        # Higher priority emails should come first
        if self.priority == other.priority:
            return self.date > other.date  # Newer emails first
        return self.priority > other.priority

    def __repr__(self):
        return f"Sender: {self.sender_category}\nSubject: {self.subject_line}\nDate: {self.date // 10000}-{(self.date // 100) % 100}-{self.date % 100}\n"
