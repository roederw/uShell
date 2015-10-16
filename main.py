from uvaclient import uvaclient

u = uvaclient()
u.login()
u.submit("100", "100.cpp")
