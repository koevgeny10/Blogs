def getLoginUrl(self):
    if self.request.user.is_authenticated:
        self.login_url = '/'
        self.redirect_field_name = None
    return super(self.__class__, self).get_login_url()
