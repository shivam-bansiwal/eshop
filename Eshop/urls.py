from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('cart/',views.cartDetails),
    path('checkout/',views.checkoutDetails),
    path('contact/',views.contactDetails),
    path('confirm/',views.confirm),
    path('wishlist/<int:num>/',views.wishlistDetails),
    path('wishlist/',views.wishlist),
    path('deletewishlist/<int:num>/',views.wishlistDelete),
    path('login/',views.loginDetails),
    path('product/<int:num>/',views.productDetails),
    path('shop/<str:cat>/<str:br>/',views.shopDetails),
    path('signup/',views.signupUser),
    path('profile/',views.profile),
    path('logout/',views.logout),
    path('addproduct/',views.addproduct),
    path('deleteproduct/<int:num>/',views.deleteProduct),
    path('editproduct/<int:num>/',views.editProduct),
    path('deletecart/<int:num>/',views.deletecart),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
