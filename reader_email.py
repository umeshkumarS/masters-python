import imaplib
import email
import os

class email_access():

    def __init__(self):
        self.ORG_EMAIL   = "@gmail.com"
        self.FROM_EMAIL  = "sumanharish85"  + self.ORG_EMAIL
        self.FROM_PWD    = "operagini@241"
        self.SMTP_SERVER = "imap.gmail.com"
        self.SMTP_PORT   = 587
        #self.search_text = '(SUBJECT "II MASTERS PU COLLEGE" UNSEEN)'
        self.search_text = '(OR (SUBJECT "II MASTERS PU COLLEGE" UNSEEN) (SUBJECT "II MASTERS PU COLLEGE KEY" UNSEEN))'
    def read_email_from_gmail(self):
  
        id_list = []
        if 1:
            mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
            mail.login(self.FROM_EMAIL, self.FROM_PWD)
            mail.select('inbox')



            type, data = mail.search(None, self.search_text)
            mail_ids = data[0]
            id_list = mail_ids.split()
            id_list.reverse()
            for i in id_list:

                resp, data = mail.fetch(i, '(RFC822)')
                text = data[0][1].decode('utf-8')
                msg = email.message_from_string(text)
                print (msg['from'])
                subject  = msg['subject']
                print (subject)
                att_path, filename  = self.save_attachment(msg)

    def save_attachment(self, msg, download_folder="static/data"):

        att_path = "No attachment found."
        filename = ''
        for part in msg.walk():
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue
            filename = part.get_filename()
            if not filename:continue
#            if 'ARMVMStatus' in filename:
#                filename = 'ARMVMStatus.csv'
#            if 'VM_Inventory' in filename:
#                filename    = 'VM_Inventory.xlsx' #if base is sent in mail
                #download_folder = 'Data'
            att_path = os.path.join(download_folder, filename)
            if 1 :
                fp = open(att_path, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
        #self.df_to_db()
        return att_path, filename
if __name__ == "__main__":
       obj  = email_access()
       obj.read_email_from_gmail()
