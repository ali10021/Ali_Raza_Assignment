from rest_framework.permissions import BasePermission

class CustomPermission(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return obj == request.user
    
class CustomPermissionForSalesData(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
    
    
    

