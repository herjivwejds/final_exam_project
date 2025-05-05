from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, UserProfile

@api_view(['POST'])
def register_user(request):
    telegram_id = request.data.get("telegram_id")
    full_name = request.data.get("full_name")
    user, created = UserProfile.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={'full_name': full_name}
    )
    return Response({"status": "ok", "new": created})

@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    if not products:
        return Response({"message": "Bu yerda taomlar ro'yxati bo'ladi (keyinchalik qo'shamiz)."})
    data = []
    for product in products:
        data.append({
            "id": product.id,
            "name": product.name,
            "price": str(product.price),
            "image": request.build_absolute_uri(product.image.url)
        })
    return Response(data)
