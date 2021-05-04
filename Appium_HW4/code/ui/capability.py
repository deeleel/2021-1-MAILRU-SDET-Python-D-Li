import os

def capability_select(device_os):
    if device_os == 'android':
        capability = {"platformName": "Android",
                      "platformVersion": "8.1",
                      "automationName": "Appium",
                      "appPackage": "ru.mail.search.electroscope",
                      "appActivity": "ru.mail.search.electroscope.ui.activity.AssistantActivity",
                      "autoGrantPermissions": True,
                      "app": os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                          '../stuff/Marussia_v1.39.1.apk')
                                             ),
                      "orientation": "PORTRAIT"
                      }
    else:
        raise ValueError("Incorrect device os type")
    return capability
