# Web stack debugging #3
> Each file in this repository holds code that illustrates Web stack debugging
> specific to the Bash Scripting & DevOps.

## Description of what each file shows:
* 0-strace_is_your_friend.pp: Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

	Hint:
	- `strace` can attach to a current running process
	- You can use [tmux](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) to run [strace](https://strace.io/) in one window and `curl` in another one
	Requirements:
	- Your `0-strace_is_your_friend.pp` file must contain Puppet code
	- You can use whatever Puppet resource type you want for you fix
