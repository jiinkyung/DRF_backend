from django.urls import path
from .views import CommentAPIView, VeganAPIView, VeganDetailAPIView, CommentDetailAPIView

urlpatterns = [
    path('vegan/', VeganAPIView.as_view()),
    path('vegan/<int:pk>/', VeganDetailAPIView.as_view()),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:post_id>/', CommentDetailAPIView.as_view()),

]