# Fix apache wordpress server
exec { 'fix_apache_wordpress':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
}
