import tempfile
import os

AUTH_DELIMITER = '__________'

import base64


def to_base64(input_string):
    encoded_bytes = base64.b64encode(input_string.encode('utf-8'))
    return encoded_bytes.decode('utf-8')


def from_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    return decoded_bytes.decode('utf-8')


def getEnvParam(env_var_name, default_value):
    env_value = os.environ.get(env_var_name)
    if env_value is not None: return env_value;
    return default_value


def getApiId(auth_str):
    return from_base64(auth_str).split(AUTH_DELIMITER)[0]


def getApiHash(auth_str):
    return from_base64(auth_str).split(AUTH_DELIMITER)[1]


def getSessionString(auth_str):
    return from_base64(auth_str).split(AUTH_DELIMITER)[2]


def saveBase64ToBinaryFile(base64_data, extension):
    _, tmp_file_path = tempfile.mkstemp(suffix='.' + extension)
    with open(tmp_file_path, 'wb') as tmp_file:
        tmp_file.write(base64.b64decode(base64_data))
    return tmp_file_path
