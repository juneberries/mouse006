def on_button_pressed_a():
    global on
    on = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global on
    kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
    kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR2)
    on = 1
input.on_button_pressed(Button.B, on_button_pressed_b)

dis = 0
on = 0
kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR2)
on = 1
trnds = 50

def on_forever():
    global dis
    pins.digital_write_pin(DigitalPin.P2, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P2, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P2, 0)
    dis = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) / 36
basic.forever(on_forever)

def on_forever2():
    if on == 0:
        if trnds >= dis:
            basic.pause(20)
            if trnds / 5 >= dis:
                kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
                    kitronik_motor_driver.MotorDirection.FORWARD,
                    50)
                kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                    kitronik_motor_driver.MotorDirection.REVERSE,
                    40)
                basic.pause(500)
                kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
                    kitronik_motor_driver.MotorDirection.FORWARD,
                    100)
                kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                    kitronik_motor_driver.MotorDirection.FORWARD,
                    100)
                basic.pause(500)
            elif trnds > dis:
                kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
                    kitronik_motor_driver.MotorDirection.FORWARD,
                    100)
                kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                    kitronik_motor_driver.MotorDirection.FORWARD,
                    100)
        else:
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
                kitronik_motor_driver.MotorDirection.REVERSE,
                50)
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                kitronik_motor_driver.MotorDirection.FORWARD,
                40)
basic.forever(on_forever2)
