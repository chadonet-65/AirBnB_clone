import uuid
from datetime import datetime


class BaseModel:
    """
    Base Model class that defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor to initialize instance variables
        """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at = datetime.now()
                    self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the public attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """
        new_dict = self.__dict__.copy()  # copy of the instance's __dict__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict