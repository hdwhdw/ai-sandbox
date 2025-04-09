class User:
    """
    Represents a user in the system.
    """
    
    # Define user status constants
    STATUS_ACTIVE = "active"
    STATUS_INACTIVE = "inactive"
    STATUS_PENDING = "pending"
    STATUS_SUSPENDED = "suspended"
    
    def __init__(self, user_id, username, email, role="user"):
        """
        Initialize a new user.
        
        Args:
            user_id (str): Unique identifier for the user
            username (str): Username for the user
            email (str): Email address of the user
            role (str): Role of the user (default: "user")
        """
        self.user_id = user_id
        self.username = username
        self.email = email
        self.role = role
        self.status = self.STATUS_ACTIVE
        self.is_active = True  # Keep for backward compatibility
    
    def deactivate(self):
        """Deactivate the user account."""
        self.status = self.STATUS_INACTIVE
        self.is_active = False
    
    def activate(self):
        """Activate the user account."""
        self.status = self.STATUS_ACTIVE
        self.is_active = True
        
    def suspend(self):
        """Suspend the user account."""
        self.status = self.STATUS_SUSPENDED
        self.is_active = False  # Suspended users are not active
    
    def set_pending(self):
        """Set user account to pending verification."""
        self.status = self.STATUS_PENDING
        self.is_active = False  # Pending users are not active
    
    def is_admin(self):
        """Check if the user is an admin."""
        return self.role == "admin"
