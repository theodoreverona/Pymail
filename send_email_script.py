import smtplib
import ssl

# Setup port number and servr name

smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server

email_from = "[insert gmail address here]"
email_to = "[insert email address here"

pswd = "[insert key here from gmail account]"

# content of message

message = "Good morning, collect your invoice money"

# Create context
simple_email_context = ssl.create_default_context()


try:
    # Connect to the server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server :-)")
    
    # Send the actual email
    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email successfully sent to - {email_to}")

# If there's an error, print it out
except Exception as e:
    print(e)

# Close the port
finally:
    TIE_server.quit()



    
    
    
    

