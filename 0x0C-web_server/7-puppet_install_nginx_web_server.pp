# configure an nginx web server
package { 'nginx':
  ensure  =>  latest
}
service { 'nginx':
  ensure  =>  running,
  enable  =>  true,
  require =>  Package['nginx']
}
file { 'index':
  ensure  =>  file,
  path    =>  '/var/www/html/index.html',
  content =>  "Hello World!"
}
file_line { 'redirect':
  ensure  =>  present,
  notify  =>  Service['nginx'],
  path    =>  '/etc/nginx/sites-available/default',
  require =>  Package['nginx'],
  line    =>  "\n\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=dQw4w9WgXcQ\\ permanent;",
  after   =>  'server_name _;'
}
