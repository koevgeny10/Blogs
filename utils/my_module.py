def get_login_url(self):
    if self.request.user.is_authenticated:
        self.login_url = '/'
        self.redirect_field_name = None
    return super().get_login_url()
