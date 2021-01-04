dis = 0
dis2 = 0

def on_forever():
    global dis2
    if 50 > dis:
        dis2 = dis
        basic.pause(100)
        if dis2 > dis:
            basic.show_icon(IconNames.SMALL_HEART)
            kitronik_motor_driver.motor_off(kitronik_motor_driver.Motors.MOTOR1)
            kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
                kitronik_motor_driver.MotorDirection.REVERSE,
                50)
    else:
        basic.show_icon(IconNames.HEART)
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR1,
            kitronik_motor_driver.MotorDirection.REVERSE,
            50)
        kitronik_motor_driver.motor_on(kitronik_motor_driver.Motors.MOTOR2,
            kitronik_motor_driver.MotorDirection.FORWARD,
            40)
basic.forever(on_forever)

def on_forever2():
    global dis
    pins.digital_write_pin(DigitalPin.P2, 0)
    control.wait_micros(2)
    pins.digital_write_pin(DigitalPin.P2, 1)
    control.wait_micros(10)
    pins.digital_write_pin(DigitalPin.P2, 0)
    dis = pins.pulse_in(DigitalPin.P1, PulseValue.HIGH) / 36
basic.forever(on_forever2)
