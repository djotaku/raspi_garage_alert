import RPi.GPIO as GPIO

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("Printing a 1 if garage is closed and a 0 if open") 
    while True:
        print(GPIO.input(16))



if __name__ == "__main__":
    main()
