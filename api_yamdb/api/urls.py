from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoriesViewSet,
    CommentViewSet,
    GenresViewSet,
    ReviewViewSet,
    TitlesViewSet,
)

app_name = 'api'

router = DefaultRouter()
router.register('titles', TitlesViewSet)
router.register('genres', GenresViewSet, basename='genres')
router.register('categories', CategoriesViewSet, basename='categories')
router.register(
    r'titles/(?P<title_id>[\d]+)/reviews',
    ReviewViewSet,
    basename='reviews'
)

router.register(
    r'titles/(?P<title_id>[\d]+)/reviews/(?P<review_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments',
)
urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('users.urls')),
]
