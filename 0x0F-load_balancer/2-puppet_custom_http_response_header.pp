# configure an nginx web server
exec { 'Update apt repository':
  command => 'apt-get -y update',
  path    => '/usr/bin:/usr/sbin:/bin'
}

package { 'nginx':
  ensure  =>  installed,
}

file_line { 'add_headr':
  path  => '/etc/nginx/sites-available/default',
  after => 'server_name _;',
  line  => 'add_header X-Served-By $hostname always;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
