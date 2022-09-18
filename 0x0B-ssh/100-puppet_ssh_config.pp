# edit ssh config file
file_line { 'identityfile':
  ensure  =>  present,
  path    =>  '/etc/ssh/ssh_config',
  line    =>  'IdentityFile ~/.ssh/school',
  match   =>  '^IdentityFile'
}

file_line { 'passwd_auth':
  ensure  =>  present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   =>  '^PasswordAuthentication'
}
