from rest_framework import status
from django.conf import settings
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from urllib.parse import urlparse, urlunparse


class CustomPagination(PageNumberPagination):
    """
    Кастомный пагинатор для оборачивания данных в data.
    """

    def get_paginated_response(self, data):
        next_link = self.get_next_link()
        previous_link = self.get_previous_link()
        return Response({
            'pagination': {
                'total': self.page.paginator.count,
                'rows': self.page_size,
                'next': next_link,
                'previous': previous_link,
            },
            'data': data,
            'message': self.message if hasattr(self, 'message') else None
        })

    def get_next_front_link(self, link):
        if link:
            parsed_url = urlparse(link)
            next_page_number = self.page.next_page_number()
            query_params = f'page={next_page_number}'.encode() \
                if parsed_url.query else f'?page={next_page_number}'.encode()
            path = parsed_url.path.replace('api/', '').encode()
            url = urlunparse(
                (parsed_url.scheme.encode(),
                 settings.FRONT_DOMAIN.encode(),
                 path, parsed_url.params.encode(),
                 query_params, parsed_url.fragment.encode())
            )
            return url.replace(b'http://', b'').decode()
        return None

    def get_previous_front_link(self, link):
        if link:
            parsed_url = urlparse(link)
            previous_page_number = self.page.previous_page_number()
            query_params = f'page={previous_page_number}'.encode() \
                if parsed_url.query else f'?page={previous_page_number}'.encode()
            path = parsed_url.path.replace('api/', '').encode()
            url = urlunparse(
                (parsed_url.scheme.encode(), settings.FRONT_DOMAIN.encode(),
                 path, parsed_url.params.encode(), query_params, parsed_url.fragment.encode())
            )
            return url.replace(b'http://', b'').decode()
        return None

    def get_response(self, serialized_data):
        if self.page.paginator.count > 0:
            return self.get_paginated_response(serialized_data)
        else:
            response_data = {"pagination": None, "data": None, "message": "Объектов нет."}
        return Response(response_data, status=status.HTTP_200_OK)

    def get_paginated_response_schema(self, schema):
        return {
            'type': 'object',
            'properties': {
                'pagination': {
                    'type': 'object',
                    'nullable': True,
                    'properties': {
                        'total': {
                            'type': 'integer',
                            'example': 3,
                        },
                        'rows': {
                            'type': 'integer',
                            'example': 2,
                        },
                        'next': {
                            'type': 'string',
                            'nullable': True,
                            'format': 'uri',
                            'example': 'http://api.example.org/accounts/?{page_query_param}=4'.format(
                                page_query_param=self.page_query_param)
                        },
                        'previous': {
                            'type': 'string',
                            'nullable': True,
                            'format': 'uri',
                            'example': 'http://api.example.org/accounts/?{page_query_param}=2'.format(
                                page_query_param=self.page_query_param)
                        },

                    }
                },
                'data': schema,
                'message': {
                    'type': 'string',
                    'example': 'Сообщение об успешном запросе.',
                },
            },
        }
