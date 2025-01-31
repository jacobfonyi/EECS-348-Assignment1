#EECS 348 Assignment 1 Driver File
#CEO Email prioritization program
#Input: test file named Assignment1_Test_File.txt
#Outputs: Read Test file that is sent to appropiate class 



from hospital import Hospital

def main():
    filename = input("Enter file: ")
    hospital = Hospital()
    with open(filename, 'r') as file:
        for line in file:
            command = line.strip().split(maxsplit=1)
            if command[0] == "EMAIL":
                _, details = command
                sender_category, subject_line, date = details.split(maxsplit=3)
                hospital.arrive(first_name, last_name, int(age), illness, int(severity))
            elif command[0] == "NEXT":
                inbox.next_email()
            elif command[0] == "READ":
                inbox.read()
            elif command[0] == "COUNT":
                inbox.count()
                
if __name__ == "__main__":
    main()
