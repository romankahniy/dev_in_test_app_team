import subprocess


def get_udid():
    cmd = "adb devices"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=True, check=True)
    device = result.stdout.decode().strip().splitlines()[1]
    if device:
        return device.split()[0]
    else:
        raise Exception("No active devices")


def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': '9',
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': get_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity',
        'app': 'C:\\Users\\super\\OneDrive\\Робочий стіл\\dev_in_test_app_team\\app_binaries\\com.ajaxsystems_2022-08-19.apk'
    }
