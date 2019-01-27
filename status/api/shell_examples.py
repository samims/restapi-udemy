"""
Just Notes
"""

from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from status.api.serializers import StatusSerializer
from status.models import Status

obj = Status.objects.first()
serializer = StatusSerializer(obj)
print(serializer.data)
json_data = JSONRenderer().render(serializer.data)
print(json_data)

stream = BytesIO(json_data)
data = JSONParser().parse(stream)
print(data)

"""
serialize a queryset
"""

qs = Status.objects.all()
serializer2 = StatusSerializer(qs, many=True)
serializer2.data
json_data2 = JSONRenderer().render(serializer2.data)
print(json_data2)

stream2 = BytesIO(json_data2)
data2 = JSONParser().parse(stream2)
print(data2)

# create obj

data = {"user": 1}

serializer = StatusSerializer(data=data)

serializer.is_valid()
serializer.save()

# if serializer.is_valid():
#     serializer.save()


'''
Update obj
'''
obj = Status.objects.first()
data = {'content': 'Some new content'}
update_serializer = StatusSerializer(object=obj, data=data)  # returns object
update_serializer.is_valid()
update_serializer.save()

'''
Delete obj
'''

obj = Status.objects.first()
data = {'user': 1, 'content': 'Please delete me'}
serializer = StatusSerializer(object=obj, data=data)
serializer.is_valid()
serializer.save()
