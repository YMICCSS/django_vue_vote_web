
# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import *
from .serializers import ItemSerializer, VoteSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics, status
class ItemListCreateView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemRetrieveDeleteView(RetrieveDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class VoteAPIView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def create(self, request, *args, **kwargs):
        selected_items = request.data.get('items', [])
        voter_name = request.data.get('voter_name', '').strip()

        # 檢查投票人名字和選擇的投票項目是否合法
        if not selected_items or not voter_name:
            return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

        items = Item.objects.filter(id__in=selected_items)

        if len(items) != len(selected_items):
            return Response({'error': 'Invalid input'}, status=status.HTTP_400_BAD_REQUEST)

        # 將選擇的投票項目加入到投票table中
        for item in items:
            vote = Vote(voter_name=voter_name)
            vote.item = item
            vote.save()

        for item in items:
            item.votes = Vote.objects.filter(item=item).count()
            item.save()

        # 序列化，返回結果
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

