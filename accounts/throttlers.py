from rest_framework.throttling import SimpleRateThrottle


class RegisterThrottle(SimpleRateThrottle):
    scope = "register"

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class ProfileThrottle(SimpleRateThrottle):
    scope = "profile"

    def get_cache_key(self, request, view):
        email = request.user.email
        indent = self.get_ident(request)
        return f"profile:{email}:{indent}"
