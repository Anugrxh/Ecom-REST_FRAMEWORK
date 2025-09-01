from rest_framework import serializers
from .models import Category, Product, Cart, Rating, Order,ProductImage,OrderItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("slug", "created_at", "updated_at")

# shop/serializers.py

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]

class ProductSerializer(serializers.ModelSerializer):
    product_images = ProductImageSerializer(many=True, write_only=True, required=False)
    images = serializers.SerializerMethodField(read_only=True)  # For GET responses

    class Meta:
        model = Product
        fields = [
            "id", "category", "name", "description", "price",
            "discount_price", "is_featured", "stock_available",
            "slug", "created_at", "updated_at",
            "product_images", "images"  # write-only and read-only respectively
        ]
        read_only_fields = ("slug", "created_at", "updated_at", "images")

    def get_images(self, obj):
        return [img.image.url for img in obj.product_images.all()]

    def create(self, validated_data):
        product_images_data = self.context['request'].FILES.getlist('product_images')
        product = Product.objects.create(**validated_data)
        for image in product_images_data:
            ProductImage.objects.create(product=product, image=image)
        return product

    def update(self, instance, validated_data):
        product_images_data = self.context['request'].FILES.getlist('product_images')

        # Update regular fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if product_images_data:
            # Delete old images
            instance.product_images.all().delete()
            # Add new uploaded images
            for image in product_images_data:
                ProductImage.objects.create(product=instance, image=image)

        return instance


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ("user", "created_at", "product")

class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source='product', write_only=True)

    class Meta:
        model = Cart
        fields = ("id", "product", "product_id", "quantity", "added_at")

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ("id", "product", "quantity", "price_at_purchase")

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ("user", "total_amount", "status", "created_at", "order_items")
