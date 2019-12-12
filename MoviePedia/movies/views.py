from django.shortcuts import render
from rest_framework import viewsets, generics, status
from db.models import Film, Rate, Comment
from movies.serializers import FilmSerializer, CommentSerializer, RateSerializer
from movies.permissions import IsGetOrIsAuthenticated
from django.http import Http404, HttpResponseBadRequest
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


# Create your views here.
class FilmListView(viewsets.ModelViewSet):
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
    queryset = Comment.objects.all()

    def get_queryset(self):
        filmid = self.kwargs.get(self.lookup_url_kwarg)
        queryset = Comment.objects.filter(film = filmid)

        if queryset.exists():
            return queryset
        else:
            raise Http404

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data = request.data)

        if serializer.is_valid():
            if Film.objects.filter(pk = self.kwargs.get(self.lookup_url_kwarg)).exists():
                serializer.save(film_id = self.kwargs.get(self.lookup_url_kwarg))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise Http404

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def post(self, request, *args, **kwargs):
        serializer = RateSerializer(data = request.data)

        if serializer.is_valid():
            if Film.objects.filter(pk = self.kwargs.get(self.lookup_url_kwarg)).exists():
                serializer.save(film_id = self.kwargs.get(self.lookup_url_kwarg))
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                raise Http404

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
