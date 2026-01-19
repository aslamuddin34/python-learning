from datetime import datetime

# Get current time
now = datetime.now()

print("==============================")
print("   PYTHON SYSTEM REPORT")
print("==============================")
print(f"Date: {now.strftime('%A, %B %d, %Y')}")
print(f"Time: {now.strftime('%I:%M %p')}")
print("==============================")