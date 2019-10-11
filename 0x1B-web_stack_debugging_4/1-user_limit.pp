# remove open file limit for a user
file { 'remove user limit':
  ensure  => file,
  path    => '/etc/security/limits.conf',
  content => '\n'
}
