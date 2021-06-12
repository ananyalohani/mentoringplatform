from rest_framework import viewsets
from main.mixins import ViewSetPermissionByMethodMixin
import mentor.permissions as mentor_permissions
from rest_framework import permissions
from users import permissions as user_permissions
from mentor.models import Mentor, MentorResponsibility, MentorDepartment, MentorDesignation, MentorDiscipline
from mentor.serializers import MentorSerializer, MentorResponsibilitySerializer, MentorDepartmentSerializer, \
    MentorDesignationSerializer, MentorDisciplineSerializer


class MentorViewSet(ViewSetPermissionByMethodMixin, viewsets.ModelViewSet):
    permission_classes = (mentor_permissions.CanAccessMentor,)
    permission_action_classes = dict(
        list=(permissions.IsAuthenticated,),
        retrieve=(permissions.IsAuthenticated,),
        destroy=(user_permissions.IsAdmin,),
        create=(user_permissions.IsAdmin,)
    )
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    lookup_field = 'uid'


class MentorResponsibilityViewSet(ViewSetPermissionByMethodMixin, viewsets.ModelViewSet):
    permission_classes = (user_permissions.IsAdmin,)
    permission_action_classes = dict(
        list=(permissions.IsAuthenticated,),
        retrieve=(permissions.IsAuthenticated,)
    )
    queryset = MentorResponsibility.objects.all()
    serializer_class = MentorResponsibilitySerializer
    lookup_field = 'uid'


class MentorDepartmentViewSet(ViewSetPermissionByMethodMixin, viewsets.ModelViewSet):
    permission_classes = (user_permissions.IsAdmin,)
    permission_action_classes = dict(
        list=(permissions.IsAuthenticated,),
        retrieve=(permissions.IsAuthenticated,)
    )
    queryset = MentorDepartment.objects.all()
    serializer_class = MentorDepartmentSerializer
    lookup_field = 'uid'


class MentorDesignationViewSet(ViewSetPermissionByMethodMixin, viewsets.ModelViewSet):
    permission_classes = (user_permissions.IsAdmin,)
    permission_action_classes = dict(
        list=(permissions.IsAuthenticated,),
        retrieve=(permissions.IsAuthenticated,)
    )
    queryset = MentorDesignation.objects.all()
    serializer_class = MentorDesignationSerializer
    lookup_field = 'uid'


class MentorDisciplineViewSet(ViewSetPermissionByMethodMixin, viewsets.ModelViewSet):
    permission_classes = (user_permissions.IsAdmin,)
    permission_action_classes = dict(
        list=(permissions.IsAuthenticated,),
        retrieve=(permissions.IsAuthenticated,)
    )
    queryset = MentorDiscipline.objects.all()
    serializer_class = MentorDisciplineSerializer
    lookup_field = 'uid'
