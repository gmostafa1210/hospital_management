import xmlrpc.client

url = 'http://localhost:8014'
db = 'hospital-14'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))

# Authentication
uid = common.authenticate(db, username, password, {})
if not uid:
    print('Authentication failed.')
    exit()

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Search Count Method
partners_count = models.execute_kw(
    db, uid, password, 'res.partner', 'search_count', 
    [[['is_company', '=', True]]])
print("\npartners_count", partners_count)

# Search Method
partners = models.execute_kw(
    db, uid, password, 'res.partner', 'search', 
    [[['is_company', '=', True]]], 
    {'offset': 3, 'limit': 2})
print("\npartners", partners)

# Read Method
partner_rec = models.execute_kw(
    db, uid, password, 'res.partner', 'read', 
    [partners],
    {'fields': ['id', 'name']})
print("\npartner_rec", partner_rec)

# Search Read Method
partner_search_read = models.execute_kw(
    db, uid, password, 'res.partner', 'search_read', 
    [[['is_company', '=', True]]], 
    {'fields': ['id', 'name'], 'limit': 2})
print("\npartner_search_read", partner_search_read)



