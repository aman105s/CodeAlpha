from scapy.all import sniff

def packet_callback(packet):
    # Display the packet summary
    print(packet.summary())
    
    # Check if the packet has IP layer
    if packet.haslayer('IP'):
        ip_layer = packet['IP']
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        
        # Check if the packet has a TCP layer
        if packet.haslayer('TCP'):
            tcp_layer = packet['TCP']
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        
        # Check if the packet has a UDP layer
        elif packet.haslayer('UDP'):
            udp_layer = packet['UDP']
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
        
        # Print the payload if available
        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"Payload: {payload}")

# Start sniffing packets
print("Starting packet capture...")
sniff(prn=packet_callback, store=0)
