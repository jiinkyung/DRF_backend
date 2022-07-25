
# 비건식당 커뮤니티
 
## 🍃구현 기능
### 1️⃣ 게시판 기능: 전체 게시물 조회 및 등록
> models.py
```python
class Vegan(models.Model):
    title = models.CharField(max_length=200) # 글 제목
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 글 작성자
    description = models.TextField(blank=True) # 글 내용
    created = models.DateTimeField(auto_now_add=True) # 작성 날짜

    def __str__(self):
        return self.title
```

> serializer.py
```python
# 전체 게시물 조회
class VeganSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegan
        fields = ('id', 'title', 'author', 'description')
# 게시물 등록
class VeganCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegan
        fields = ('title','author', 'description')
# 게시물 세부 조회
class VeganDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vegan
        fields = ('id', 'title', 'author', 'description', 'created')
```

> views.py  
```python
class VeganAPIView(APIView): 
    # http://<hi>127.0.0.1:8000/vegan/
    # 전체 등록된 게시물 조회
    def get(self, request):
        vegans = Vegan.objects.all()
        serializer = VeganSimpleSerializer(vegans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # 게시물 등록
    def post(self, request):
        serializer = VeganCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# 게시물 세부 조회 
# http://127.0.0.1:8000/vegan/{pk}/
class VeganDetailAPIView(APIView):
    def get(self, request, pk):
        vegan = get_object_or_404(Vegan, id=pk)
        serializer = VeganDetailSerializer(vegan)
        return Response(serializer.data, status=status.HTTP_200_OK)
```  

### 2️⃣ 댓글 기능
> models.py
```python
class Comment(models.Model):
    comment = models.TextField() # 댓글 내용 
    author = models.ForeignKey(User, on_delete=models.CASCADE) # 댓글 작성자
    date = models.DateTimeField(auto_now_add=True) # 댓글 작성 날짜
    post = models.ForeignKey(Vegan, null=True, blank=True, on_delete=models.CASCADE) # 해당 댓글이 달려있는 게시물

    def __str__(self):
        return self.comment
```  
> serializers.py
```python
# 전체 댓글 
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'comment', 'author', 'date', 'post')
# 댓글 생성
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
```        
> views.py
```python
# 전체 댓글 조회
# http://127.0.0.1:8000/comment/
class CommentAPIView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# 댓글 상세 조회
# http://127.0.0.1:8000/comment/{post_id}/
class CommentDetailAPIView(APIView):
    def get(self, request, post_id):
        comments = get_object_or_404(Comment, id=post_id)
        serializer = CommentSerializer(comments)
        return Response(serializer.data, status=status.HTTP_200_OK)

class VeganDetailAPIView(APIView):
    # 해당 글에 댓글쓰기
    # http://127.0.0.1:8000/vegan/{pk}/
    def post(self, request, pk):
        post = get_object_or_404(Vegan, id= pk)
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(post=post) 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```        

### 3️⃣ 회원가입/로그인
> models.py
```python
from django.contrib.auth.models import User
```  
> views.py
```python
# 회원가입
# http://127.0.0.1:8000/signup/
class SignupAPIView(APIView):
    def post(self, request):
        user = User.objects.create_user(username=request.data['id'], password=request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"Token": token.key})

# 로그인
# http://127.0.0.1:8000/login/
class LoginAPIView(APIView):
    def post(self, request):
        user = auth.authenticate(username=request.data['id'], password=request.data['password'])
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({"Token": token.key})
        else:
            return Response(status=401)
```            
