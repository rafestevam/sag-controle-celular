#!/usr/bin/env python

# from app import app

# # Inicialização da app Python
# if __name__ == '__main__':
#     app.run()

import sys
import site

site.addsitedir('/var/www/sag-controle-celular/api-controle-celular/controlcel/lib/python3.6/site-packages')
sys.path.insert('/var/www/sag-controle-celular/api-controle-celular/controlcel')

from app import app as application