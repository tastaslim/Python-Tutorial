class Authenticator:
    def __init__(self, client_name):
        self.client_name = client_name

    def access_token(self, **kwargs):
        try:
            return self.client_name.access_token(**kwargs)
        except NotImplementedError as e:
            print("Error authenticating:", e)
            raise e
        except Exception as e:
            print("Error authenticating:", e)
            raise e

    def refresh_token(self, **kwargs):
        try:
            return self.client_name.refresh_token(**kwargs)
        except NotImplementedError as e:
            print("Error authenticating:", e)
            raise e
        except Exception as e:
            print("Error authenticating:", e)
            raise e
