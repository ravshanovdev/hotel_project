from rest_framework.permissions import BasePermission


class IsBusiness(BasePermission):

    message = "Only Business users can perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.user_type == "business"


class IsAdminOrBusiness(BasePermission):

    message = "Only Admin or Business users can perform this action."

    def has_permission(self, request, view):
        return request.user.is_authenticated and (request.user.is_staff or request.user.user_type == "business")



