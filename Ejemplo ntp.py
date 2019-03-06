import ntplib
from time import ctime

c = ntplib.NTPClient()

response = c.request('europe.pool.ntp.org', version=3)

print(response.offset)
print(response.version)
print(ctime(response.tx_time))

print(response.leap)
print(ntplib.leap_to_text(response.leap))

print(response.root_delay)

print(response.ref_id)
print(ntplib.ref_id_to_text(response.ref_id))
