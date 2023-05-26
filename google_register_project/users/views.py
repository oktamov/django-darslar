# views.py
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.models import SocialToken

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter

class GoogleRegister(APIView):
    def post(self, request):
        token = request.data.get('access_token')
        if token:
            try:
                # Google API'ga HTTP POST so'rovi yuborish
                response = requests.get(
                    'https://www.googleapis.com/oauth2/v3/userinfo',
                    params={'access_token': token}
                )
                response.raise_for_status()

                # Foydalanuvchi haqida ma'lumotlarni olish
                user_data = response.json()
                email = user_data.get('email')
                name = user_data.get('name')

                # Foydalanuvchi hisobini yaratish
                user = User.objects.create(username=email, email=email, first_name=name)
                token = SocialToken.objects.create(user=user, token=token)

                return Response({'token': token.key})

            except requests.RequestException:
                return Response({'error': 'Invalid access token'}, status=400)
        else:
            return Response({'error': 'Access token is required'}, status=400)
