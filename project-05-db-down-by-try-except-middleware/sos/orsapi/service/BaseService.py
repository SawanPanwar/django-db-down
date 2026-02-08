from abc import ABC, abstractmethod
from ..exception.application_exception import ApplicationException


class BaseService(ABC):

    def __init__(self):
        self.pageSize = 5

    def save(self, obj):
        try:
            if (obj.id == 0):
                obj.id = None
            obj.save()
        except Exception as e:
            raise ApplicationException("Unexpected error occurred while saving object")

    def delete(self, obj_id):
        try:
            obj = self.get(obj_id)
            obj.delete()
        except Exception as e:
            raise ApplicationException("Unexpected error occurred while delete object")


    def get(self, obj_id):
        try:
            obj = self.get_model().objects.get(id=obj_id)
            return obj
        except self.get_model().DoesNotExist:
            return None
        except Exception as e:
            raise ApplicationException("Unexpected error occurred while getting object")

    def search(self):
        try:
            objs = self.get_model().objects.all()
            return objs
        except self.get_model().DoesNotExist:
            return None
        except Exception as e:
            raise ApplicationException("Unexpected error occurred while delete object")

    def preload(self):
        try:
            objs = self.get_model().objects.all()
            return objs
        except self.get_model().DoesNotExist:
            return None
        except Exception as e:
            raise ApplicationException("Unexpected error occurred while delete object")

    @abstractmethod
    def get_model(self):
        pass
