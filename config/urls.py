from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from ErrorHandle.views import error_404 ,error_403
#
# handler404 = error_404
# handler403 = error_403
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_honypot/', include('admin_honeypot.urls', namespace='admin_honeypot')),

    path('', include('Admin.urls')),
    path('', include('ACL.urls')),
    path('', include('Category.urls')),
    path('', include('Sms.urls')),
    path('', include('Call_Price.urls')),
    path('', include('ContactUs.urls')),
    path('', include('Cart.urls')),

    ## Auth ##
    path('', include('Auth.urls')),
    path('', include('social_django.urls', namespace='social')),

    # ## Admin ##
    # path('api/admin/categories/', include('Category.urls')),
    # path('api/admin/articles/', include('Article.urls')),
    # path('api/admin/users/', include('User.urls')),
    # path('api/admin/products/', include('Product.urls')),
    # path('api/admin/carts/', include('Cart.urls')),
    # path('api/admin/coupons/', include('Coupon.urls')),
    # path('api/admin/tickets/', include('Ticket.urls')),
    # path('api/admin/acl/', include('ACL.urls')),
    # path('api/admin/payments/', include('Payment.urls')),
    # path('api/admin/comments/', include('Comment.urls')),
    # path('api/admin/wishlists/', include('WishList.urls')),
    # path('api/admin/sliders/', include('Slider.urls')),
    # path('api/admin/likes_dislikes/', include('Like_And_DisLike.urls')),
    # path('api/admin/settings/', include('Setting.urls')),
    # path('api/admin/newsletters/', include('Newsletter.urls')),
    # path('api/admin/stars/', include('Star.urls')),
    # path('api/admin/orders/', include('Order.urls')),
    # path('api/admin/contact_us/', include('Contact_us.urls')),
    # path('api/admin/wallets/', include('Wallet.urls')),
    # path('api/admin/call/price/', include('Call_Price.urls')),
    #
    # ## AccountPanel ##
    # path('api/panel/', include('AccountPanel.urls')),
    #
    # ## Client ##
    # path('', include('Main.urls')),
    # path('checkout/', include('Cart_Checkout.urls')),
    # path('payment/', include('ZarinPal.urls')),
]

urlpatterns += [
    # path('api/auth/', include('Auth.api.urls')),
    # path('api/student/', include('Student.api.urls')),
    # path('api/teacher/', include('Teacher.api.urls')),
    # path('api/class/', include('Class.api.urls')),
    # path('api/blog/', include('Blog.api.urls')),
    # path('api/chat/', include('Chat.api.urls')),
    # path('api/quiz/', include('QuizBuilder.api.urls')),
    # path('api/installment/', include('Installment.api.urls')),
    # path('api/sms/', include('Sms.api.urls')),
    # path('api/shop/', include('Shop.api.urls')),
    # path('api/poll/', include('Poll.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
