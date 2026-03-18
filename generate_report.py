from fpdf import FPDF
import csv

# Step 1: Read data from CSV
data = []
with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data.append(row)

# Step 2: Analyze data
total_score = 0
for row in data:
    total_score += int(row['Score'])
average_score = total_score / len(data)

# Step 3: Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)

pdf.cell(0, 10, "Student Report", ln=True, align="C")
pdf.ln(10)

# Add student data
pdf.set_font("Arial", '', 12)
for row in data:
    pdf.cell(0, 10, f"Name: {row['Name']}, Age: {row['Age']}, City: {row['City']}, Score: {row['Score']}", ln=True)

pdf.ln(10)
pdf.cell(0, 10, f"Average Score: {average_score:.2f}", ln=True)

# Save PDF
pdf.output("report.pdf")
print("PDF report created successfully! File name: report.pdf")