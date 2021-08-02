

# --------------- App imports -------------------
from App.models          import Question
from App.api.serializers import QuestionSerializer

# --------------- DRF imports -------------------
from rest_framework            import viewsets,permissions
from rest_framework.generics   import ListAPIView
from rest_framework.throttling import AnonRateThrottle


class IsAdminOrReadOnly(permissions.IsAdminUser):
    """Only Admin can post data others can only read it """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff



class QuestionVS(viewsets.ModelViewSet):
    """
        This will List All Questions and individual Questions
    """
    queryset             =   Question.objects.all()
    serializer_class     =   QuestionSerializer
    permission_classes   =   [IsAdminOrReadOnly]  
    throttle_classes     =   [AnonRateThrottle]  


class UserSelectedCategory(ListAPIView):
    """
        This will List All Questions Selected by User
    """
    serializer_class     =   QuestionSerializer
    throttle_classes     =   [AnonRateThrottle]  

    def get_queryset(self):
        selected_category = self.kwargs['type']
        return Question.objects.all().filter(category__category_name=selected_category)
        