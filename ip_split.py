# A simple script for splitting an IP address into array elements

ip_address = input("IP Address: ")
ip_split = ip_address.split('.')
points = '.'

print("Part 1:", ip_split[0])
print("Part 2:", ip_split[1])
print("Part 3:", ip_split[2])
print("Part 4:", ip_split[3])
final_ip = ip_split[0] + points + ip_split[1] + points + ip_split[2] + points + ip_split[3]
print("IP Address: ", final_ip)