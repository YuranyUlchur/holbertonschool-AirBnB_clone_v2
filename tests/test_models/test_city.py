#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State

class test_City(test_basemodel):
    """Test Case"""

    def __init__(self, *args, **kwargs):
        """attribute initialization"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_creation(self):
        """verification"""
        state = State(name="California")
        new = self.value(state_id=state.id, name="San_Francisco")
        self.assertEqual(type(new.state_id), str)
        self.assertEqual(type(new.name), str)
