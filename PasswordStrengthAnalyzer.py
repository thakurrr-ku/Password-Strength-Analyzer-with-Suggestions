import re

def check_password_strength(password):
    suggestions = []

    if len(password) < 8:
        suggestions.append("Password should be at least 8 characters long.")
    
    if not re.search(r'[a-z]', password):
        suggestions.append("Include at least one lowercase letter.")
    
    if not re.search(r'[A-Z]', password):
        suggestions.append("Include at least one uppercase letter.")
    
    if not re.search(r'[0-9]', password):
        suggestions.append("Include at least one digit.")
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        suggestions.append("Include at least one special character (e.g., !, @, #, $).")
    
    if any(pattern in password.lower() for pattern in ["password", "12345", "qwerty", "abc123"]):
        suggestions.append("Avoid using common patterns like 'password', '12345', etc.")

    if len(suggestions) == 0:
        print("Your password is strong!")
    else:
        for suggestion in suggestions:
            print(f"Suggestion: {suggestion}")

password = input("Enter your password: ")
check_password_strength(password)
