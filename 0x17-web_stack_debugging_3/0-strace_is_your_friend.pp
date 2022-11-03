# Fix apache wordpress server
exec { 'fix_apache_wordpress':
  command => '/usr/bin/env sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}
