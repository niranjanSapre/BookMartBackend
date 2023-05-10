from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView, DestroyAPIView
from .models import Book_Detail, Book_Images
from .serializers import BookDetailsSerializer, BookImageSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
import cv2
#import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Create your views here.

class BookDetailsList(ListCreateAPIView):

    serializer_class = BookDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Book_Detail.objects.filter(user=self.request.user)
    
class BookDetailsView(RetrieveUpdateDestroyAPIView):

    serializer_class = BookDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def get_queryset(self):
        return Book_Detail.objects.filter(user=self.request.user)
    
class AllBooksView(ListCreateAPIView):

    serializer_class = BookDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Book_Detail.objects.all()
    
class UserUploadedBooksView(ListCreateAPIView):

    serializer_class = BookDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user)
        return Book_Detail.objects.filter(user=self.request.user)
    

class BookImageSaveView(ListCreateAPIView):
    serializer_class = BookImageSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Book_Images.objects.filter(user=self.request.user)
    
class BookImageDeleteView(DestroyAPIView):
    serializer_class = BookImageSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Book_Images.objects.filter(user=self.request.user)
    
class BookEstimatedPriceView(GenericAPIView):
    def get(self, request):

        def rgb_to_hex(rgb_color):
            hex_color = "#"
            for i in rgb_color:
                i = int(i)
                hex_color += ("{:02x}".format(i))
            return hex_color

        user_id = self.request.user
        images = Book_Images.objects.filter(user=user_id).order_by('-timestamp').first()  
        print(images)
        image_id = images.id
        print(image_id)

        img1 = str(images.book_page1.path)
        img2 = str(images.book_page2.path)
        img3 = str(images.book_page3.path)
        originalPrice = images.price
        print(originalPrice)

        if originalPrice == None or originalPrice == 0:
            price = 200 
        else:
            price = originalPrice

        img1 = cv2.imread(str(img1))
        img2 = cv2.imread(str(img2))
        img3 = cv2.imread(str(img3))

        img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        img3 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

        n_clusters = 1
       
        list_hex = []
        img_list = [img1, img2, img3]
        for item in img_list:
            kmeans = KMeans(n_clusters)
            kmeans.fit(item)
            colors = kmeans.cluster_centers_
            labels = kmeans.labels_

            label_count = [0 for i in range(n_clusters)]

            for ele in labels:
                label_count[ele] += 1
            index_color = label_count.index(max(label_count))
        

            dict_colour_percen = {}
            print
            for index, ele in enumerate(label_count):
                hex_color = rgb_to_hex(colors[index])
                list_hex.append(hex_color)
                color_percen = float(ele)/len(labels)*100
                dict_colour_percen[hex_color] = color_percen
            #plt.show()

        list_first_index = []
        for items in list_hex:
            list_first_index.append(items[1:2])
    
        estimated_price = 0
        list_per = []
        for items in list_first_index:
            if(items=='0' or items=='1'):
                list_per.append(20)
            if(items=='2'):
                list_per.append(26.3)
            if(items=='3'):
                list_per.append(32.6)
            if(items=='4'):
                list_per.append(38.9)
            if(items=='5'):
                list_per.append(45.2)
            if(items=='6'):
                list_per.append(51.5)
            if(items=='7'):
                list_per.append(57.8)
            if(items=='8'):
                list_per.append(64.1)
            if(items=='9'):
                list_per.append(70.4)
            if(items=='a'):
                list_per.append(76.7)
            if(items=='b'):
                list_per.append(83)
            if(items=='c'):
                list_per.append(89.3)
            if(items=='d'):
                list_per.append(90)
            if(items=='e'):
                list_per.append(90)
            if(items=='f'):
                list_per.append(90)
        sum = 0
        for item in list_per:
            sum+=item
        avg_per=sum/len(list_per)
        estimated_price = price*(avg_per/100)
        estimated_price = format(estimated_price,'.2f')
        
        data = {
            'est_price': estimated_price,
            'id': image_id
        }

        return Response(data, status=status.HTTP_200_OK)