def greet(pal, *args):
    folk = ' and '.join((pal,) + args)
    return f"Hello, {folk}!"
