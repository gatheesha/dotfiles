function setproxy
    set proxy_value "http://192.168.42.129:44355"
    set no_proxy_value "localhost,127.0.0.1,LocalAddress,LocalDomain.com"

    set -l PROXY_ENV http_proxy ftp_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY FTP_PROXY ALL_PROXY
    set -l NO_PROXY_ENV no_proxy NO_PROXY
    for envar in $PROXY_ENV
      set -g -x $envar $proxy_value
    end
    for envar in NO_PROXY_ENV
      set -g -x $envar $no_proxy_value
    end
    echo "proxy started..."
    echo "$http_proxy"
end
