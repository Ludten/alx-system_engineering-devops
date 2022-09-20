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
  ensure =>  present,
  path   =>  '/etc/nginx/sites-available/default',
  line   =>  "\n\trewrite ^/redirect_me/$ https://www.youtube.com/watch?v=dQw4w9WgXcQ\\ permanent;",
  after  =>  'server_name _;'
}
file { 'custom_404':
  ensure  =>  file,
  path    =>  '/usr/share/nginx/html/custom_404.html',
  content =>  "Ceci n'est pas une page"
}

$new_line = "\n\terror_page 404 /custom_404.html;\n\tlocation = /custom_404.html {\n\t\troot /usr/share/nginx/html;\n\t\tinternal;\n\t}"

file_line { 'error_404':
  ensure  =>  present,
  notify  =>  Service['nginx'],
  path    =>  '/etc/nginx/sites-available/default',
  require =>  Package['nginx'],
  line    =>  $new_line,
  after   =>  'rewrite \^\/redirect_me\/\$ https\:\/\/www\.youtube\.com\/watch\?v=dQw4w9WgXcQ\\ permanent;'
}
