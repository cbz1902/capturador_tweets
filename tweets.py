######################Clase que nos premite modelar un tweets como un objeto############################################
class tweets:
    def __init__(self,tweet,user,mencion,localizacion,hashtag):
        """Inicializador de la clase"""
        self.tweet = tweet
        self.user = user
        self.mencion = mencion
        self.localizacion = localizacion
        self.hashtag = hashtag
    def get_tweet(self):
        """Muestra el texto del tweet"""
        return self.tweet
    def get_user(self):
        """Muestra el usuario quién realizó el tweet"""
        return self.user
    def get_mencion(self):
        """Muestra la mención que hay en tweet"""
        return self.mencion
    def get_localizacion(self):
        """Muestra las coordenadas desde donde se realizó el tweet"""
        return self.localizacion
    def get_hashtag(self):
        """Muestra los hashtag que se mecionaron en el tweet"""
        return self.hashtag



