import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

MY_ADDRESS = 'your email address'
PASSWORD = 'your password email address'

def get_contacts(filename):
    """
    get names and emails address from contact email from file
    """
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    get template or other will you read on body email from file
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main(): #the main function will execute first
    names, emails = get_contacts('your file on .txt format') # read contacts
    message_template = read_template('your file on .txt format') # read templat or text

    # set up the SMTP server
    s = smtplib.SMTP(host='your smtp host', port=port you use) #host like 'gmail or other'
    s.starttls() #user tls mode
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # Prints out the emails address for our sake
        print(email)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="subject"
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        #add attachment what you want to sender
        attach_file = "your file" #get file
        attachment = open("path of your file", "rb") #open file with rb
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('content-Disposition', "attachment; filename= %s" % attach_file) #header for name of file
        msg.attach(p)

        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
        
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()
