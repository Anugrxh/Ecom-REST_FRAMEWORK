from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Category, Product, Cart, Rating, Order ,OrderItem
from .serializers import CategorySerializer, ProductSerializer, CartSerializer, RatingSerializer, OrderSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

# Categories
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]

class CategoryRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]

    def create(self, request, *args, **kwargs):
        name = request.data.get("name")
        if Category.objects.filter(name__iexact=name).exists():
            return Response(
                {"error": f"Category '{name}' already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)

# Products
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAdminUser()]
        return [AllowAny()]


class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [IsAdminUser()]
        return [AllowAny()]




# Ratings
class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        product_id = self.kwargs['pk']
        serializer.save(user=self.request.user, product_id=product_id)

class RatingListView(generics.ListAPIView):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.filter(product_id=self.kwargs['pk']).order_by('-created_at')

# Cart
class CartListView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartAddView(generics.CreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartUpdateView(generics.UpdateAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartRemoveView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

# Orders
class OrderCheckoutView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        cart_ids = self.request.data.get('cart_items', [])
        carts = Cart.objects.filter(user=user, id__in=cart_ids)

        if not carts.exists():
            return Response({"error": "No valid cart items provided."}, status=status.HTTP_400_BAD_REQUEST)

        total = 0
        for item in carts:
            price = item.product.discount_price if item.product.discount_price else item.product.price
            total += price * item.quantity

        order = serializer.save(user=user, total_amount=total, status='PENDING')

        # Create OrderItems from Cart items
        order_items = []
        for item in carts:
            order_items.append(
                OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price_at_purchase=item.product.discount_price if item.product.discount_price else item.product.price
                )
            )
        OrderItem.objects.bulk_create(order_items)

        carts.delete()  # Clear cart after order


# List Orders
class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
