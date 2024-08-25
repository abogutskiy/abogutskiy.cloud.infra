# Use an Alpine Linux base image
FROM ubuntu:latest

# Install WireGuard and other necessary tools
RUN apt-get update && \
    apt-get install -y wireguard iproute2 resolvconf iptables && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Expose the WireGuard port
EXPOSE 51820/udp

# Command to start WireGuard
CMD ["wg-quick", "up", "wg0"]
