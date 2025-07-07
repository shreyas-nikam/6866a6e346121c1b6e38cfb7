
def calculate_bilateral_links(num_intermediaries):
    """Calculates the number of bilateral links in a network."""
    return num_intermediaries * (num_intermediaries - 1) // 2

def calculate_ccp_links(num_intermediaries):
    """Calculates the number of links to a CCP."""
    return num_intermediaries
