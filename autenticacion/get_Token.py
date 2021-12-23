import requests
from firebase_admin import auth

__FIREBASE_USER_VERIFY_SERVICE = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword"
__FIREBASE_API_KEY = "AIzaSyB5cvfwNdX_HP4pJODxxlNv4JRuIIWJp_s"


def user_login(email, passwd):
    url = "%s?key=%s" % (__FIREBASE_USER_VERIFY_SERVICE, __FIREBASE_API_KEY)
    data = {"email": email,
            "password": passwd,
            "returnSecureToken": True}
    result = requests.post(url, json=data)
    is_login_successful = result.ok
    json_result = result.json()
    return json_result    # authToken=> json_result['idToken']


def get_token(email, password):
    try:
        id_token = user_login(email, password)
        return id_token['idToken']

    except:
        raise ('usuario invalido o password invalido, tratemos de nuevo')


