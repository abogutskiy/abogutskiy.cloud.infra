# Use linuxserver/wireguard as the base image
FROM linuxserver/wireguard:latest

# Set the default port and port delta
ARG PORT=51820

COPY etc/wireguard/ /etc/wireguard/
EXPOSE 51820

# Run the base image's entrypoint script
ENTRYPOINT ["/init"]
