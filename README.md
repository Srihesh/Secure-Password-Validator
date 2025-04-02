#Secure Password Validator

This Python script checks if your passwords have been compromised in data breaches using the Have I Been Pwned (HIBP) API.

## How It Works

1. **Secure Hashing**: Uses SHA-1 hashing algorithm to convert passwords into hashes before sending to the API
2. **k-Anonymity Protection**: Only sends the first 5 characters of the hash to maintain privacy
3. **API Integration**: Connects with HIBP's range search API to check for compromised passwords
4. **Result Analysis**: Compares the remaining hash characters with API response to find matches

## Features

- Command-line interface for easy use
- Secure implementation that never sends full passwords
- Clear output showing whether passwords were found in breaches
- Multiple password checking in a single run

## Usage

Run the script from command line with passwords as arguments:
```
python password_checker.py passkey1 passkey2 passkey3
```

## Security Notes

- Full passwords never leave your local machine
- The script uses the k-anonymity model to protect your passwords
- Only the first 5 characters of the hash are transmitted

## Dependencies

- Python 3.x
- `requests` library (install with `pip install requests`)
