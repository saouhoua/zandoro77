import pyautogui
import random
import string
import time

# Path to the delete button image
delete_button_image = 'delete_button.png'

# Function to generate a random name with 6-8 characters
def generate_random_name():
    length = random.randint(6, 8)  # Random length between 6 and 8 characters
    letters = string.ascii_lowercase  # a..z
    random_name = ''.join(random.choice(letters) for i in range(length))
    return random_name

# Function to click at random positions from a list of given locations
def click_randomly(locations):
    # Choose a random location from the list
    x, y = random.choice(locations)
    pyautogui.click(x, y)

# Define the updated sets of locations to click
locations_1 = [
    (839, 550), (853, 551), (868, 551), (878, 552), (887, 552), 
    (856, 561), (864, 561), (874, 562), (883, 561)
]

locations_2 = [
    (320, 546), (340, 547), (352, 547), (366, 549), (379, 547), 
    (386, 545), (396, 550), (406, 551), (361, 553)
]

locations_3 = [
    (664, 361), (669, 361), (678, 362), (686, 361), (694, 364), 
    (701, 362), (710, 362), (724, 360), (734, 362)
]

locations_4 = [
    (856, 509), (864, 509), (874, 507), (881, 508), (896, 509), 
    (873, 515), (881, 514), (888, 515)
]

locations_5 = [
    (205, 179), (215, 174), (228, 174), (215, 189), (223, 188), 
    (208, 190), (217, 165), (224, 182)
]

# Function to perform the first task sequence when the delete button is found
def first_task_sequence():
    # Perform random clicks on defined locations
    click_randomly(locations_1)
    time.sleep(10)
    pyautogui.click(98, 83)
    time.sleep(5)
    click_randomly(locations_2)
    time.sleep(3)

    # Type a random name
    random_name = generate_random_name()
    pyautogui.write(random_name, interval=0.1)  # Simulate natural typing
    time.sleep(2)

    click_randomly(locations_3)
    time.sleep(2)

    click_randomly(locations_3)  # Repeat locations_3
    time.sleep(3)

    click_randomly(locations_4)
    time.sleep(8)
    pyautogui.click(98, 83)
    time.sleep(5)
    click_randomly(locations_5)
    time.sleep(3)

# Function to perform the alternate task sequence when the delete button is not found
def alternate_task_sequence():
    # Perform random clicks on defined locations
    click_randomly(locations_2)
    time.sleep(5)

    # Type a random name
    random_name = generate_random_name()
    pyautogui.write(random_name, interval=0.1)  # Simulate natural typing
    time.sleep(2)

    click_randomly(locations_3)
    time.sleep(2)

    click_randomly(locations_3)  # Repeat locations_3
    time.sleep(3)

    click_randomly(locations_4)
    time.sleep(8)
    pyautogui.click(98, 83)
    time.sleep(5)
    click_randomly(locations_5)
    time.sleep(3)

# Main function to detect the delete button and perform tasks accordingly
def main():
    # Search for the delete button on the screen (only once)
    try:
        delete_button = pyautogui.locateOnScreen(delete_button_image, confidence=0.8)

        if delete_button:
            print("Delete button found, executing first task sequence...")
            pyautogui.click(pyautogui.center(delete_button))  # Click the delete button
            time.sleep(9)
            first_task_sequence()
        else:
            print("Delete button not found, executing alternate task sequence...")
            alternate_task_sequence()

    except Exception as e:
        print(f"Error while detecting the delete button: {e}")
        # If there's an error (e.g., image not found), still execute the alternate task sequence
        alternate_task_sequence()

# Run the main function
main()
