from rest_framework_simplejwt.tokens import  RefreshToken


def generate_tokens(username):
    refresh_token = RefreshToken.for_user(username)
    access_token = str(refresh_token.access_token)
    return {"access token":access_token,
            'refresh_token':str(refresh_token)}