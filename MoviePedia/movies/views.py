from django.shortcuts import render
from rest_framework import viewsets, generics
from db.models import Film, Rate, Comment, SubComment
from movies.serializers import FilmSerializer, CommentSerializer, RateSerializer
from movies.permissions import IsGetOrIsAuthenticated
from django.http import Http404
from rest_framework.permissions import AllowAny


# Create your views here.
class FilmView(viewsets.ModelViewSet):
    permission_classes = [IsGetOrIsAuthenticated]

    serializer_class = FilmSerializer
    def get_queryset(self):
        queryset = Film.objects.all()
        title_from_request = self.request.query_params.get('title', None)
        year_from_request = self.request.query_params.get('year', None)

        if title_from_request is not None and year_from_request is not None:
            queryset = queryset.filter(title = title_from_request, year = year_from_request)
        elif title_from_request is not None:
            queryset = queryset.filter(title = title_from_request)
        elif year_from_request is not None:
            queryset = queryset.filter(year = year_from_request)

        if queryset.exists():
            return queryset
        else:
            raise Http404

class CommentsListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    lookup_url_kwarg = 'filmid'
    def get_queryset(self):
        filmid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Comment.objects.filter(film = filmid)
        if queryset.exists():
            return queryset
        else:
            raise Http404

class RateListView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RateSerializer
    lookup_url_kwarg = 'rateid'
    def get_queryset(self):
        rateid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Rate.objects.filter(film = rateid)
        if queryset.exists():
            return queryset
        else:
            raise Http404
