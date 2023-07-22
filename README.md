# Safe Snapraid

Examples

1. Run 
    ```bash
    docker run -ti 
        --privileged 
        --net=host --pid=host --ipc=host 
        --volume /:/host 
        busybox 
        chroot /host
    ```