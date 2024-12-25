# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 05:04:07 2024

@author: Madhu
"""

# from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

# Bank Account Opening and Closing Procedures


# Text content (replace this with the content you want in your PDF)
content = """

# Opening and Closing Accounts
At [Bank Name], we offer a wide range of accounts to meet the needs of our customers. This section outlines the procedures for opening and closing checking and savings accounts.

## 1 Opening a Checking Account
A checking account provides a convenient way for customers to manage their day-to-day finances. To open a checking account with [Bank Name], please follow the steps below:

### 1.1 Eligibility Criteria
  - Must be at least 18 years old.
  - Must provide valid government-issued identification (e.g., passport, driver’s license).
  - Proof of address (e.g., utility bill, lease agreement) for residents of the local area.
  - Social Security Number (SSN) or Taxpayer Identification Number (TIN).

### 1.2 Required Documents
  - Completed application form (available online or at any branch).
  - Valid ID.
  - Proof of address.
  - Proof of employment/income (if applicable).

### 1.3 Account Features
  - No minimum balance requirement (depending on the account type).
  - Access to checks and debit cards.
  - Online and mobile banking access.
  - Overdraft protection (if requested).
  - Monthly maintenance fee may apply (unless specific criteria are met).

### 1.4 Account Opening Process
  - Submit required documents to the bank’s representative.
  - Review and sign the account agreement.
  - Initial deposit of [$X] may be required.
  - Receive account details (account number, debit card, checkbook, etc.).

### 1.5 Account Activation
  - Your checking account will be activated within [X] business days after the initial deposit is processed.
  - You can immediately start using your account for transactions such as deposits, withdrawals, and bill payments.

## 2 Closing a Checking Account
If you wish to close your checking account, please follow these steps:

### 2.1 Account Balance
  - Ensure that your account balance is zero or that any outstanding payments are settled.
  - If applicable, transfer any remaining balance to another account.

### 2.2 Steps for Closing
  - Submit a request to close the account in writing or through online banking (if available).
  - Return all checks, debit cards, and other account-related materials to the bank.
  - Complete the necessary forms and sign the account closure agreement.

### 2.3 Final Statement and Fees
  - A final statement will be issued. Any applicable fees or charges will be deducted from the account balance.
  - Any unclaimed balance will be returned via check or electronic transfer to the designated address or account.

### 2.4 Post-Closure
  - After the account is closed, it may take up to [X] business days for the closure process to be fully completed.
  - You will receive confirmation of account closure once the process is complete.

## 3 Opening a Savings Account
A savings account is designed to help customers save money securely while earning interest. To open a savings account with [Bank Name], please follow these steps:

### 3.1 Eligibility Criteria
  - Must be at least 18 years old.
  - Valid government-issued identification.
  - Proof of address.
  - SSN or TIN.

### 3.2 Required Documents
  - Completed application form.
  - Valid ID and proof of address.
  - Deposit of minimum required balance (if applicable).

### 3.3 Account Features
  - Interest is earned on the balance (variable rate).
  - Monthly service fees may apply if the balance falls below a minimum threshold.
  - Withdrawals can be made at any time, though limits may apply on the number of transactions per month.

### 3.4 Account Opening Process
  - Submit all required documentation.
  - Make the required initial deposit.
  - Review and sign the savings account agreement.
  - Receive account details.

### 3.5 Interest Rates
  - Interest is compounded monthly, with rates varying depending on the account balance.

## 4 Closing a Savings Account
To close your savings account, follow these instructions:

### 4.1 Account Balance
  - Ensure that the account balance is zero or that any outstanding withdrawals or transactions are completed.
  - Transfer any remaining funds to another account.

### 4.2 Steps for Closing
  - Request closure in writing or via the bank’s online portal.
  - Return any savings account-related materials (such as passbooks, debit cards, etc.).
  - Complete and sign the account closure form.

### 4.3 Final Statement and Fees
  - A final account statement will be issued.
  - Any applicable fees or penalties will be deducted from the balance prior to account closure.

