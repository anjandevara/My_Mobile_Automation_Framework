
# COMMAND TO GET ANDROID DEVICE NAME
get_device_name = "adb shell getprop ro.product.name"

# COMMAND TO GET ANDROID PLATFORM NAME
get_platform_name = "adb shell getprop net.bt.name"

# COMMAND TO GET ANDROID ANDROID DEVICE VERSION
get_device_version = "adb shell getprop ro.build.version.release"

# COMMAND TO SWIPE FROM LEFT TO RIGHT
swipe_little_from_bottom_to_top = "adb shell input swipe 520 1750 520 1300"
swipe_from_left_to_right = "adb shell input swipe 0 1000 2000 1000"
hide_keyboard = "adb shell input keyevent KEYCODE_BACK"
text_enter = "adb shell input text "
# COMMAND TO GET IOS DEVICE UDID
get_udid = "idevice_id -l"