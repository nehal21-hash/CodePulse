from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('CodeforcesRating',views.CodeforcesPrediction,name='CodeforcesRatingPredictions'),
    path('recommendation-topic',views.recommendTopic,name='recommendation-topic'),
    path('analyze',views.analyze,name='analyzer')

]
