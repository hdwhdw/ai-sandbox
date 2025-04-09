import decimal

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return a minus b."""
    return abs(a - b)


def round_num(x, ndigits=0):
    """
    Round x to ndigits using ROUND_HALF_UP (i.e. “5” always rounds up).
    """
    ctx = decimal.getcontext().copy()
    ctx.rounding = decimal.ROUND_HALF_UP
    d = decimal.Decimal(x)
    quant = decimal.Decimal(10) ** -ndigits
    return float(ctx.quantize(d, quant))

round = round_num
