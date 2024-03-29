import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def replace_placeholders(text, placeholders):
    for placeholder, value in placeholders.items():
        text = text.replace("[" + placeholder + "]", value)
    return text


def send_email(subject, message, sender_email, receiver_emails, attachment_path):
    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Change this to your SMTP server and port
    server.starttls()
    server.login(sender_email, ' ')  # you get it from google, refer to the readme

    # Iterate through each receiver email
    for receiver in receiver_emails:
        receiver_name = receiver['name']
        receiver_email = receiver['email']

        # Create message container
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach message
        msg.attach(MIMEText(message, 'plain'))

        # Attach PDF file
        with open(attachment_path, "rb") as f:
            part = MIMEApplication(f.read(), Name="MyResume.pdf")
        part['Content-Disposition'] = f'attachment; filename="{attachment_path}"'
        msg.attach(part)

        # Send email
        server.send_message(msg)

    # Quit SMTP server
    server.quit()

job_title = "" # Write the role here
company_name = "" # Compnay name
job_id = "" # Job ID 
job_url = "" # Job URL
subject = "sub: MS DS student at CU Boulder interested in "+job_title+" at "+company_name # Change according to you!
pdf_path = "C:/Users/OneDrive/Documentos/resume/MyResume.pdf" # Example path

text_path = ""

if(job_id == ""):
    text_path = "C:/Users/OneDrive/Documentos/resume/DS_without_id.txt" # Example path
else:
    text_path = "C:/Users/OneDrive/Documentos/resume/DS_with_id.txt" # Example path

# Read content from text file
with open(text_path, 'r') as file:
    content = file.read()

# Define placeholders and their corresponding values
placeholders = {
    "Job Title": job_title,
    "Company Name": company_name,
    "Job URL": job_url,
    "Job ID": job_id
}

# Replace placeholders in the content
content = replace_placeholders(content, placeholders)

sender_email = "anudeep.nayak123@gmail.com"

# List of receiver emails with name and email
receiver_emails = [
    {"name": "their name", "email": "example@gmail.com"},
    {"name": "their name2", "email": "example2@gmail.com"}
] 

# Replace placeholders in the content for each recipient
for receiver in receiver_emails:
    placeholders["Name"] = receiver["name"]
    modified_content = replace_placeholders(content, placeholders)
    
    # Call send_email function with modified content for each recipient
    send_email(subject, modified_content, sender_email, [receiver], pdf_path)
