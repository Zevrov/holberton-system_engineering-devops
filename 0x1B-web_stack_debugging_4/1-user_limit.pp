# remove open file limit for a user
file { 'remove user limit':
  content => '\n',
  ensure  => file,
  path    => '/etc/security/limits.conf'
}
