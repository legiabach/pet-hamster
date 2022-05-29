def on_gesture_shake():
    basic.show_icon(IconNames.SAD)
    soundExpression.giggle.play_until_done()
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    basic.show_icon(IconNames.HAPPY)
    soundExpression.mysterious.play_until_done()
    basic.show_icon(IconNames.ASLEEP)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

basic.show_icon(IconNames.ASLEEP)