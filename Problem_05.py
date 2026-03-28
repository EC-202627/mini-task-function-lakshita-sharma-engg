def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    
    if fine > max_fine:
        fine = max_fine
    
    print(f"Book: {book_title}")
    print(f"Days overdue: {days_overdue}")
    print(f"Fine: Rs. {fine}")

data = input().split()
book_title = " ".join(data[:-3])
days_overdue = int(data[-3])
daily_rate = float(data[-2])
max_fine = float(data[-1])

calculate_fine(book_title, days_overdue, daily_rate, max_fine)
