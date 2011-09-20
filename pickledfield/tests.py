import datetime

from django.db import models
from django.test import TestCase

from fields import JSONField

class JsonModel(models.Model):
    json = JSONField()


class JSONFieldTest(TestCase):
    """JSONField Wrapper Tests"""

    def test_json_field_create(self):
        """Test saving a JSON object in our JSONField"""

        json_obj = {
            "item_1": "this is a json blah",
            "blergh": "hey, hey, hey"}

        obj = JsonModel.objects.create(json=json_obj)
        new_obj = JsonModel.objects.get(id=obj.id) 

        self.failUnlessEqual(new_obj.json, json_obj)


    def _test_json_field_modify(self):
        """Test modifying a JSON object in our JSONField"""

        json_obj_1 = {'a': 1, 'b': 2}
        json_obj_2 = {'a': 3, 'b': 4}

        obj = JsonModel.objects.create(json=json_obj_1)

        self.failUnlessEqual(obj.json, json_obj_1)

        obj.json = json_obj_2

        self.failUnlessEqual(obj.json, json_obj_2)

        obj.save()

        self.failUnlessEqual(obj.json, json_obj_2)

        self.assert_(obj)

    def _test_json_field_load(self):
        """Test loading a JSON object from the DB"""

        json_obj_1 = {'a': 1, 'b': 2}

        obj = JsonModel.objects.create(json=json_obj_1)

        new_obj = JsonModel.objects.get(id=obj.id)

        self.failUnlessEqual(new_obj.json, json_obj_1)

    def _test_json_list(self):
        """Test storing a JSON list"""

        json_obj = ["my", "list", "of", 1, "objs", {"hello": "there"}]

        obj = JsonModel.objects.create(json=json_obj)
        new_obj = JsonModel.objects.get(id=obj.id)
        self.failUnlessEqual(new_obj.json, json_obj)
