from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe
from recipe import serializers


class BaseRecipeAttrViewSet(
	viewsets.GenericViewSet,
	mixins.ListModelMixin,
	mixins.CreateModelMixin):
	"""Base viewset for user-owned recipe attributes Tags&Ingredients"""
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		"""Return objects for the current authenticated user only"""
		"""Filter the list by the current user"""
		return self.queryset.filter(user=self.request.user).order_by('-name')

	def perform_create(self, serializer):
		"""Create a new object (tag or ingredient)"""
		serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttrViewSet):
	"""Manage tags in the database"""
	"""Brings the list of tags"""
	queryset = Tag.objects.all()
	serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
	"""Manage ingredients in the database"""
	queryset = Ingredient.objects.all()
	serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
	"""Manage Recipes in the database"""
	queryset = Recipe.objects.all()
	serializer_class = serializers.RecipeSerializer
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get_queryset(self):
		"""Retrieve the recipes for the authenticated user"""
		return self.queryset.filter(user=self.request.user)