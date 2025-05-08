# Python Keylogger with Email, Screenshot, and Audio Recording

This Python-based keylogger is a personal cybersecurity project designed to log keystrokes, capture screenshots, and record audio, subsequently sending these files to a specified email address. It utilizes several Python libraries to achieve this functionality.

## Disclaimer

**This project is intended for educational and personal security testing purposes ONLY.** Using this tool without explicit permission on systems you do not own or have the right to access is illegal and unethical. The developer assumes no responsibility for any misuse of this software.

## Features

* **Keylogging:** Records all keystrokes made on the system.
* **Screenshot Capture:** Periodically takes screenshots of the active screen.
* **Audio Recording:** Records audio from the default microphone for a set duration (currently 30 seconds).
* **Email Reporting:** Sends the logged keystrokes, screenshots, and audio recordings as attachments to a pre-configured email address.
* **Library Usage:** Leverages the following Python libraries:
    * `email`: For creating and handling email messages.
    * `smtplib`: For sending emails using the Simple Mail Transfer Protocol.
    * `sounddevice`: For recording audio from the microphone.
    * `getpass`: For securely obtaining user input (though likely not directly used for keylogging itself, it might be used for configuration).
    * `PIL.ImageGrab` (or `mss`): For capturing screenshots.
    * `pynput.keyboard`: For capturing keyboard input.

## Setup and Usage

**Warning:** Exercise extreme caution when running this script. Ensure you understand its functionality and only use it on systems you have explicit permission to test.

1.  **Prerequisites:**
    * Python 3.x installed on your system.
    * The required libraries installed. You can install them using pip:
        ```bash
        pip install pynput pillow sounddevice
        ```
        You might need to install platform-specific dependencies for `sounddevice`. Refer to the `sounddevice` documentation for details.

2.  **Configuration:**
    * Open the Python script (`your_keylogger_script_name.py`).
    * Locate the section where the email sending parameters are defined.
    * **Modify the following variables:**
        * `sender_email`: Your email address.
        * `sender_password`: Your email password (consider using an App Password for security if your email provider supports it).
        * `receiver_email`: The email address where the logs will be sent.
    * Adjust the `screenshot_interval` and `audio_duration` (currently 30 seconds) if desired.
    * **Important Security Note:** Hardcoding your email credentials directly in the script is not recommended for long-term use or distribution. Consider more secure methods for handling sensitive information.

3.  **Running the Keylogger:**
    * Execute the Python script:
        ```bash
        python keylogger.py
        ```
    * The keylogger will run in the background, logging keystrokes, taking screenshots, and recording audio according to the configured intervals.
    * The collected data will be saved locally and then sent to the specified email address.

## Important Considerations

* **Antivirus Detection:** This type of tool may be flagged as malicious by antivirus software. You might need to configure exceptions or disable your antivirus temporarily for testing (at your own risk).
* **Ethical Use:** As emphasized earlier, use this tool responsibly and ethically. Unauthorized use is illegal and harmful.
* **Security Risks:** Be extremely careful about where you run this script and who has access to the collected data in your email.
* **Email Configuration:** Ensure your email provider's SMTP settings are correctly configured in the script. You might need to enable "less secure app access" or generate an App Password depending on your provider's security policies.
* **Error Handling:** The provided script might not include extensive error handling. You might want to add error handling for network issues, file saving problems, etc.
* **Persistence:** This script, as described, will likely stop running when the terminal window is closed. For persistent operation, you would need to implement methods for running it in the background (e.g., as a service or using tools like `nohup` or `screen` on Linux). This is beyond the scope of this basic README.

## Disclaimer of Liability

This software is provided "as is" without any warranty, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the author or contributors be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
