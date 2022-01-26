def defractalize(fractal):
    while fractal in fractal:
        fractal.remove(fractal)
