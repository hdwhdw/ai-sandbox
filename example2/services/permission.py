class PermissionService:
    """
    Service to handle user permissions.
    """
    
    def __init__(self, auth_service):
        """
        Initialize the permission service.
        
        Args:
            auth_service: Authentication service to check if users are authenticated
        """
        self.auth_service = auth_service
        
    def can_access_resource(self, user, resource):
        """
        Check if a user has permission to access a resource.
        
        Args:
            user: User trying to access the resource
            resource: Resource being accessed
            
        Returns:
            bool: True if user can access the resource, False otherwise
        """
        # First check if user is authenticated
        if not self.auth_service.is_authenticated(user.user_id):
            return False
            
        # Check if user is active
        if not user.is_active:
            return False
            
        # For demo purposes, we'll implement a simple permission system:
        # - Admins can access everything
        # - Regular users can only access resources that don't start with "admin_"
        if user.is_admin():
            return True
            
        return not resource.startswith("admin_")
