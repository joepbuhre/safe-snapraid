# Safe Snapraid

Hi. Welcome!

Find here an application which checks the output of `snapraid diff` and parses it. An example output of that command will be:

```log
Loading state from /services/snapraid/snapraid.content...
Comparing...
copy test.log -> test.log
copy test2.log -> test2.log
copy test/test3.log -> test/test3.log
remove test.log
remove test2.log
remove test/test3.log

    21100297 equal
       0 added
       3 removed
       0 updated
       0 moved
       3 copied
       0 restored
There are differences!
```
We see here that everything what has been removed has also been copied. This scenario is totally fine. However if we add a line eg:
```log
remove test4.log
```
This one could not be copied. When this has happened snapraid has two outputs. Option 1 would be outputting a warning, this is handy for debugging. Option 2 would be exitting with a -1 error code. 


## Examples
There are a few examples we can do

1. Run with logs
    ```bash
    docker run --rm ghcr.io/joepbuhre/safesnapraid:latest 
    ```
2. Run with exit code to execute snapraid sync when everything is okay
    ```bash
    docker run --rm \
        ghcr.io/joepbuhre/safesnapraid:latest \
        --diff "$(snapraid diff)" \
        --exit-only \
        && snapraid sync

    ```