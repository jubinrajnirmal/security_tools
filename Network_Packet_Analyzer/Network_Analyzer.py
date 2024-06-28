from scapy.all import sniff, IP, TCP, UDP

def packet_inspector(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        #Protocol_ID -> https://www.oreilly.com/library/view/internet-core-protocols/1565925726/re09.html
        if protocol == 6:
            protocol_name = 'TCP'
        elif protocol == 17:
            protocol_name = 'UDP'
        else:
            protocol_name = 'Other'

        print(f'\nIP packet: {src_ip} -> {dst_ip} (Protocol: {protocol_name})')

        #TCP Packet Handling
        if packet.haslayer(TCP):
            tsport = packet[TCP].sport
            tdport = packet[TCP].dport
            print(f'\nTCP segment = Source Port: {tsport}, Destination Port: {tdport}')
            if packet[TCP].payload:
                print(f'Payload: {bytes(packet[TCP].payload)}')

        #UDP Packet Handling
        elif packet.haslayer(UDP):
            usport = packet[UDP].sport
            udport = packet[UDP].dport
            print(f'UDP segment: Source Port: {usport}, Destination Port: {udport}')
            if packet[UDP].payload:
                print(f'Payload: {bytes(packet[UDP].payload)}')

        else:
            print('No TCP/UDP Packets')

def user_consent():
    print("This network packet sniffer tool captures and analyzes network packets.")
    print("Ensure that you have the right permission needed to monitor network traffic on this network.")
    print("Unauthorized use of this packet sniffing tool can violate privacy and network security policies!")
    print("Use this tool for testing or educational purposes and within legal boundaries only!")
    consent = input("Do you acknowledge and agree to these terms? (Y/N): ").strip().lower()
    return consent == "y"

def main():
    if not user_consent():
        print('Consent not given, exiting program!')
        return
    print('This tool does not save the output, every packet is analyzed on the fly and then discarded!')
    print("Starting to sniff this network...")
    sniff(prn=packet_inspector, store=0)

if __name__ == '__main__':
    main()