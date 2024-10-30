from aima3.utils import expr
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .IE import diagnose, get_treatment
from .KnowledgeBase import build_knowledge_base
from .agenda import Agenda


# Create your views here.

@api_view(['POST'])
def diagnose_user(request):
    symptoms = request.data.get('symptoms')
    user_symptoms = {}
    c = 0
    for symptom in symptoms:
        user_symptoms[f'symp{c}'] = (expr(f'{symptom}(John)'))
        c += 1

    # Define the agenda
    agenda = Agenda()
    agenda.assign_agenda(user_symptoms)

    # Temporary memory
    memory = {}
    kb = build_knowledge_base()
    agenda = diagnose(kb, agenda, memory, c, username=request.data.get('username'))

    return Response(agenda.agenda, status=status.HTTP_200_OK)


@api_view(['POST'])
def diagnose_treatment(request):
    disease = request.data.get('disease')
    username = request.data.get('username')

    # Define the agenda
    agenda = Agenda()
    agenda.add_to_agenda('disease', expr(f'{disease}({username})'))

    # Temporary memory
    memory = {}
    kb = build_knowledge_base()
    agenda = get_treatment(kb, agenda, memory, username=request.data.get('username'))

    return Response(agenda.agenda, status=status.HTTP_200_OK)
