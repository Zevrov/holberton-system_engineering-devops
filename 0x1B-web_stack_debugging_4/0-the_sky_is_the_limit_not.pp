# fix open file limit on nginx
file { 'let Nginx open more files':
  content => 'ULIMIT="-n 1048576"',
  ensure  => file,
  path    => '/etc/default/nginx'
}

service { 'Nginx':
  ensure     => running,
  hasrestart => true,
  name       => 'nginx',
  subscribe  => File['/etc/default/nginx']
}
