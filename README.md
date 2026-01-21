# educational-keylogger
A Python script demonstrating how keystrokes are captured for educational and defensive purposes.
# Educational Keylogger

## Objective
I built this tool to understand how malware persistence and data exfiltration work. By building a keylogger from scratch, I learned how easy it is to capture input and, more importantly, how to detect this behavior in a system (looking for unauthorized background Python processes).

## Tools Used
* **Python 3**
* **Pynput Library** (for controlling input devices)
* **Kali Linux**

## The Code
The script uses the `pynput` library to create a "Listener" that runs in the background. It intercepts every keystroke and appends it to a local file (`log.txt`).

## Disclaimer
This project is for **educational purposes only**. It was created in a virtual lab environment to learn about endpoint security and malware analysis.

## Evidence
![Keylogger Output](YOUR_SCREENSHOT_NAME.png)<img width="1635" height="664" alt="Screenshot 2026-01-21 105546" src="https://github.com/user-attachments/assets/4658aae1-bd38-4faf-b956-635788376896" />
<img width="1679" height="658" alt="Screenshot 2026-01-21 105422" src="https://github.com/user-attachments/assets/dd46e180-0ec0-4604-89bb-21f1043152b2" />
<img width="1299" height="906" alt="Screenshot 2026-01-21 105042" src="https://github.com/user-attachments/assets/15fc476e-0a8f-414f-b151-e6f3b6eaf4d2" />
