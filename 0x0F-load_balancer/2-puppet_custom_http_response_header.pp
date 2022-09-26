# configure an nginx web server
exec { 'Update apt repository':
  command => 'apt-get -y update',
  path    => '/usr/bin:/usr/sbin:/bin'
}

package { 'nginx':
  ensure  =>  installed,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}

file_line { 'add_headr':
  notify  => Service['nginx'],
  path    => '/etc/nginx/sites-available/default',
  after   => '^[ \t]{1,}location \/ {',
  line    => 'add_header X-Served-By $hostname always;',
  require => Package['nginx'],
}
