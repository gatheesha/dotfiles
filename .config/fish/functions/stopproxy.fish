function stopproxy
    set -l PROXY_ENV http_proxy ftp_proxy https_proxy all_proxy HTTP_PROXY HTTPS_PROXY FTP_PROXY ALL_PROXY
    for envar in $PROXY_ENV
        set -g -x $envar
    end
    echo "proxy stopped..."
end
