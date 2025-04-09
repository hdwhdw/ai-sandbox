import time
from ..models.user import User

class AuthenticationService:
    """
    Service to handle user authentication.
    """
    
    def __init__(self, session_timeout=3600):
        """
        Initialize authentication service.
        
        Args:
            session_timeout (int): Time in seconds before a session expires (default: 1 hour)
        """
        self.active_sessions = {}  # user_id -> last_activity_timestamp
        self.session_timeout = session_timeout
    
    def authenticate(self, user, password):
        """
        Authenticate a user with password.
        
        Args:
            user (User): User object to authenticate
            password (str): Password to verify
            
        Returns:
            bool: True if authentication successful, False otherwise
        """
        # In a real system, we would verify the password here
        # For this demo, we'll assume password verification is successful
        
        # Check if user is active
        if not user.is_active:
            return False
        
        # Record session activity
        self.active_sessions[user.user_id] = time.time()
        return True
    
    def is_authenticated(self, user_id):
        """
        Check if a user is currently authenticated.
        
        Args:
            user_id (str): ID of the user to check
            
        Returns:
            bool: True if user is authenticated, False otherwise
        """
        if user_id not in self.active_sessions:
            return False
            
        # Check if session has timed out
        last_activity = self.active_sessions[user_id]
        current_time = time.time()
        
        if current_time - last_activity > self.session_timeout:
            # Session expired, remove it
            del self.active_sessions[user_id]
            return False
            
        # Update last activity time
        self.active_sessions[user_id] = current_time
        return True
    
    def logout(self, user_id):
        """
        Log out a user.
        
        Args:
            user_id (str): ID of the user to log out
        """
        if user_id in self.active_sessions:
            del self.active_sessions[user_id]
    
    def update_session_timeout(self, timeout):
        """
        Update the session timeout value.
        
        Args:
            timeout (int): New timeout value in seconds
        """
        self.session_timeout = timeout
