# Symptom Tracker Automation for UMBC Symptom Tracker
*NOTE: This is a script for people who are healthy and have not come into contact, exposed, or contracted COVID-19 within the past 14 days. If you find yourself coming down with symptoms, please fill out the form as intended with an accurate description of your symptoms.*

---

### This is a small script that auto-fills the symptoms in the UMBC Symptom Tracker
You must create a profile by using the `configurator.py` program. Which will locally create a profile in the `config.json` file.  

### Requirements (pip)
- Pickle
- Selenium

### Inputs/Outputs
There is no input besides the need to give your @umbc.edu address, password, and personal phone number. All of this information is stored locally.

### Using tool with Two-Factor Authentication (2FA)  
This tool can be used with 2FA. There is a `10` second window from when you get logged in and should recieve a push notification from *DUO*. Failure to accept the push notification will result in the program suspending, thus not being able to complete the form.

### Roadmap:   
- Webop.py
  - Using *Flask* in order to create a GUI in order to create a profile and run the tracker
