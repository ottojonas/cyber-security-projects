import sys

from icecream import ic
from scapy.all import sniff
from scapy.layers.inet import IP, TCP


# func to handle each packet
def handle_packet(packet, log):

    # check if packet has TCP layer
    if packet.haslayer(TCP):

        # fetch source and destination ip
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        # extract source and destination ports
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        # write packet info to log file
        log.write(f"TCP connection: {src_ip}:{src_port} => {dst_ip}:{dst_port}\n")


# main func to start packet sniffing
def main(interface, verbose=False):
    # create log file name based on interface
    logfile_name = f"log_files/sniffer_{interface}_log.txt"
    # open log file for writing
    with open(logfile_name, "w") as logfile:
        try:
            # start packet sniffinf on interface with verbose output
            if verbose:
                sniff(
                    iface=interface,
                    prn=lambda pkt: handle_packet(pkt, logfile),
                    store=0,
                    verbose=verbose,
                )
            else:
                sniff(
                    iface=interface,
                    prn=lambda pkt: handle_packet(pkt, logfile),
                    store=0,
                )
        except KeyboardInterrupt:
            sys.exit(0)


# check if script is run directly
if __name__ == "__main__":
    # check if correct number of args are being passed
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        ic("usage: python main.py <interface> [verbose]")
        sys.exit(1)
    # determine if verbose is enabled
    verbose = False
    if len(sys.argv) == 3 and sys.argv[2].lower() == "verbose":
        verbose = True
    # call main func with specified interface and verbose option
    main(sys.argv[1], verbose)
