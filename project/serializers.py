from rest_framework import serializers

from .models import Project, Tool, Technology

class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        exclude = ['id']


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        exclude = ['id']


class ProjectSerializer(serializers.ModelSerializer):
    tools = ToolSerializer(many=True)
    technology = TechnologySerializer(many=True)
    class Meta:
        model = Project
        fields = ['name', 'description', 'technology', 'tools', 'hardware_used', 'price', 'video_demo_link', 'time_of_upload', 'quantity', 'pdf_available']
        depth = 1