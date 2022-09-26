# configure an nginx web server
exec { 'Update apt repository':
  command => 'apt-get -y update',
  path    => '/usr/bin:/usr/sbin:/bin'
}

package { 'nginx':
  ensure  =>  installed,
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file_line { 'index':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=dQw4w9WgXcQ permanent;',
}

file_line { 'add_headr':
  path  => '/etc/nginx/sites-available/default',
  after => '^[ \t]{1,}location \/ {',
  line  => 'add_header X-Served-By $hostname always;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
