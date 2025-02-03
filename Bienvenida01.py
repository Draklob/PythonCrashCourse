personal_name = "Javier Barreiro"
nombre_personal = "Javier Barreiro"

print("Hello, my name is ", personal_name)
print(f"Hello {personal_name}, would you like to learn some python today?")

# Printing the name in lowercase, uppercase and title case
print(f"Lowercase: {personal_name.lower()}")
print(f"Uppercase: {personal_name.upper()}")
print(f"Title: {personal_name.title()}" )

famous_name = "Walt Disney"
famous_quote = "All or dreams can come true, if we have the courage to pursue them."
print(f"{famous_name} once said: {famous_quote}")

famous_name_strip = " Walt Disney "
print(f"{famous_name_strip} with spaces")
print(f"{famous_name_strip.lstrip()} no left space")
print(f"{famous_name_strip.rstrip()} no right space")
print(f"{famous_name_strip.strip()} no extra spaces")

google_url ="https//:www.google.es"
print(google_url.removeprefix("https//:"))

# numbers
print((2+2)*2)
print(4*2)
print(16/2)
print(10-2)

favourite_number = 23
print(f"Printing your favourite number {favourite_number}")