from models import Usuario

def get_dados_facebook(
    strategy,
    user,
    response,
    details,
    is_new=False,
    *args,
    **kwargs
    ):
    
    if "facebook" in kwargs['backend'].redirect_uri:
        
        #Recupera imagem perfil facebook
        img_url = 'http://graph.facebook.com/%s/picture?type=large' % response['id']
                
        usuario = Usuario.objects.get_or_create(email = user)[0]
        usuario.typeaccount = 'facebook'
        usuario.photo = img_url        
        usuario.username = response['name']
        usuario.save()