import playfab.PlayFabErrors as PlayFabErrors
import sys
import traceback

ProductionEnvironmentURL = "https://{titleId}.playfabapi.com{methodUrl}"
"""
You must set this value for PlayFabSdk to work properly (Found in the Game
Manager for your title, at the PlayFab Website)
"""

TitleId = ""

"""
You must set this value for Admin/Server/Matchmaker to work properly (Found in the Game
Manager for your title, at the PlayFab Website)
"""

DeveloperSecretKey = None

"""
Client specifics
"""

"""
Set this to the appropriate AD_TYPE_X constant below
"""
AdvertisingIdType = ""

"""
Set this to corresponding device value
"""
AdvertisingIdValue = None

"""
DisableAdvertising is provided for completeness, but changing it is not
suggested
Disabling this may prevent your advertising-related PlayFab marketplace
partners from working correctly
"""

DisableAdvertising = False
AD_TYPE_IDFA = "Idfa"
AD_TYPE_ANDROID_ID = "Adid"

class InternalSettings:
    pass

_internalSettings = InternalSettings()

"""
This is automatically populated by the PlayFabAuthenticationApi.GetEntityToken method.
"""
_internalSettings.EntityToken = None

"""
This is automatically populated by any PlayFabClientApi.Login method.
"""
_internalSettings.ClientSessionTicket = None
_internalSettings.SdkVersionString = "PythonSdk-0.0.180906"
_internalSettings.RequestGetParams = {
    "sdk": _internalSettings.SdkVersionString
}

def GetURL(methodUrl, getParams):
    if not TitleId:
        raise PlayFabErrors.PlayFabException("You must set PlayFabSettings.TitleId before making an API call")

    url = []
    url.append(ProductionEnvironmentURL.format(titleId = TitleId, methodUrl=methodUrl))

    if getParams:
        for idx, (k, v) in enumerate(getParams.items()):
            if idx == 0:
                url.append("?")
            else:
                url.append("&")
            url.append(k)
            url.append("=")
            url.append(v)

    return "".join(url)

def DefaultExceptionLogger(exceptionObj):
    print("Unexpected error:", sys.exc_info()[0])
    traceback.print_exc()

GlobalErrorHandler = None
GlobalExceptionLogger = DefaultExceptionLogger
