from vk_api import Vk
from pprint import pprint

if __name__ == '__main__':
    user_id = '289854633'
    access_token = 'vk1.a.FzH7FIejX2D1IpjZg_aeijq2AidOJibdTNFbjqFkeIJUWLipr87v0zRJL0jOklCQtV_wVsXqoZF3BXbqGwVnTL8kJ1QqH_z4M2bSUqmRS9Mjp83ftDxQEYWWh5Z0d4LI-yBD7qA5MPC1T9ZTyJxFoPa2whkP4a0EGWvLJSU7xtz6dn4hJOlxoFANYSirkvC0'
    vk = Vk(access_token, user_id)
    pprint(vk.get_users_photos())
