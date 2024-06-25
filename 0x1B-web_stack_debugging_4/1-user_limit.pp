# Define a class to manage open file limits
class { 'limits': }

# Define a specific limit for the 'holberton' user
limits::limits {
  'holberton-open-files': ensure => present,
    domain                       => 'user',
    type                         => 'soft',
    item                         => 'nofile',
    value                        => 1024, # Change this value as needed (default system limit)
}
