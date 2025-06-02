# download_button.py
import pyautogui
import time
import sys

def wait_for_button(image_path='downloadlinksaved_button.png', confidence_level=0.8):
    """Continuously wait for the button to appear until found."""
    print(f"Waiting for {image_path} to appear...")

    start_time = time.time()  # Record the start time
    timeout = 20  # Timeout after 20 seconds (you can adjust this)

    while True:  # Loop until timeout or button is found
        button_location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence_level, grayscale=True)
        if button_location:
            print(f"{image_path} found at {button_location}. Clicking...")
            pyautogui.click(button_location)
            sys.exit(0)  # Exit successfully once the button is found
        
        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            print(f"{image_path} not found within {timeout} seconds. Exiting with failure.")
            sys.exit(1)  # Exit with error code if button is not found

        time.sleep(0.5)  # Sleep briefly before checking again

if __name__ == "__main__":
    wait_for_button()
