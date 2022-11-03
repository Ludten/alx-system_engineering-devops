# Fix apache wordpress server
exec { 'fix_apache_wordpress':
  command => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
}
