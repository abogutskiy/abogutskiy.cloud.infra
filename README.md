# About 
This is a repository with the default configuration for abogutskiy.cloud 
droplets. It includes configuration for [Nginx](https://nginx.org/en/), 
[Wireguard](https://www.wireguard.com/), [XRay](https://github.com/XTLS/Xray-core)
and (`TODO`) [amnezia](https://amnezia.org/en) docker images. 

There are three ways (profiles) to setup docker:
 * default
 * local
 * isolated

Default profile is used for production droplets used in abogutskiy.cloud
dns records. Local profile is useful for debuging and isolated profile is 
the most convenient one.

# Default profile
This profile  setup locate configs on host machine and mount them into containers.
This approach is useful cos we can see/modify configs without rebuilding 
the container. 

For production setup we locate wireguard configs in */etc/wireguard*, xray 
configs in */etc/xray*, amnezia in */etc/amnezia*, ssl certs in */var/certs*
and static content for nginx in */var/www*.

# Local profile
The same as default profile but arrange configs in specific folder and 
mount it from there. For instance production configs with local profile 
and */tmp/vpn-conf* local folder will locate wireguard configs in
*/tmp/vpn-conf/etc/wireguard*, xray configs in */tmp/vpn-conf/etc/xray*,
etc and mount them into docker images.

# Isolated setup
Just build the images with pre-copied configs inside

# Supported protocols

## Wireguard 
Pure vpn tunnel, nothing more. Fast and reliable but, won't help against DPI.
Download clients [here](https://www.wireguard.com/install/)

## XRay
Most popular protocols stack to bypass content moderation. Very popular in China,
works even with DPI. Supports [wide range](https://github.com/XTLS/Xray-examples/tree/main/All-in-One-fallbacks-Nginx#xray---all-in-one-configuration--nginxdecoy-website)
of protocols.

In this repository we'll set up configs for:
 * vmess + tcp + tls
 * vless + tcp + tls (`TODO add configs`) 
 * shadowsocks + tcp + tls (`TODO add configs`)
 * trojan + tcp + tls (`TODO add configs`)

## Amnezia
Russian protocols stack to bypass content moderation. Popular in Russia,
based on openVPN protocol and can use [several protocols](https://docs.amnezia.org/documentation/how-amnezia-works#how-does-traffic-masking-work-)
to mask the traffic.

 `TODO add amnezia support`

# Prerequisites

This setup can be used on any linux VM, but you need to install docker, 
git, git-crypto, setup ipv6 and maybe something else.

Setup will definitely run with:
 * Ubuntu 24
 * Preconfigured with https://github.com/abogutskiy/environment
