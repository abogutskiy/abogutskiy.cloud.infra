FROM caddy:2.8.4-alpine

WORKDIR /var/www

COPY ../html/ /var/www/html/
COPY ../static/ /var/www/static/

COPY ../caddy/Caddyfile /etc/caddy/Caddyfile

EXPOSE 80
EXPOSE 443
EXPOSE 2019 # admin api

# The base Caddy image has a default command to run Caddy (`caddy run --config /etc/caddy/Caddyfile`).
# By copying our Caddyfile to the default location, we don't need to specify a CMD or ENTRYPOINT.
# The base image will automatically pick up our configuration.
