#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginex/conf.d/default.conf
nginex -g 'daemon off;'