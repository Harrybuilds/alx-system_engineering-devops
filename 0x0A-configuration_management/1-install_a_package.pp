#puppet manifest to install python's flask package using pip

exec { 'install-werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.0.2'
  }

exec { 'install-flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep Version | grep q- 2.1.0',
}

