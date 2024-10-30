from aima3.utils import expr
from rest_framework.decorators import api_view
from rest_framework.response import Response

from diagnosis_project.diagnosis_project.IE import diagnose
from diagnosis_project.diagnosis_project.KnowledgeBase import build_knowledge_base


