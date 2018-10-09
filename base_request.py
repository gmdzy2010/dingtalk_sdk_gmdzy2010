import requests


class BaseRequest(object):
    """The base request for dingtalk"""
    request_url = None
    request_methods_valid = [
        "get", "post", "put", "delete", "head", "options", "patch"
    ]
    
    def __init__(self):
        self.logger = None
        self._request_method = "get"
    
    @property
    def request_method(self):
        """Mostly, the get method is used to request wanted json data, as a
        result, the property of request_method is set to get by default."""
        return self._request_method
    
    @request_method.setter
    def request_method(self, method_str):
        request_method_lower = method_str.lower()
        if request_method_lower in self.request_methods_valid:
            self._request_method = request_method_lower
        else:
            raise ValueError(
                "%s is not a valid HTTP request method, please choose one"
                "of %s to perform a normal http request, correct it now."
                "" % (method_str, ",".join(self.request_methods_valid))
            )
    
    def get_response(self, **kwargs):
        """Get the original response of requests"""
        request = getattr(requests, self.request_method, None)
        if request is None and self._request_method is None:
            raise ValueError("A effective http request method must be set")
        if self.request_url is None:
            raise ValueError(
                "Fatal error occurred, the class property \"request_url\" is"
                "set to None, reset it with an effective url of dingtalk api."
            )
        response = request(self.request_url, **kwargs)
        return response
    
    def get_json_response(self, **kwargs):
        """This method is to catch the exception of ValueError, detail:
        http://docs.python-requests.org/zh_CN/latest/user/quickstart.html#json
        """
        response = self.get_response(**kwargs)
        return response.json()

