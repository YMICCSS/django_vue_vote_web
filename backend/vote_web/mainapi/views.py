
# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from .models import *
from .serializers import ItemSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.db import transaction
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

        try:
            with transaction.atomic():
                for item in items:
                    # 記錄投票人跟投的項目
                    vote = Vote(voter_name=voter_name)
                    vote.item = item
                    vote.save()
                    # 將票數增加
                    item.votes = Vote.objects.filter(item=item).count()
                    item.save()
        except Exception as e:
            Exception('Unexpected error: {}'.format(e))

        # 序列化，返回結果
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

