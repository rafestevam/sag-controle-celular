import sys
import site

site.addsitedir('/var/www/sag-controle-celular/controlcel/lib/python3.6/site-packages')
sys.stdout = sys.stderr
sys.path.insert(0, '/var/www/sag-controle-celular/api-controle-celular/api')


from app import app as application