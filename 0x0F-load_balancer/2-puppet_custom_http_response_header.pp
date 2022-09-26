# configure an nginx web server
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

file_line { 'index':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;',
  require => Package['nginx'],
}

file_line { 'add_headr':
  ensure  => present,
  path    => '/etc/nginx/sites-available/default',
  after   => 'server_name _;',
  line    => 'add_header X-Served-By $hostname always;',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
