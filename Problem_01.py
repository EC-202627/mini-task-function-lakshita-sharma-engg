M = input()
N = int(input())

def calculate_fine(name, days):
    fine = days * 5
    
    if fine > 150:
        fine = 150
        print("You have accumulated the maximum fine of INR: 150.0")
    
    print("Book:", name)
    print("Days overdue:", days)
    print("Fine: Rs.", float(fine))

calculate_fine(M, N) 
