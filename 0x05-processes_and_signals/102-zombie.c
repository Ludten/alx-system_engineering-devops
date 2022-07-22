#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - Zombie enabler
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - check the code.
 *
 * Return: Always 0.
 */
int main(void)
{
	int i;
	pid_t child_pid, my_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		my_pid = getpid();
		if (child_pid == -1)
		{
			perror("Error:");
			return (1);
		}
		if (child_pid == 0)
		{
			printf("Zombie process created, PID: %u\n", my_pid);
			exit(0);
		}
	}
	infinite_while();

	return (0);
}