### 4.4 Post-Closure
  - Account closure confirmation will be sent within [X] business days.
  - Any remaining balance will be returned to you via check or transferred electronically.

# Contact Information
If you have any questions regarding the opening or closing of accounts, please contact us at:

- Phone: [Bank's Phone Number]
- Email: [Bank's Email Address]
- Website: [Bank's Website]
- Branch Locations: [List of branch addresses]
"""

# Function to create the PDF
def create_pdf_v1(content, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter

    # Set initial font and size
    c.setFont("Helvetica", 10)

    # Add the content to the PDF
    text_object = c.beginText(40, height - 40)
    text_object.setFont("Helvetica", 10)
    text_object.setTextOrigin(40, height - 40)
    
    # Add the content in paragraphs, preserving structure
    for line in content.split("\n"):
        text_object.textLine(line)

    # Draw the text to the PDF
    c.drawText(text_object)

    # Save the PDF file
    c.save()

# Call the function to create the PDF
# create_pdf(content, "C:/Users/Madhu/Downloads/Account_Opening_Closing_Guide.pdf")



def create_pdf_v2(content, filename):
    # Create a SimpleDocTemplate object to handle the PDF creation
    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Set up styles for the document
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    
    # Split the content into paragraphs (each paragraph separated by a blank line)
    content_paragraphs = [Paragraph(line, normal_style) for line in content.split("\n") if line.strip()]

    # Build the PDF
    doc.build(content_paragraphs)

# create_pdf(content, "C:/Users/Madhu/Downloads/Account_Opening_Closing_Guide.pdf")




def create_pdf(content, filename):
    # Create a SimpleDocTemplate object to handle the PDF creation
    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Set up styles for the document
    styles = getSampleStyleSheet()

    # Define custom styles for headings
    heading_style = ParagraphStyle(
        'Heading1',
        parent=styles['Heading1'],
        fontSize=16,
        spaceAfter=12,
        textColor=colors.black,
        alignment=1,  # Centered
        fontName='Helvetica-Bold'
    )
    
    subheading_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=10,
        textColor=colors.black,
        alignment=0,  # Left aligned
        fontName='Helvetica-Bold'
    )
    
    subsubheading_style = ParagraphStyle(
        'Heading3',
        parent=styles['Heading3'],
        fontSize=12,
        spaceAfter=8,
        textColor=colors.black,
        alignment=0, # left aligned
        fontName='Helvetica-Bold'
    )
    
    # Define the normal text style for paragraphs
    normal_style = styles['Normal']
    
    # Split the content into lines and process it
    paragraphs = []
    
    # Split the content by lines and process for headings and subheadings
    for line in content.split("\n"):
        if line.startswith("# "):  # Main Heading
            paragraph = Paragraph(line[2:], heading_style)
        elif line.startswith("## "):  # Subheading
            paragraph = Paragraph(line[3:], subheading_style)
        elif line.startswith("### "):
            paragraph = Paragraph(line[len("### "):], subsubheading_style)
        else:  # Normal content
            paragraph = Paragraph(line, normal_style)
        
        paragraphs.append(paragraph)
    
    # Create the PDF document with the processed paragraphs
    doc.build(paragraphs)

# Example usage
# content = """
# # Opening and Closing Accounts

# At [Bank Name], we offer a wide range of accounts to meet the needs of our customers. This section outlines the procedures for opening and closing checking and savings accounts.

# ## 1.1 Opening a Checking Account

# A checking account provides a convenient way for customers to manage their day-to-day finances. To open a checking account with [Bank Name], please follow the steps below:

# ### 1.1.1 Eligibility Criteria

# - Must be at least 18 years old.
# - Must provide valid government-issued identification.
# - Proof of address for residents of the local area.
# """

# Call the function to create the PDF
# create_pdf(content, "C:/Users/Madhu/Downloads/small_example.pdf")
create_pdf(content, "C:/Users/Madhu/Downloads/Account_Opening_Closing_Guide.pdf")



