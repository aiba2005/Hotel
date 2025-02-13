from rest_framework import permissions


class CheckOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'owner':
            return True
        if request.user.status == 'client':
            return False


class CheckClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'client':
            return True
        if request.user.status == 'owner':
            return False


# class CheckStatus(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.status == 'pro':
#             return True
#         if request.user.status == 'simple' and obj.status_movie == 'simple':
#             return  True
#
#         return False
