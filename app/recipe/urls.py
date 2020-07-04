from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipes', views.RecipeViewSet)

""" So that the reverse function can see the appropiate app"""
app_name = 'recipe'

urlpatterns = [
	path('', include(router.urls))
]