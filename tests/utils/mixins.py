class RequestHelperMixin:
    def authenticate(self):
        """Helper method to force user authentication"""
        self.client.force_authentication(user=self.user)
    
    def send_request(self, method, url, data=None, authenticate=False):
        """
        Helper method to send a request with optional authentication

        :param method: HTTP method as as string ('get', 'post', 'put', 'patch')
        :param url: URL to send the request to.
        :param data: (optional) Data to be sent with the request.
        :param authenticate: If True, authenticates the client before making the request.
        :return: Response object.
        
        """

        if authenticate:
            self.authenticate()

        methods = {
            'get': self.client.get(url),
            'post': self.client.post(url, data=data),
            'put': self.client.put(url, data=data),
            'patch': self.client.put(url, data=data),
            'delete': self.client.delete(url),
        }

        method = method.lower()

        try:
            return methods[method]
        except KeyError:
            raise ValueError("Unsupported HTTP method provided.") 
