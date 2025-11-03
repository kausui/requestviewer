FROM nginx:1.21-alpine

# ローカルのdefault.confをコンテナにコピー
COPY containers/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf
COPY containers/nginx/ssl/password /etc/nginx/conf.d/password
COPY containers/nginx/ssl/servercertfull.pem /etc/nginx/conf.d/servercertfull.pem
COPY containers/nginx/ssl/serverprivatekey.pem /etc/nginx/conf.d/serverprivatekey.pem