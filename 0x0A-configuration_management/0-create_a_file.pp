#puppet that creates a file and define the file attributes

file { '/tmp/school':
ensure  => present,
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet'
}