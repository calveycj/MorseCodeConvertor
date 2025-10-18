from converter import text_to_morse

convert_message = True

while convert_message:
    user_input = input("Please enter the string you would like to convert to morse code: ")
    user_response = input(f"You entered: {user_input}, is that correct? (Y/N): ")
    if user_response.upper() == "Y":
        morse_code = text_to_morse(user_input)
        print(f"Morse code for {user_input} is: {morse_code}")
    elif user_response.upper() == "N":
        continue
    else:
        print("Terminating program...")
        convert_message = False
