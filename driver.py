#EECS 348 Assignment 1 Driver File
#CEO Email prioritization program
#Input: test file named Assignment1_Test_File.txt
#Outputs: Read Test file that is sent to appropiate class 



from maxheap import MaxHeap
from email import Email

def main():
    filename = input("Enter file: ")
    inbox = Inbox()
    with open(filename, 'r') as file:
        for line in file:
            command = line.strip().split(maxsplit=1)
            if command[0] == "EMAIL":
                _, details = command
                sender_category, subject_line, date = details.split(",", 2)
                maxheap.push(Email(sender_category, subject_line, date))
            elif command[0] == "NEXT":
                next_email = maxheap.peek()
                if next_email:
                    print("Next email:")
                    print(next_email)
                else:
                    print("No emails to read.")
            elif command[0] == "READ":
                maxheap.pop()
            elif command[0] == "COUNT":
                print(f"There are {self.maxheap.count()} email(s) to read.")
                
if __name__ == "__main__":
    main()
