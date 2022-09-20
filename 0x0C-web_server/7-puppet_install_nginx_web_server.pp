# configure an nginx web server
package { 'nginx':
  ensure  =>  installed
}
file { 'index':
  ensure  =>  file,
  path    =>  '/var/www/html/index.html',
  content =>  "Hello World!\n"
}
file_line { 'redirect':
  ensure =>  present,
  path   =>  '/etc/nginx/sites-available/default',
  line   =>  'rewrite ^/redirect_me/$ https://www.youtube.com/watch?v=dQw4w9WgXcQ\ permanent;',
  after  =>  'server_name _;'
}
service { 'nginx':
  ensure  =>  running,
  require =>  Package['nginx']
}
