from rest_framework import viewsets,mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Recipe,Tag,Ingredient
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RescipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # This method overrides the default queryset to filter recipes so that only
    #  the recipes created by the authenticated user are returned.
    def get_queryset(self):
        return self.queryset.filter(user = self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        """return serializer class for request"""
        if self.action == 'list':
            return serializers.RecipeSerializer
        
        return self.serializer_class
    
    def perform_create(self, serializer):
        """create a new recipe"""
        serializer.save(user=self.request.user)


class BaseRecipeAttrViewSet(mixins.DestroyModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """filter queryset to authenticate user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
       

class TagViewSet(BaseRecipeAttrViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    
class IngredientViewSet(BaseRecipeAttrViewSet):
    serializer_class = serializers.IngredientSerializer
    queryset = Ingredient.objects.all()    