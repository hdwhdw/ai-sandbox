import unittest
from ..models.user import User
from ..services.authentication import AuthenticationService

class TestAuthentication(unittest.TestCase):
    
    def setUp(self):
        self.auth_service = AuthenticationService()
        self.user = User("user1", "testuser", "test@example.com")
        
    def test_authentication_active_user(self):
        """Test that an active user can authenticate."""
        self.user.is_active = True
        result = self.auth_service.authenticate(self.user, "password123")
        self.assertTrue(result)
        self.assertTrue(self.auth_service.is_authenticated(self.user.user_id))
        
    def test_authentication_inactive_user(self):
        """Test that an inactive user cannot authenticate."""
        self.user.is_active = False
        result = self.auth_service.authenticate(self.user, "password123")
        self.assertFalse(result)
        self.assertFalse(self.auth_service.is_authenticated(self.user.user_id))
        
    def test_logout(self):
        """Test that a user can be logged out."""
        self.auth_service.authenticate(self.user, "password123")
        self.auth_service.logout(self.user.user_id)
        self.assertFalse(self.auth_service.is_authenticated(self.user.user_id))


if __name__ == "__main__":
    unittest.main()
