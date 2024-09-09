# Use the official Nginx image as the base image
FROM nginx:latest

# Set a build argument for Nginx configuration file
ARG NGINX_CONF=/etc/nginx/nginx.conf

COPY etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY var/www/abogutskiy.cloud /usr/share/nginx/html/
COPY var/certs/ /etc/nginx/certs/

# Expose the necessary ports (80 for HTTP and 443 for HTTPS)
EXPOSE 80
EXPOSE 443

# Start Nginx when the container launches
CMD ["nginx", "-g", "daemon off;"]

