import atexit

import service_grpc


def finish():
    """Clean up the run."""
    run = service_grpc.run
    if run is None:
        return

    # Clean up the hooks
    for hook in run.hooks:
        hook()
        atexit.unregister(hook)
