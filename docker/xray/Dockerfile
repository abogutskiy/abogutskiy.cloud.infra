FROM alpine:latest

ENV XRAY_VERSION 1.8.1

RUN apk add --no-cache curl

RUN curl -L -o /usr/local/bin/xray https://github.com/XTLS/Xray-core/releases/download/v${XRAY_VERSION}/Xray-linux-64.zip && \
    unzip /usr/local/bin/xray -d /usr/local/bin && \
    chmod +x /usr/local/bin/xray

RUN mkdir -p /etc/xray

# Copy your configuration files to the container
COPY etc/xray/ /etc/xray

# Expose the necessary ports
EXPOSE 9090

# Run Xray
CMD ["xray", "-c", "/etc/xray/config.json"]
