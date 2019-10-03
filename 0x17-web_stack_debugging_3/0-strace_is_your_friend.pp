# Fix to config file

exec {'fix php extension':
  command  => 'sed -ri "s,phpp,php," /var/www/html/wp-settings.php',
  provider => shell,
}
