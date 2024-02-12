# Password Leak Checker

### Overview

The Password Checker is a Python script designed to check if a given password has been compromised in data breaches. It utilizes [this](https://haveibeenpwned.com/Passwords) API to retrieve information about leaked passwords and provides users with a warning if their password has been compromised.
The project was developed as a part of the Python ZTM course, with some improvements, such as binary search etc.

### Usage

Install Python (if not already installed).
Clone or download the repository to your local machine.
Open a terminal or command prompt and cd to the directory containing the script.
Run the script using Python, providing the passwords you want to check as command-line arguments. Do not include any commas, as CLI will interpret them as part of provided passwords.

### Example:

```python passwordchecker.py password123 admin1234```

Output: 

```
password123 was found 293142 times, consider another password
7B902E6FF1DB9F560443F2048974FD7D386975B0
admin1234 was found 45863 times, consider another password
```

If your password contains a '*' symbol, don't forget escaping it:

```python passwordchecker.py password123 admin1234\*```

This will prevent the shell from interpreting the * character as a wildcard. 
