from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST', 'DELETE'])
def api_auth(request):
    
    if request.method == 'GET':
        if request.user.is_authenticated():
            return Response({'user_id': request.user.id})
        return Response({'user_id': None})
    
    elif request.method == 'POST':
        username = request.DATA.get('username')
        password = request.DATA.get('password')
        user = authenticate(username=username, password=password)
        if not user is None:
            if user.is_active:
                login(request, user)
                data = {'success': True, 'user_id': user.id}
                return Response(data)

            return Response({'success' : False, 'user_id' : None, 
                             'message' : 'inactive'})
        return Response({'success' : False, 'user_id' : None, 
                             'message' : 'invalid'})

    elif request.method == 'DELETE':
        logout(request)
        return Response(status = status.HTTP_204_NO_CONTENT)

