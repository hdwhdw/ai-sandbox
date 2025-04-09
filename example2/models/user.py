class User:
    """
    Represents a user in the system.
    """
    
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
        self.is_active = True
    
    def deactivate(self):
        """Deactivate the user account."""
        self.is_active = False
    
    def activate(self):
        """Activate the user account."""
        self.is_active = True
    
    def is_admin(self):
        """Check if the user is an admin."""
        return self.role == "admin"
