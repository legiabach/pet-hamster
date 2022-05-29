input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.showIcon(IconNames.Sad)
    soundExpression.giggle.playUntilDone()
    basic.showIcon(IconNames.Asleep)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showIcon(IconNames.Happy)
    soundExpression.mysterious.playUntilDone()
    basic.showIcon(IconNames.Asleep)
})
basic.showIcon(IconNames.Asleep)
