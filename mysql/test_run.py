import sys
import _mysql


db = _mysql.connect('mysqlserver', 'root', 'password')
sys.exit(0)
