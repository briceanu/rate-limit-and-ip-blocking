from rest_framework.permissions import BasePermission



# Build a backend service that implements 
# basic security features like rate limiting, IP blocking


# IP blocking
ips = []
base_ip = "234.34.100."



for i in range(235):
    ips.append(f"{base_ip}{i}")

class Prevent_Country_IPs(BasePermission):
    def has_permission(self, request, view):
        # try to get the ip from the 'http_x_forwarded_for' header
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
        if x_forwarded_for:
            x_forwarded_for_ip = x_forwarded_for.split(',')[0] 
        else:
            x_forwarded_for_ip = None
        # try to get the ip from the 'remote_addr' 
        remote_addr = request.META.get('REMOTE_ADDR', None)
        
        ip = x_forwarded_for_ip or remote_addr
        if ip is None:
            return False
        # block the request if the ip of the client is in the  
        # blocked ranges
        if ip in ips:
            return False
        return True


