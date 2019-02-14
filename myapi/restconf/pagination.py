from rest_framework import pagination

# class CustomPagination(pagination.PageNumberPagination):
#     page_size = 3


class CustomPagination(pagination.LimitOffsetPagination):
    default_limit = 10
    max_limit = 5
