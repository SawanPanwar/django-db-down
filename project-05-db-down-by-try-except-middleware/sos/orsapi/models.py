from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def to_json(self):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
        return data

    class Meta:
        db_table = 'sos_role'
