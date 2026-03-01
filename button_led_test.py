import RPi.GPIO as GPIO
import time

# Pins for buttons and LEDs
BUTTON_PINS = {
    "Red": 4,
    "Green": 6,
    "Blue": 5,
    "Yellow": 15
}

LED_PINS = {
    "Red": 14,
    "Green": 12,
    "Blue": 26,
    "Yellow": 20
}

# Setup

GPIO.setmode(GPIO.BCM)

# Set button pins as inputs with pull-up resistors
for name, pin in BUTTON_PINS.items():
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Set LED pins as outputs
for name, pin in LED_PINS.items():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

print("GPIO Button/LED Test Running...")
print("Press a button to light its matching LED. CTRL+C to exit.")


# Main loop
try:
    while True:
        for color in BUTTON_PINS:
            button_pin = BUTTON_PINS[color]
            led_pin = LED_PINS[color]
            if GPIO.input(button_pin) == GPIO.LOW:
                print(f"{color} button pressed")
                GPIO.output(led_pin, GPIO.HIGH)
            else:
                GPIO.output(led_pin, GPIO.LOW)

        # Small delay to debounce buttons
        time.sleep(0.05)

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()
