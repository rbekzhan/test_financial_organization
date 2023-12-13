FROM nginx:stable-perl
WORKDIR /var/www

RUN rm /etc/nginx/conf.d/default.conf
RUN rm /etc/nginx/nginx.conf
RUN mkdir -p static

COPY server.conf /etc/nginx/conf.d
COPY nginx.conf /etc/nginx
