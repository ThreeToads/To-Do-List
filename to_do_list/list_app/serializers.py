from rest_framework import serializers
from .models import Tasks


class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title',  'user', 'completed', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', ]


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'user']
        read_only_fields = ['id', 'created_at', 'updated_at', ]


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'completed', 'user', 'created_at', 'updated_at', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'title', 'completed', 'user', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]


class TaskDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', ]
        read_only_fields = ['id', 'created_at', 'updated_at', ]
