from django.urls import path
from .views import MessageSendView, MessageAllView, PreviousMessageView, MessageReceiveView, MessageOnlyReceiveView

urlpatterns = [
    path('', MessageSendView.as_view()),
    path('all', MessageAllView.as_view()),
    path('userchat', PreviousMessageView.as_view()),
    path('receiver', MessageReceiveView.as_view()),
    path('receiveonly', MessageOnlyReceiveView.as_view())
]