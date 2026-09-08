import csv  
from datetime import datetime

# generate report
filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"
with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["ID", "Status"])
    # Write mock data
    writer.writerow([1, "Completed"])  

print(f"Report saved as: {filename}") 